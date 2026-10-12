"""Regenerate performance reports on the latest main; never merge generated files.

Only immutable snapshots are carried from the event checkout. Each push retry
starts from a fresh remote head, preserving forecasts, result cache and code.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SNAPSHOTS = Path("football_output_v2/performance/snapshots")
OUTPUTS = ("football_output_v2/performance", "football_output_v2/readable/football_performance_report.xlsx")


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], check=check,
                          text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def merge_snapshots(source: Path, destination: Path) -> None:
    """Copy missing snapshot files; an existing different byte is a hard error."""
    if not source.exists():
        return
    for item in sorted(source.rglob("*")):
        if item.is_symlink():
            raise ValueError(f"Snapshot symlink is not allowed: {item}")
        if not item.is_file():
            continue
        target = destination / item.relative_to(source)
        if target.exists():
            if target.read_bytes() != item.read_bytes():
                raise ValueError(f"Immutable snapshot conflict: {target}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(item, target)


def publish(repo: Path, *, remote: str = "origin", branch: str = "main",
            attempts: int = 3, review_command: list[str] | None = None) -> None:
    repo = repo.resolve()
    command = review_command or [sys.executable, "performance_tracking.py", "review"]
    with tempfile.TemporaryDirectory(prefix="performance-publish-") as temporary:
        temporary = Path(temporary)
        saved = temporary / "snapshots"
        merge_snapshots(repo / SNAPSHOTS, saved)
        for attempt in range(attempts):
            git(repo, "fetch", remote, branch)
            base = git(repo, "rev-parse", "FETCH_HEAD").stdout.strip()
            work = temporary / f"attempt-{attempt}"
            git(repo, "worktree", "add", "--detach", str(work), base)
            try:
                merge_snapshots(saved, work / SNAPSHOTS)
                subprocess.run(command, cwd=work, check=True)
                for path in OUTPUTS:
                    if (work / path).exists():
                        git(work, "add", "--", path)
                if git(work, "diff", "--cached", "--quiet", check=False).returncode == 0:
                    print("Performance outputs already current.")
                    return
                git(work, "-c", "user.name=github-actions[bot]", "-c",
                    "user.email=41898282+github-actions[bot]@users.noreply.github.com",
                    "commit", "-m", "Update forward-only gameweek performance reports [skip ci]")
                result = git(work, "push", remote, f"HEAD:refs/heads/{branch}", check=False)
                if result.returncode == 0:
                    print(result.stdout + result.stderr)
                    return
                git(repo, "fetch", remote, branch)
                latest = git(repo, "rev-parse", "FETCH_HEAD").stdout.strip()
                if latest == base:
                    raise RuntimeError("Report push failed without a concurrent update: " + result.stderr)
                print("Main advanced; regenerating reports from the new head.")
            finally:
                git(repo, "worktree", "remove", "--force", str(work))
    raise RuntimeError(f"Main kept advancing; report publishing stopped after {attempts} attempts")


if __name__ == "__main__":
    publish(Path(__file__).resolve().parent)
