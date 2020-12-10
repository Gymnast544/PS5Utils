import webbrowser
import keyboard
import threading


webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

ps5link = "https://www.target.com/p/playstation-5-console/-/A-81114595"
checkoutlink = "https://www.target.com/co-review"


def open_store(storename, storeid):
    x = threading.Thread(target=linkopener, args=(storename, storeid))
    x.start()

def linkopener(storename, storeid):
    storename=storename.replace(" ", "-")
    #webbrowser.get("chrome").open(ps5link)
    webbrowser.get("chrome").open("https://www.target.com/sl/"+storename+"/"+str(storeid))
    keyboard.wait("`")
    webbrowser.get("chrome").open(checkoutlink)

#open_store("Gaithersburg", "1193")
