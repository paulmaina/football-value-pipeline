"""Support dotted unittest names alongside existing sibling fixture imports."""
from pathlib import Path
import sys

test_directory = str(Path(__file__).resolve().parent)
if test_directory not in sys.path:
    sys.path.insert(0, test_directory)
