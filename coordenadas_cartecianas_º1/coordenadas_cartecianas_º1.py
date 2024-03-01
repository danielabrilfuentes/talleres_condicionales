# input 
X = int(input("ingrese la coordenada x:"))
Y = int(input("ingrese la coordenada y:"))

# processing 
if X == 0:
    if Y == 0:
        print("la coordenada" ,(X , Y), "esta en el origen")
    else:
        print("la coordenada" ,(X , Y), "esta en el eje y")
elif Y == 0:
    print("la coordenada" ,(X , Y), "esta en el eje x")
elif X > 0:
    if Y > 0:
        print("la coordenada" ,(X , Y), "esta en el cadrante 1")
    else:
        print("la coordenada" ,(X , Y), "esta en el cuadrante 4")
elif Y < 0:
    print("la coordenada" ,(X , Y), "esta en el cuadrante 3")
else:
    print("la coordenada" ,(X , Y), "esta en el cuadrante 2")


