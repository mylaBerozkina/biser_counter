def write_biser_order_txt_file(dictionary, dict_for_biser):
    # compare our result with biser that we have
    for key in dictionary:
        if key in dict_for_biser:
            new_value = dict_for_biser[key] - dictionary[key]
            if new_value > 0:
                dictionary[key] = 0
            else:
                dictionary[key] = - new_value
    # sort keys for getting sorted list of biser in order
    keys = list(dictionary.keys())
    keys.sort()

    # write a txt file for order
    with open("biser_order.txt", "w+") as file:
        for key in keys:
            if dictionary[key] == 0:
                continue
            else:
                string = key +"	" + str(dictionary[key]) + "\n"
                file.write(string)
