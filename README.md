# PS5Utils
 
Uses python 3, install at https://www.python.org/downloads/
In command prompt install all of the packages in requirements.txt using pip (Navigate to the folder with the download, do pip install -r "requirements.txt")
Targetlinkopener.py is used by another program

Target checkerjson.py is the stock checker program. 

Requires an API Link (See the notion page to get it)

Notifies by webhook and alarm (see how to set up a discord webhook here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). 
When the API call changes it immediately notifies via webhook
Also saves the api changes as a text file - after the drop you can review the api data to see if there are any patterns.

If consoles are in stock it plays the alarm and sends store links of each of the stores that are in stock to the webhook, and opens them up in chrome too

The store links are nice since you can easily click set to my store on the page and then try that store, no need to manually search for which ones are in stock and select those as mystore

Pressing the ~ key will also open up the place order page once you've carted a console if any store pages have opened up, skipping the view cart page

Sends consoles in order of how close they are to the zipcode, with closest being sent first (and at the top of the discord channel)

Checks the api every 2-3 seconds
Constantly sends messages on discord (with no ping) so that you can make sure the bot is running even if you're not at your computer

Look at the top few lines of code to put your api link and webhook data in before you run - otherwise will return an error
I recommend running from IDLE


checkoutspammer.py is an aid for checking out

We've noticed with target it helps to spam the checkout button. This program locates all instances of the checkout button on screen and spams them for x seconds (you can decide, default is 100

Since it locates all instances you should be able to do splitscreen and have twice the chances of checking out

Go through the target checkout process and take multiple screenshots of the place order button in whatever settings you plan to use (use the same zoom settings and same browser)
I have included some screenshots but they might not work super well for your computer

Press ctrl+y in order to stop the clicking (and regain control of mouse)
