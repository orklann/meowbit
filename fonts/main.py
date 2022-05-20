from meowbit import screen
from font5 import Font5
from font8 import Font8

f = open("file.txt", "r")
text = f.read()
f.close()
screen.sync = 0
screen.fill(0)
font5 = Font5(screen.pixel)
font5.text(text, 10, 20, 255)
font8 = Font8(screen.pixel)
font8.text(text, 0, 40, 255)
screen.refresh()

