import pathlib
from pathlib import Path


def get_root_path() -> Path:
    return pathlib.Path(__file__).resolve().parents[3]
