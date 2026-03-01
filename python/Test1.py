import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option(
    "mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://twitch.tv")

while True:
    try:
        continue_in_web_button = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div/div[2]/div/div[1]/button")
        if continue_in_web_button.is_displayed():
            continue_in_web_button.click()
            break
    except:
        continue

while True:
    try:
        reject_button = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div/div/div/div[3]/div[3]/div/button")
        if reject_button.is_displayed():
            reject_button.click()
            break
    except:
        continue

while True:
    try:
        browse_button = driver.find_element(By.XPATH,"/html/body/div/div[2]/a[2]/div")
        if browse_button.is_displayed():
            browse_button.click()
            break
    except:
        continue

while True:
    try:
        search_bar = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/header/div/div/div/div/input")
        if search_bar.is_displayed():
            search_bar.send_keys("StarCraft II")
            search_bar.send_keys(Keys.RETURN)
            break
    except:
        continue

while True:
    try:
        channels_tab = driver.find_element(By.XPATH,"/html/body/div/main/nav/div/div[2]/div/ul/li[2]/a/div/div/div")
        if channels_tab.is_displayed():
            channels_tab.click()
            break
    except:
        continue
time.sleep(1)
driver.execute_script("window.scrollTo(0, 200)")
time.sleep(1)
driver.execute_script("window.scrollTo(200, 500)")

while True:
    try:
        selected_channel = driver.find_element(By.XPATH,"/html/body/div/main/div/div/div[1]/div/div/div[4]")
        if selected_channel.is_displayed():
            selected_channel.click()
            break
    except:
        continue
time.sleep(5)
driver.save_screenshot("screenshot.png")
driver.close()
driver.quit()
print("Done")