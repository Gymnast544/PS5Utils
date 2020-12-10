import pyautogui
import threading
import time
import keyboard

pyautogui.PAUSE = 0
waitbetweenclicks = .11
secondsclicking = 100

images = ["target1.png", "target2.png", "target3.png", "target4.png"]#add any more images of the center of the checkout button here - HIGHLY RECOMMENDED THAT YOU TAKE SOME YOURSELF AND ADD THEM


def spamlocation(pos):
    global stop
    print("Thread started at position", pos)
    starttime = time.time()
    while time.time()-starttime<secondsclicking and not stop:
        #runs for x seconds
        pyautogui.click(pos)
        time.sleep(waitbetweenclicks)
    print("Thread ended")


stop = False

def stopClicking():
    global stop
    print("Stopping")
    stop = True
    quit()

positions = []

keyboard.add_hotkey("ctrl+y", stopClicking)


print("Starting the checking")
while True:
    for image in images:
        for pos in pyautogui.locateAllOnScreen(image, confidence=.75):
            positiontoadd = (pos.left+(pos.width/2),pos.top+(pos.height/2))
            shouldAdd = True
            for existingpos in positions:
                if abs(existingpos[0]-positiontoadd[0])<100 and abs(existingpos[1]-positiontoadd[1])<100:
                    shouldAdd = False
                else:
                    print("Difference of", abs(existingpos[0]-positiontoadd[0]), abs(existingpos[1]-positiontoadd[1]))
            if shouldAdd:
                positions.append(positiontoadd)
                t = threading.Thread(target=spamlocation, args=((positiontoadd),))
                t.start()
