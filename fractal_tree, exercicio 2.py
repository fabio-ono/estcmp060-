# Importando a biblioteca turtle para o projeto.
import turtle
from turtle import *

# Criando o objeto caneta para desenhar as figuras.
caneta = turtle.Turtle()

# Personalizando o título da janela onde aparecerão os desenhos.
turtle.title("Y Fractal Tree!")
# Modificando a velocidade do desenho.
caneta.speed("fastest")
# Posicionando a caneta para cima.
caneta.left(90)

# Declarando o ângulo que será usado na árvore e em seus galhos.
angulo = 30


# Função que desenhará a árvore de acordo com o tamanho desejado
# e a quantidade de galhos.
def arvore(tamanho, nivel):
    if nivel > 0:
        # Transicionando a cor da linha para verde de acordo com a mudança de nivel.
        colormode(255)
        # Trocando a cor do traço de acordo com o nível.
        caneta.pencolor(0, 255//nivel, 0)

        # Desenhando a base da árvore.
        caneta.forward(tamanho)
        caneta.right(angulo)

        # Instrução responsável por desenhar os galhos do lado esquerdo da árvore.
        arvore(0.8 * tamanho, nivel - 1)
        caneta.pencolor(0, 255//nivel, 0)
        caneta.left(2 * angulo)

        # Instrução responsável por desenhar os galhos do lado direito da árvore.
        arvore(0.8 * tamanho, nivel - 1)
        caneta.pencolor(0, 255//nivel, 0)

        caneta.right(angulo)
        caneta.forward(-tamanho)


# Árvore de tamanho 80 com 7 subníveis
arvore(80, 7)

# .done() usado para deixar a janela aberta após o término do desenho
turtle.done()
