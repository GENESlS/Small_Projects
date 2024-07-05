#import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#first version, more hacker style, need good proxy


#change here, need good proxy, free ones rarely work
proxy = "32.223.6.94:80"    

# Create Chromeoptions instance 
options = Options()
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

options.add_argument("--headless=new")
options.add_argument(f"--proxy-server={proxy}")
 
# Setting the driver path and requesting a page 
driver = webdriver.Chrome(
    #service=Service(ChromeDriverManager().install()),
    options=options
)
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  
 
#driver.get("https://www.google.com")
#driver = uc.Chrome()
#driver = webdriver.Edge()
driver.get("https://namazvakitleri.diyanet.gov.tr/tr-TR/9560/izmir-icin-namaz-vakti")
#driver.maximize_window() 
driver.implicitly_wait(30)

#assert "Diyanet" in driver.title
#remaining_time = driver.find_element(By.ID, 'remainingTimeField')
#print (driver.page_source.encode("utf-8"))
print(driver.find_element(By.TAG_NAME, "body").text)
remainingClosest = driver.find_element(By.ID, 'remainingTimeField').get_attribute("innerHTML")
prayerTimes_list = []
prayerTimes = driver.find_elements(By.CLASS_NAME, "tpt-time").get_attribute("innerHTML")
for times in prayerTimes:
    prayerTimes_list.append(times)

print("Sonraki vakte kalan süre: "+remainingClosest)
print("Imsak: "+prayerTimes_list[0])
print("Gunes: "+prayerTimes_list[1])
print("Ogle: "+prayerTimes_list[2])
print("Ikindi: "+prayerTimes_list[3])
print("Aksam: "+prayerTimes_list[4])
print("Yatsi: "+prayerTimes_list[5])
assert "No results found." not in driver.page_source
driver.close()
#print(remaining_time)