from email import message_from_file
from email.message import Message
from pathlib import Path
import sys
from typing import List, Union

def eml_to_html(eml_path: Union[str, Path]):
    eml_path: Path = Path(eml_path)
    if not eml_path.is_file():
        print(f"Skipping {eml_path}; is not a file")

    if eml_path.suffix is not ".eml":
        print(f"Skipping {eml_path}; not an .eml file")

    html_path: Path = eml_path.with_suffix(".html")
    with eml_path.open(mode="r") as eml_file, html_path.open(mode="w") as html_file:
        message: Message = message_from_file(eml_file)
        payload: str = message.get_payload()
        html_file.write(payload)

if __name__ == "__main__":
    file_paths: List[str] = sys.argv
    
    for file_path in file_paths:
        eml_to_html(file_path)
