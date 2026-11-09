"""Copy the verified historical benchmark inputs from the pinned Git commit."""
import json
from pathlib import Path

from historical_benchmark import materialize_inputs

root = Path(__file__).resolve().parent.parent
config_path = root / "historical_benchmark_config.json"
config = json.loads(config_path.read_text(encoding="utf-8"))
manifest = json.loads((root / config["input_manifest"]).read_text(encoding="utf-8"))
destination = root / "workflow_artifacts" / "shortlist-audit" / "pinned_inputs"
materialize_inputs(root, destination, config, manifest)
print(destination)
