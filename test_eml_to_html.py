from glob import glob
from pathlib import Path

import pytest
from eml_to_html import eml_to_html


@pytest.mark.parametrize("eml_path_str", glob("test_emails/*.eml"))
def test_eml_to_html(eml_path_str: str):
    eml_path: Path = Path(eml_path_str)
    html_path: Path = eml_to_html(eml_path)

    assert html_path.exists()
    assert html_path.stat().st_size > 0
