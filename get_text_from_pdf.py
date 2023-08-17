import PyPDF2

def get_text_from_pdf(pdf_doc: str):
    pdf_file_obj = open(pdf_doc, 'rb')

    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

    for i in range(len(pdf_reader.pages)):
        page_one_obj = pdf_reader.pages[i]
        text_page_one = page_one_obj.extract_text()

        if i < len(pdf_reader.pages) - 1:
            page_two_obj = pdf_reader.pages[i+1]
            text_page_two = page_two_obj.extract_text()

        if not text_page_one.count("Count"):
            text_page = "Beads chart not found"
            i += 1
        elif text_page_two.count("Count"):
            text_page = text_page_one + text_page_two
            break
        else:
            text_page = text_page_one
            break

    pdf_file_obj.close()

    return text_page
