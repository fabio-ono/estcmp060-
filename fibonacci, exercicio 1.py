# Importando a biblioteca turtle para o projeto.
import turtle
import math

# Coleta o número de iterações
num_iteracoes = int(input("Digite o número de iterações: "))

# Setup da caneta
caneta = turtle.Turtle()

# "tamanho" representa o fator multiplicativo que determina
# se aumenta ou diminui a escala da figura dos quadrados.
tamanho = 20


def fibonacci(num_iteracoes):
    val_a = 0
    val_b = 1
    quadrado_a = val_a
    quadrado_b = val_b

    # Alterando a cor dos quadrados para laranja.
    caneta.pencolor("orange")

    # Desenhando o primeiro quadrado
    caneta.forward(val_b * tamanho)
    caneta.left(90)
    caneta.forward(val_b * tamanho)
    caneta.left(90)
    caneta.forward(val_b * tamanho)
    caneta.left(90)
    caneta.forward(val_b * tamanho)

    # Sequencia fibonacci.
    fib = quadrado_b
    quadrado_b = quadrado_b + quadrado_a
    quadrado_a = fib

    # Desenhando os outros quadrados.
    for i in range(1, num_iteracoes):
        caneta.backward(quadrado_a * tamanho)
        caneta.right(90)
        caneta.forward(quadrado_b * tamanho)
        caneta.left(90)
        caneta.forward(quadrado_b * tamanho)
        caneta.left(90)
        caneta.forward(quadrado_b * tamanho)

        # Sequencia fibonacci.
        fib = quadrado_b
        quadrado_b = quadrado_b + quadrado_a
        quadrado_a = fib

    # Posicionando a caneta no primeiro quadrado.
    caneta.penup()
    caneta.setposition(tamanho, 0)
    caneta.seth(0)
    caneta.pendown()

    # Posicionando a caneta para cima.
    caneta.left(90)
    # Desenhando a espiral.
    for i in range(num_iteracoes):
        # Alterando a cor da espiral para azul.
        caneta.pencolor("blue")
        print(val_b)
        espiral = math.pi * val_b * tamanho / 2
        espiral = espiral / 90
        for j in range(90):
            caneta.forward(espiral)
            caneta.left(1)

        fib = val_a
        val_a = val_b
        val_b = fib + val_b


# Condição para que o número de iterções seja maior que 0
# caso contrário o programa não será executado
if num_iteracoes > 0:
    print("Sequencia fibonacci para {}".format(num_iteracoes), "Elementos: ")
    caneta.speed(50)
    fibonacci(num_iteracoes)
    turtle.done()

else:
    print("Número de iterações precisa ser maior que 0!")
