# classmethod y staticmethod
# classmethod: recibe cls como parametro para modificar atributos de clase.
# staticmethod: se usa para definir un método que no necesita instancia de la clase.

class Person:
    role = "mid-level"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_role(cls, new_role):
        cls.role = new_role

    @staticmethod
    def is_older(age):
        return age >= 18


# Outputs
person_one = Person("John", 30)
person_two = Person("James", 31)

print(person_one.role)  # mid-level
print(person_two.role)  # mid-level

Person.change_role("senior")

print(person_one.role)  # senior
print(person_two.role)  # senior

print(Person.is_older(20))  # True
print(Person.is_older(15))  # False
