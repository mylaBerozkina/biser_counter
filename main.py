from get_text_from_pdf import get_text_from_pdf

text_page = get_text_from_pdf('i_love_sea.pdf')

check = text_page.splitlines()
#print(check)
i = 0
while i < len(check):
	if len(check[i]) < 3 or check[i].count('.'):
		check.remove(check[i])
	else:
		i += 1
#print(check)
ch = "".join(check)
x = ch.split("Chart #:")
x.pop(0)

for i in x:
	y = i.split("Count:")
	x.insert(x.index(i), y)
	x.remove(i)

for i in x:
	i[0] = i[0][-5:]
	dict_item = {i[0]:i[1]}
	x.insert(x.index(i), dict_item)
	x.remove(i)
print(x)


