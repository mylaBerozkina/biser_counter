import re

def create_dictionary(text_page: str):
    check = text_page.splitlines()

    i = 0
    while i < len(check):
        if len(check[i]) < 3 or check[i].count('.'):
            check.remove(check[i])
        else:
            i += 1

    ch = "".join(check)
    x = ch.split("Chart #:")
    x.pop(0)

    for i in x:
        y = i.split("Count:")
        x.insert(x.index(i), y)
        x.remove(i)

    dictionary = {}

    for i in x:
        key_item = re.findall(r"\d{5}", i[0])
        if not bool(key_item):
            key_item = [i[0][-5:]]
        try:
            dictionary[key_item[0]] = int(i[1])
        except ValueError:
            value_item = re.findall(r"^\d{1,5}", i[1])
            dictionary[key_item[0]] = int(value_item[0])

    return dictionary