import PyPDF2


def get_text_from_pdf(pdf_doc: str):
    text_page = ''
    try:
        with open(pdf_doc, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            #   get text from page in pdf document
            for i in range(len(pdf_reader.pages)):
                page_one_obj = pdf_reader.pages[i]
                text_page_one = page_one_obj.extract_text()
                #   except error for the next checking
                if i < len(pdf_reader.pages) - 1:
                    page_two_obj = pdf_reader.pages[i + 1]
                    text_page_two = page_two_obj.extract_text()
                    #   check if we get all Beads Chart
                    if not text_page_one.count("Count"):
                        text_page = "Beads chart not found"
                        i += 1
                    elif text_page_two.count("Count"):
                        text_page = text_page_one + text_page_two
                        break
                    else:
                        text_page = text_page_one
                        break
    except PyPDF2.errors.PdfReadError:
        print('Put in container folder only pdf-file, please')

    return text_page
