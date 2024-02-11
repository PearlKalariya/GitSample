import pyautogui as pg
import time

song=input("enter song")
pg.press("win")
time.sleep(1)
pg.write("spotify")
# time.sleep(1)
pg.press("enter")
pg.moveTo(51,151,duration=4)
pg.click()
pg.moveTo(367,85,duration=3)
pg.click()
pg.hotkey('ctrl','a')
pg.write(song)
pg.press("enter")
# pg.moveTo(565,483,duration=5)
# pg.click()

x,y = pg.locateOnScreen("capture.png",confidence = 0.7)
pg.moveTo(x,y)
pg.doubleclick()