
from selenium import webdriver 
driver = webdriver.Chrome()
import urllib
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver.get ("https://www.google.com")

search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
search_box.send_keys("navyenterprise")
search_box.submit()
results = driver.find_elements(By.ID, "result-stats")
print(results)
for results in results:
    text = results.text.split()[1]
    print(text)
    
options = Options()
options.add_argument("--window-size=1920,1200")
service = Service(options=options, executable_path='/snap/bin/chromium.chromedriver')

wait = WebDriverWait(driver, 7)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "g")))
headings = driver.find_elements(By.CLASS_NAME, "g")  

for heading in headings:

    title = driver.find_element(By.TAG_NAME, 'h3')
    links = driver.find_element(By.CLASS_NAME, 'MjjYud')  
    print(title)
    print(links)
    
f = open("results.txt" , "w")
text = results.text.split()[1]
f.write(text)


