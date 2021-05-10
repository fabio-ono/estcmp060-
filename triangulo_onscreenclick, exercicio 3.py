# Importando a biblioteca turtle para o projeto.
import turtle

# Usamos o Screen() para criar uma janela do turtle.
janela = turtle.Screen()

# Usando a ferramenta .title para mudar o título da janela onde serão criados os triângulos.
turtle.title("Crie triângulos clicando na tela!")

# Criando o objeto "triangulo" para fazer os desenhos.
triangulo = turtle.Turtle()

# Alterando alterando a cor da caneta para azul.
triangulo.pencolor("blue")


def funcao_triangulo(x, y):
    # Usando .penup e .pendown para mover a caneta para diferentes pontos sem desenhar nada na tela.
    triangulo.penup()
    # Usando o .goto para definir onde serão feitos os desenhos baseados em localizações de x e y
    # como em um gráfico.
    triangulo.goto(x, y)
    triangulo.pendown()

    # Usando uma estrutura de repetição para criar o desenho do triângulo.
    for i in range(3):
        # Usando o .forward para criar uma linha reta.
        triangulo.forward(100)
        # Usando o .left para fazer a forma triangular de acordo com angulação de 120 graus
        triangulo.left(120)
        triangulo.forward(100)


# Usamos o .onscreenclick para informar a posição atual do cursor
# mostrando onde deve ser feito o desenho.
turtle.onscreenclick(funcao_triangulo, 1)

# Usamos o .done() para manter a janela do turtle aberta.
turtle.done()
