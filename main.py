import PyPDF2

pdfFileObj = open('Cotton_ornament_Free.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)

pageObj = pdfReader.pages[1]

textPage0 = pageObj.extract_text()

pdfFileObj.close()

check = textPage0.splitlines()
i = 0
while i < len(check):
	if len(check[i]) < 4:
		check.remove(check[i])
	else:
		i += 1

ch = "".join(check)
x = ch.split("Chart #:")
x.pop(0)
check = x[1][0][-5:]

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



