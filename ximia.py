from ximia_data import chemical_elements
d = input()
d = d.split(" ")
fl = 0
tr = ""
for i in d:
    if i[-1] in "1234567890" and i[0:-1] in chemical_elements:
        tr += str(chemical_elements[i[0:-1]])
        tr += "*"
        tr += str(i[-1])
        tr += "+"
        fl += int(chemical_elements[i[0:-1]]) * int(i[-1])
    elif i in chemical_elements:
        tr += str(chemical_elements[i])
        fl += int(chemical_elements[i])
    else:
        print("ошибка")
tr += "="
print(tr, fl)