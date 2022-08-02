# eml-to-html
Converts `.eml` email files to `.html` files.

## Installation
```
pip install eml-to-html
```

## Usage
```
eml-to-html *.eml
```

Outputs

```
➜  eml-to-html git:(master) ✗ python eml_to_html.py test_emails/*.eml
🟢 Written `test_email_1.html`
🟢 Written `test_email_2.html`
```

File tree is now:

```
➜  eml-to-html git:(master) ✗ tree test_emails 
test_emails
├── test_email_1.eml
├── test_email_1.html
├── test_email_2.eml
└── test_email_2.html

0 directories, 4 files
```

## About
This micro module was written by [Jeroen Overschie](https://jeroenoverschie.nl/) in 2022.