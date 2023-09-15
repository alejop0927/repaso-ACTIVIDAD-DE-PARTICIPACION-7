from dataclasses import dataclass
from typing import List

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elem == elemento for elem in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        new_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        new_conjunto.unir(self)
        new_conjunto.unir(otro_conjunto)
        return new_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nombre_conjunto = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_conjunto)
        for elemento in elementos_comunes:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        nombres_elementos = ', '.join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({nombres_elementos})"


elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

conjunto1 = Conjunto("Conjunto1")
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)

conjunto2 = Conjunto("Conjunto2")
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

print(conjunto1)
print(conjunto2)
