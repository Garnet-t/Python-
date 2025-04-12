# rossete.py 4 круга 
import turtle 
t = turtle.Pen()
for x in range(8): # ставить больше 4 + из-за поворота идёт лишний обход
    t.circle(100)
    t.left(60)
