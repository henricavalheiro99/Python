import math

c1 = int(input("Cateto 1: "))
c2 = int(input("Altura do Triangulo: "))
h = math.sqrt(c1*c1+c2*c2)
print(f"Hipotenusa: {h:.1f}")