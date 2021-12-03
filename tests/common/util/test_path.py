import pathlib

from app.common.util.path import get_root_path


def test_get_root_path() -> None:
    current_file_path = pathlib.Path(__file__)
    assert get_root_path() / "tests" / "common" / "util" / "test_path.py" == current_file_path
