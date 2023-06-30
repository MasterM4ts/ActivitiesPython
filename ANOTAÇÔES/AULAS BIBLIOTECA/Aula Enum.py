#Apresentação#

import enum

class Animal(enum.Enum):
    cachorro = 1
    gato = 2
    pantera = 2

#Comparação Usando "is".
if Animal.cachorro is Animal.gato:
    print("Cão e gato são os mesmos animais.")
else:
    print("Cão e gato são animais diferentes.")

#Comparação Usando "!=".
if Animal.pantera != Animal.gato:
    print("Leões e gatos são Diferentes.")
else:
    print("Pantera e gato são iguais.")