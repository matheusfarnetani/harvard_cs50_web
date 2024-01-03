people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# # Define how to sort
# def f(person):
#     return person["name"]

# # Tells sort function to sort by what you defined
# people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)