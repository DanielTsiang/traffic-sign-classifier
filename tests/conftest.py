import sys
from pathlib import Path

root_path = Path(__file__).parents[1].resolve()
source_code_path = root_path
sys.path.extend([root_path.as_posix(), source_code_path.as_posix()])
SAMPLE_PATH = source_code_path / "static" / "sample"
