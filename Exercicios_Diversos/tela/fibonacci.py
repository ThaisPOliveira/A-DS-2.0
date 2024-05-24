import turtle
quadrado=turtle.Turtle()
circulo=turtle.Turtle()
circulo.hideturtle()
quadrado.hideturtle()

quadrado.speed(0)
fibonnaci=15
anterior, proximo=1,1
for step in range(2):
  
    for _ in range (5):
        quadrado.forward(proximo)
        quadrado.left(90)
    quadrado.forward(proximo)  
    circulo.circle(proximo, 90) 
   
for step in range(fibonnaci):
    proximo+=anterior
    for _ in range (5):
        quadrado.forward(proximo)
        quadrado.left(90)
    quadrado.forward(proximo)  
    circulo.circle(proximo, 90) 
    anterior=proximo-anterior