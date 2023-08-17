from get_text_from_pdf import get_text_from_pdf
from create_dictionary import create_dictionary

text_page = get_text_from_pdf('Olha 1.pdf')

dictionary = create_dictionary(text_page)

print(dictionary)
