import PyPDF2

def get_text_from_pdf(pdf_doc: str):
    pdf_file_obj = open(pdf_doc, 'rb')

    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    for i in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[i]
        text_page = page_obj.extract_text()
        if not text_page.count("Chart"):
            text_page = "Beads chart not found"
            i += 1
        else:
            i = i
            break
    print(i)

    pdf_file_obj.close()
    return text_page

