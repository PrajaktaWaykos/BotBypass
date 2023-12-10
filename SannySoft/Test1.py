from selenium import webdriver
from PIL import Image

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)

driver.get("https://bot.sannysoft.com/")

driver.save_screenshot('screenshot.png')
image = Image.open('screenshot.png')
image.show()