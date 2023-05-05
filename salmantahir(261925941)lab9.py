##Name: salman tahir
##roll no: 261925941
##lab_9

#Task_1:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class House:
    def __init__(self, address, num_rooms):
        self.address = address
        self.num_rooms = num_rooms
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def remove_person(self, person):
        if person in self.people:
            self.people.remove(person)

    def print_people(self):
        for person in self.people:
            print(f"{person.name} ({person.age})")

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Charlie", 35)
house = House("123 Main St", 3)
house.add_person(person1)
house.add_person(person2)
house.add_person(person3)

house.print_people()
