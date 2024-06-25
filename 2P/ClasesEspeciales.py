import os
os.system('cls' if os.name == 'nt' else 'clear')

class Libro:
    def __init__(self, autor, titulo, cant_paginas):
        self.autor = autor
        self.titulo = titulo
        self.cant_paginas = cant_paginas

    def __str__(self):
        return f'Título: "{self.titulo}", escrito por {self.autor}'
    
    def __len__(self):
        return self.cant_paginas
    
libro = Libro("Stephen King", "It", 1032)
print(str(libro))
print(len(libro))