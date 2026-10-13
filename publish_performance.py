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
            attempts: int = 3, review_command: list[str] | None = None,
            validation_command: list[str] | None = None, artifact_dir: Path | None = None) -> None:
    repo = repo.resolve()
    command = review_command or [sys.executable, "performance_tracking.py", "review"]
    artifacts = (repo / artifact_dir).resolve() if artifact_dir is not None else None
    if artifacts is not None:
        if not artifacts.is_relative_to(repo) or artifacts == repo or artifacts.name != "workflow_artifacts":
            raise ValueError("Artifact destination must be a workflow_artifacts directory inside the checkout")
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
                try:
                    subprocess.run(command, cwd=work, check=True)
                    if validation_command is not None:
                        subprocess.run(validation_command, cwd=work, check=True)
                finally:
                    if artifacts is not None:
                        # Retain this attempt's reports even if validation fails; never copy secrets/raw cache.
                        artifacts.mkdir(parents=True, exist_ok=True)
                        if (artifacts / "performance").exists(): shutil.rmtree(artifacts / "performance")
                        performance = work / "football_output_v2/performance"
                        if performance.exists():
                            shutil.copytree(performance, artifacts / "performance", ignore=shutil.ignore_patterns("snapshots"))
                        workbook = work / OUTPUTS[1]
                        if workbook.exists(): shutil.copyfile(workbook, artifacts / workbook.name)
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
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--api-key-source", choices=("dotenv", "environment"), default="dotenv")
    parser.add_argument("--validate-reports", action="store_true")
    parser.add_argument("--artifact-dir", type=Path)
    args = parser.parse_args()
    publish(Path(__file__).resolve().parent, review_command=[sys.executable,
        "performance_tracking.py", "review", "--api-key-source", args.api_key_source],
        validation_command=([sys.executable, "workflow_checks.py", "reports", "--output",
            "football_output_v2/performance/workflow_health.json", "--github-summary"] if args.validate_reports else None),
        artifact_dir=args.artifact_dir)
