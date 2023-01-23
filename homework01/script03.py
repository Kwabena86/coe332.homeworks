


import names


person = []

people = []

j = 0


for j in range (5):
        person.append(names.get_full_name())
        size = len(person[j]) -1 
        print(person[j] + '' + str(size))


