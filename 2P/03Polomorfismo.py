import os
os.system('cls' if os.name == 'nt' else 'clear')

class Perro:
    def hablar(self):
        print("Guau!")
class Gato:
    def hablar(self):
        print("Miau!")

hachiko = Perro()
garfield = Gato()
animales = [hachiko, garfield]

for animal in animales:
    animal.hablar()