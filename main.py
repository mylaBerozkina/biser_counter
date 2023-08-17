from get_text_from_pdf import get_text_from_pdf
from create_dictionary import create_dictionary
from files import dict_for_biser
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

# getting how many gramm of biser we need

dictionary = beads_counter("Cotton_ornament_Free.pdf", "i_love_sea.pdf", "74.pdf")


# compare our result with biser that we have
for key in dictionary:
	if key in dict_for_biser:
		new_value = dict_for_biser[key] - dictionary[key]
		if new_value > 0:
			dictionary[key] = 0
		else:
			dictionary[key] = - new_value

# write a txt file for order

with open("biser_order.txt", "w+") as file:
	for i in dictionary:
		if dictionary[i] == 0:
			continue
		else:
			string = i +"	" + str(dictionary[i]) + "\n"
			file.write(string)