from get_text_from_pdf import get_text_from_pdf
from create_dictionary import create_dictionary


# getting how many gram of biser we need
def beads_counter(pdf_files):
	result_list = []
	for pdf_file in pdf_files:
		text_page = get_text_from_pdf(pdf_file)
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
