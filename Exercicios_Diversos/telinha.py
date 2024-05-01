import turtle
tartaruga=turtle.Turtle()
# tartaruga.shape("arrow")
# tartaruga.right(45)
# tartaruga.fd(100)
# tartaruga.setx(100)
# tartaruga.sety(200)
# tartaruga.home()
# tartaruga.circle(50)
fibonnaci=10
anterior, proximo=1,1

tartaruga.forward(proximo)
tartaruga.left(25)
tartaruga.forward(proximo)
tartaruga.left(25)
tartaruga.forward(proximo)
tartaruga.left(25)
tartaruga.forward(proximo)
tartaruga.left(25)
tartaruga.forward(proximo)
tartaruga.left(25)
tartaruga.forward(proximo)

for step in range(fibonnaci):
    proximo+=anterior 
    tartaruga.forward(proximo)
    tartaruga.left(25)
    tartaruga.forward(proximo)
    tartaruga.left(25)
    tartaruga.forward(proximo)
    tartaruga.left(25)
    tartaruga.forward(proximo)
    tartaruga.left(25)
    tartaruga.forward(proximo)  
    tartaruga.left(25)
    tartaruga.forward(proximo)  
    anterior=proximo-anterior

