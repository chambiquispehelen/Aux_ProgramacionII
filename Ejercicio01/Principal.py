from Anime import Anime
from Televisor import Televisor
from Instrumento import Instrumento


def main():

    # Crear objetos Anime
    a1 = Anime("Naruto", "Shonen", 220)
    a2 = Anime("Death Note", "Misterio", 102)

    # Crear objetos Televisor
    t1 = Televisor("Chic", 4, "OLED")
    t2 = Televisor("Sony", 8, "IPS")

    # Crear objetos Instrumento
    i1 = Instrumento("Violin", "Madera", "Cuerda")
    i2 = Instrumento("Flauta", "Metal", "Aire")

    # Mostrar datos
    print("Televisor:", t1)
    print("Televisor2:", t2)

    print("Instrumento:", i1)
    print("Instrumento2:", i2)
