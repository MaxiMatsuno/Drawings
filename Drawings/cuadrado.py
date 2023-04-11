import turtle

# Crea una ventana para dibujar
ventana = turtle.Screen()

# Crea una tortuga para dibujar
tortuga = turtle.Turtle()

# Dibuja un cuadrado
for i in range(4):
    tortuga.forward(100)
    tortuga.right(90)

# Cierra la ventana al hacer clic en ella
ventana.exitonclick()