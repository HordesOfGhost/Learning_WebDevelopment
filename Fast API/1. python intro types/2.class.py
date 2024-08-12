class Person:
    def __init__(self, name:str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

person = Person('bibek')
print(get_person_name(person))