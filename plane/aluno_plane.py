from math import sin, cos, pi, sqrt
from OpenGL.GL import *

# Aqui voce deve definir o corpo desta funcao de modo a incluir as
# transofmacoes, repeticoes, condicionais, etc. necessarias para concluir
# os exercicios.
#
# Pequena referencia rapida das funcoes mais usadas:
#
# - Translacao: glTranslate(dx, dy, dz)
#
# - Rotacao: glRotate(angle, axis_x, axis_y, axis_z)
#
# - Escala: glScale(sx, sy, sz)
#
# - Espelhamento: Usar escala com fator de -1.0 no eixo em relacao ao qual a
#   escala deve ocorrer
#
# - Salvar transformacao atual: glPushMatrix()
#
# - Recuperar ultima transformacao salva: glPopMatrix()


def compor_cena(c):

    c.draw("plane")


def compor_cena_ex1(c):
    glRotate(-45, 1, 0, 0)
    glTranslate(2, 0, 0)
    c.draw("plane")


def compor_cena_ex2(c):
    glRotate(135, 0, 0, 1)
    c.draw("plane")


def compor_cena_ex3(c):
    glTranslate(-1, 0, 0)
    glRotate(45,0,1,0)
    c.draw("plane")


def compor_cena_ex4(c):
    glTranslate(1,1,0)
    glRotate(90, 1, 0, 0)
    glRotate(180, 0, 1, 0)
    c.draw("plane")


def compor_cena_ex5(c):
    glTranslate(0, -1, 0)
    glRotate(180, 0, 1, 0)
    glRotate(90, 1, 0, 0)
    c.draw("plane")


def compor_cena_ex6(c):
    c.draw("plane")


def compor_cena_ex7(c):
    c.draw("plane")


def compor_cena_ex8(c):
    c.draw("plane")
