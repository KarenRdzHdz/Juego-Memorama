"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

Integrantes:
Karen Lizette Rodríguez Hernández - A01197734
Jorge Eduardo Arias Arias - A01570549
Hernán Salinas Ibarra - A01570409

15/09/2021

Exercises marked by ***ejercicio realizado***

"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

tiles = list(range(8)) * 2
#tilesB = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H']
counter = 0

state = {'mark': None}
comprobar = [False] * 16
hide = [True] * 16

# Cuadricula en pantalla
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(105)
        left(90)
    end_fill()

#Coordenadas de xy se asocian a un index de tiles
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 100 + ((y + 200) // 100) * 4)

# Index de tiles a una coordenada x,y
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 4) * 100-200, (count // 4) * 100-200

# Clicks en pantalla
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    cond = True
    global counter
    counter += 1                                                    # ***Exercise 1: count and print taps***
    print("Clicks: " + str(counter))
    # Checar correspondencia para revelar
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    for count in range(16):
        if hide[count] != comprobar[count]:
            cond = False
    if cond:
        print("Juego acabado. Felicidades!")

# Dibuja el fondo y hace visibles las tiles
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
            
    
    mark = state['mark']
    
    

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write((str(tiles[mark]).center(6)), font=('Arial', 34, 'normal'))
        

    update()
    ontimer(draw, 50)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()