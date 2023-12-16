# PYC Inner Network Scraper v.1.0
# @A2rae c. 2023
# Licensed under the GNU Affero General Public License v3.0
# Refer to LICENSE.txt for the full print :)
# Refer to the README for full instructions.

from selenium import webdriver # This program uses Python's Selenium.
driver = webdriver.Chrome() # And also Chrome Browser Drivers, please remember to install the one that is the nearest to your browser's version

from selenium.webdriver.common.keys import Keys #Here's Selenium's modules.
from selenium.webdriver.common.by import By # Note that when you're scraping data usually you'll only ever need to use Keys and By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # Not part of Selenium, this is a base Python module :)

# The URL, change to your convienience.
driver.get("") # Paste the PYCnet login page web address here

# This part gets the login box on the front page, and inputs the text into the box.
element = driver.find_element(By.ID , "username")
element.send_keys("") # Input your username here

ele = driver.find_element(By.ID, "password")
ele.send_keys("") # Input your password here
ele.send_keys(Keys.RETURN) 

# This is mainly to allow the page enough time to load before the find functions come into play, I'm just too lazy to do WebDriverWait.
# Change the number to your convienience, it's based in seconds.
time.sleep(3)


try:
 driver.find_elements(By.ID , "divrowy") # Finds the mail elements, yes, the ID for all of them is divrowy.
 driver.find_elements(By.CLASS_NAME , "col-md-6") # Finds the elements within the mail.
 title = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME , "forumlink")))
 pyc = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME , "col-md-4")))
 date = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By. CLASS_NAME ,"col-md-2")))
 msg = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.NAME , "dels[]"))) # Couldn't get this one to work, will revise when free.
 # Displays the results in the command window.
 for title in title:
  print(title.text)
 for pyc in pyc:
  print(pyc.text)
 for date in date:
  print(date.text)
 for msg in msg:
  print(msg.text)
 # It's ideal to immediately screencap the whole window once the data is released, for some reason it closes automatically on my device around 10 seconds after it's done.
 f = open("data.txt" , 'w' , encoding="utf_8") 
 f.write(title.text)
 f.write(pyc.text) 
 f.write(date.text)
 f.write(msg.text) # As of now, this part only writes the last of the first page of your mailbox into data.txt, couldn't find a fix for it right now. Improve as you wish.

except:
    print("Oops, that didn't work.") # Error message.
else:
    open("data.txt", "r")
    print("Done! Check data.txt") # Success message :)
    driver.close()

