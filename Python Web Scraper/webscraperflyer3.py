import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By

def suppress_exception_in_del(uc):
    old_del = uc.Chrome.__del__

    def new_del(self) -> None:
        try:
            old_del(self)
        except:
            pass
    
    setattr(uc.Chrome, '__del__', new_del)

suppress_exception_in_del(uc)

# Initializing driver 
driver = uc.Chrome() 
 
# Try accessing a website with antibot service 
driver.get("https://namazvakitleri.diyanet.gov.tr/tr-TR/9560/izmir-icin-namaz-vakti")
driver.implicitly_wait(5)
print(driver.find_element(By.TAG_NAME, "body").text)
remainingClosest = driver.find_element(By.ID, 'remainingTimeField').get_attribute("innerHTML")
prayerTimes_list = []
prayerTimes = driver.find_elements(By.CLASS_NAME, "tpt-time")
for times in prayerTimes:
    prayerTimes_list.append(times.text)

print("Sonraki vakte kalan süre: "+remainingClosest)
print("Imsak: "+prayerTimes_list[0])
print("Gunes: "+prayerTimes_list[1])
print("Ogle: "+prayerTimes_list[2])
print("Ikindi: "+prayerTimes_list[3])
print("Aksam: "+prayerTimes_list[4])
print("Yatsi: "+prayerTimes_list[5])
assert "No results found." not in driver.page_source
driver.quit()