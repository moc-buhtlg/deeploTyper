import pyautogui as pg
import numpy as np
from time import sleep
from keyboard import wait

black=np.array([0,0,0],dtype=np.uint8) # по какому цвету ровняем

 ###############################
#       keybinds for AI23       #
#  x - run script               #
#  z - рука                     #
#  c - text                     #
#  esc - отмена редакта текста  #
 ###############################

while True:
    wait("x")

    img = np.asarray(pg.screenshot(),dtype=np.uint8)
    x, y = pg.position()
    xline=img[y,:,:]
    yline=img[:,x,:]

    rix, lex, upy, doy = xline.shape[0], 0, 0, yline.shape[0]

    for dx in range(xline.shape[0]-x): #right
        if not xline[x+dx].any():
            rix=x+dx
            break

    for dx in range(x): #left
        if not xline[x-dx].any():
            lex=x-dx
            break

    for dy in range(y): #up
        if not yline[y-dy].any():
            upy=y-dy
            break

    for dy in range(yline.shape[0]-y): #down
        if not yline[y+dy].any():
            doy=y+dy
            break

    mx, my = (rix + lex)//2, (upy + doy)//2


    pg.press("c")
    pg.moveTo(lex,upy)
    pg.mouseDown(button='left')
    pg.moveTo(rix,doy)
    pg.moveTo(rix+1,doy+1)
    pg.mouseUp(button='left')

    pg.write("sss")
    pg.press(['esc',"z"])

    sleep(0.1)









