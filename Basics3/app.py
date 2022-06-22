class Animal:
    pass


class Animal:
    def __init__(self, name, family, genus, species):
        self.name = name
        self.family = family
        self.genus = genus
        self.species = species

    def this_belongs(self):
        print(f"This animal {self.name} belongs to {self.family}, {self.genus}, and its species is {self.species}")
    def __str__(self):
        return f"[Anmial= {self.name}, family= {self.family}, genus= {self.genus}, and species= {self.species}]"
a1 = Animal("Cat","Felidae", "Felis","catus domestica")
a2 = Animal("Dog","Canidae", "Canis", "familiarus domesticus")
a3 = Animal("Goldfish", "Cyprinidae", "Carassius", "auratus")

print(type(a1))
print(type(a2))
print(type(a3))

print(a1.name)
print(a2.name)
print(a3.name)

print(a1.family)
print(a2.family)
print(a3.family)

print(a1.genus)
print(a2.genus)
print(a3.genus)

print(a1.species)
print(a2.species)
print(a3.species)

a1.this_belongs()
a2.this_belongs()
a3.this_belongs()

Animal.this_belongs(a1)
Animal.this_belongs(a2)
Animal.this_belongs(a3)

print(a1)
print(a2)
print(a3)


