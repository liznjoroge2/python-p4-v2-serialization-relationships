# Import the necessary models from models.py
from models import Animal, Enclosure, Zookeeper

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def to_dict(self):
        return {
            'name': self.name,
            'species': self.species,
            'age': self.age
        }

class Enclosure:
    def __init__(self, id, name, animal_count):
        self.id = id
        self.name = name
        self.animal_count = animal_count

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'animal_count': self.animal_count
        }

class Zookeeper:
    def __init__(self, id, name, years_of_experience):
        self.id = id
        self.name = name
        self.years_of_experience = years_of_experience

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'years_of_experience': self.years_of_experience
        }
