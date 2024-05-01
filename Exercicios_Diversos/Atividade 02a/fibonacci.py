import turtle
tartaruga=turtle.Turtle()
circulo=turtle.Turtle()

fibonnaci=15
anterior, proximo=1,1

for step in range(fibonnaci):
    proximo+=anterior
    for _ in range (5):
        tartaruga.forward(proximo)
        tartaruga.left(90)
    tartaruga.forward(proximo)  
    circulo.circle(proximo, 90) 
    anterior=proximo-anterior