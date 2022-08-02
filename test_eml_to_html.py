from pathlib import Path
from eml_to_html import eml_to_html

def test_eml_to_html():
    eml_to_html("./test_email.eml")
    assert Path("./test_email.html").exists()