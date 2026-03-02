from anime import anime
from televisor import Televisor
from instrumento import Instrumento

a1 = anime("Naruto", "Shonen", 220)
a2 = anime("Death Note", "Misterio", 102)
    
t1 = Televisor("Chic", 4, "OLED")
t2 = Televisor("Sony", 8, "IPS")

i1 = Instrumento("Violin", "Madera", "Cuerda")
i2 = Instrumento("Flauta", "Metal", "Aire")

print("Anime1: ", a1)
print("Anime2: ", a2)

print("Televisor:", t1)
print("Televisor2:", t2)

print("Instrumento:", i1)
print("Instrumento2:", i2)
