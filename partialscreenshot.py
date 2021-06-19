import os
import time

from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True

img_dir = 'screenshot'
img_path = os.path.join(os.getcwd(), img_dir)

driver_dir = 'drivers'
driver_path = os.path.join(os.getcwd(),driver_dir)

DRIVER = os.path.join(driver_path, 'chromedriver.exe')
driver = webdriver.Chrome(DRIVER, options=options)
#driver.maximize_window()
driver.implicitly_wait(20)
driver.get('http://localhost:3000/7')
time.sleep(20)
# now that we have the preliminary stuff out of the way time to get that image :D
element = driver.find_element_by_id('src_ip') # find part of the page you want image of
location = element.location
size = element.size
time.sleep(10)
png = driver.get_screenshot_as_png() # saves screenshot of entire page
time.sleep(10)
driver.quit()

im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
im.save(os.path.join(img_path, "fullImage.png"))
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']


im = im.crop((left, top, right, bottom)) # defines crop points
im.save(os.path.join(img_path, '3_src_ip.png')) # saves new cropped image