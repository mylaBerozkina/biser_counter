#   get dict with amount of biser that we have for now
def get_biser_store():
    with open('Biser.txt', "r") as file:
        contents = file.read()

        str_to_list = contents.splitlines()

        dict_for_biser = {}
        for i in str_to_list:
            y = i.split("\t")
            try:
                dict_for_biser[y[0]] = int(y[1])
            except ValueError:
                dict_for_biser[y[0]] = 0

    return dict_for_biser
