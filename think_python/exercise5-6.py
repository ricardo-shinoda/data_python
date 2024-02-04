import turtle


def koch_curve(t, x):
    if x < 5:
        t.forward(x)
        return
    else:
        koch_curve(t, x/3)
        t.left(60)
        koch_curve(t, x/3)
        t.right(120)
        koch_curve(t, x/3)
        t.left(60)
        koch_curve(t, x/3)


# Criar a tartaruga
t = turtle.Turtle()

# Chamar a função para desenhar a curva de Koch
koch_curve(t, 100)

# Fechar a janela ao clicar
turtle.exitonclick()
