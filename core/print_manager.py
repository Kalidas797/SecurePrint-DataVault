import os

def print_pdf(pdf_path):
    try:
        if os.path.exists(pdf_path):
            os.startfile(pdf_path, "print")
    except OSError:
        pass
