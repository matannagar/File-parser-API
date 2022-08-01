import docx2txt
import re
from open_files.clean_html import open_html
from open_files.clean_pdf import open_pdf
from open_files.clean_text import clean_text

def text_extraction(filename):
    if filename[-4:] == "docx":
        text = docx2txt.process(filename)
    elif filename[-4:] == "html":
        text = open_html(filename)
    elif filename[-3:] == "pdf":
        text = open_pdf(filename)
    else:
        with open(filename, 'r') as file:
            text = file.read()

    # remove links, specials signs, emails...
    text = clean_text(text)
    
    return text


def summarize_from_web(url):
    text = open_html(url)
    # remove links, specials signs, emails...
    text = clean_text(text)

    return text
