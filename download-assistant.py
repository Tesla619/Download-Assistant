import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Add any additional options to chrome_options if needed
chrome_options = webdriver.ChromeOptions()

# Install the Chrome driver to a temporary location
driver_path = ChromeDriverManager().install()

# Create a Chrome driver instance using the downloaded driver 
#taskkill /IM chromedriver.exe /F
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

EPLINK = "-"
epCount = 1062 + 2

show = "https://www5.gogoanimes.fi/digimon-ghost-game-episode"
    
def delay_click(xpath, delay):
    driver.find_element("xpath", xpath).click()
    time.sleep(delay)

def download(url,ep):
    driver.execute_script('''window.open(" '''+ url + EPLINK + str(ep) + '''","_blank");''')
    driver.get(url + EPLINK + str(ep))
    time.sleep(1000) #was 0.2    
    
    # #Switch Frame & Press Download
    # driver.switch_to.frame("iframe-embed")
    # driver.switch_to.frame("external-embed")    
    
    # #Going to process to download video
    # driver.switch_to.window(driver.window_handles[-1]) #last tab also check if reduntant        
    
    # #Finding the link and loading it to download the video
    # elements = driver.find_elements("tag name", "div")
    # link = elements[8].find_elements("tag name", "a")
    # driver.get(link[0].get_attribute("href"))

if __name__ == "__main__": 
    download(show, 4)
    driver.quit()