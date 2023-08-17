from get_text_from_pdf import get_text_from_pdf
from create_dictionary import create_dictionary

def beads_counter(*pdf_files):
	result_list = []
	for i in pdf_files:
		text_page = get_text_from_pdf(i)
		dictionary = create_dictionary(text_page)
		result_list.append(dictionary)
	result_dict = {}
	for d in result_list:
		for key in d:
			if key in result_dict:
				result_dict[key] = -(-(result_dict[key] + d[key])//80)
			else:
				result_dict[key] = -(-d[key]//80)

	return result_dict

dictionary = beads_counter("Olha 1.pdf", "i_love_sea.pdf", "Kosiv.pdf")
print(dictionary)
