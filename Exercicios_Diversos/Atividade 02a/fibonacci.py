import turtle
tartaruga=turtle.Turtle()
circulo=turtle.Turtle()
circulo.speed(0)
tartaruga.speed(30)
# tartaruga.shape("arrow")
# tartaruga.right(45)
# tartaruga.fd(100)
# tartaruga.setx(100)
# tartaruga.sety(200)
# tartaruga.home()
# tartaruga.circle(50)
fibonnaci=15
anterior, proximo=1,1

for step in range(fibonnaci):
    proximo+=anterior
    for _ in range (5):
        tartaruga.forward(proximo)
        tartaruga.left(90)
    tartaruga.forward(proximo)  
    circulo.circle(proximo, 90)  # Desenha um quarto de círculo
    

    anterior=proximo-anterior



