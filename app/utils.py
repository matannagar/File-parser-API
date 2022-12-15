import docx2txt
import os

if os.environ.get('MODE') == 'PRODUCTION':
    from app.open_files.clean_html import open_html
    from app.open_files.clean_pdf import open_pdf
    from app.open_files.clean_text import clean_text
else:
    from open_files.clean_html import open_html
    from open_files.clean_pdf import open_pdf
    from open_files.clean_text import clean_text

def text_extraction(filename):
    try:
        if filename[-4:] == "docx":
            text = docx2txt.process(filename)
        elif filename[-4:] == "html":
            text = open_html(filename)
        elif filename[-3:] == "pdf":
            text = open_pdf(filename)
        else:
            with open(filename, 'r', encoding='cp437') as file:
                text = file.read()

        # remove links, specials signs, emails...
        text = clean_text(text)

        return text
    except:
        return "File not supported"

def text_from_web(url):
    text = open_html(url)
    # remove links, specials signs, emails...
    text = clean_text(text)

    return text

def delete_files(folder_path):
#   Check if the folder exists
  if not os.path.exists(folder_path):
    print("The given folder does not exist!")
    return

  # Iterate over all files in the folder
  for filename in os.listdir(folder_path):
    # Construct the full filepath
    file_path = os.path.join(folder_path, filename)

    # Delete the file
    try:
      os.unlink(file_path)
    except Exception as e:
      print("Failed to delete file:", file_path)
      print(e)
