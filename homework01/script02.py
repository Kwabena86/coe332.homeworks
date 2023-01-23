

import names

person = []
people = []

j = 0 
while True:
        person.append(names.get_full_name())

        if (len(person[j]) == 9):
            people.append(person[j])


        if (len(people) == 5):
            break
        j += 1

print (people)


