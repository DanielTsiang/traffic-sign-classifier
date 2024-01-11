import sys
from pathlib import Path

root_path = Path(__file__).parents[1].resolve()
sys.path.extend([root_path.as_posix()])
SAMPLE_PATH = root_path / "static" / "sample"
