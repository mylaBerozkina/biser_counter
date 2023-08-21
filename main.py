import os
from beads_counter import beads_counter
from get_biser_store import get_biser_store
from write_biser_order_txt_file import write_biser_order_txt_file


path_to_files = os.listdir(os.path.curdir + "/beads_patterns")
for i in range(len(path_to_files)):
	path_to_files[i] = "./beads_patterns/" + path_to_files[i]

dictionary = beads_counter(path_to_files)
dict_for_biser = get_biser_store()
write_biser_order_txt_file(dictionary, dict_for_biser)
