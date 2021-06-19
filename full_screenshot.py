import os
import time


from PIL import Image
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import definition
from Screenshot import Screenshot_Clipping


# take screenshot
driver_dir = 'drivers'
driver_path = os.path.join(os.getcwd(), driver_dir)
DRIVER = os.path.join(driver_path, 'chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(DRIVER)
driver.maximize_window()
driver.get('http://localhost:3000/7')
driver.implicitly_wait(20)

ob = Screenshot_Clipping.Screenshot()


def cropFromScreenShot():
    element = driver.find_element_by_id("log_count")
    location = element.location
    size = element.size
    driver.save_screenshot(os.path.join(driver_path, "pageImage.png"))

    # crop image
    x = location['x']
    y = location['y']
    width = location['x'] + size['width']
    height = location['y'] + size['height']
    im = Image.open(os.path.join(driver_path, 'pageImage.png'))
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(os.path.join(driver_path, 'element.png'))
    # driver.quit()


def checkPageIsLoaded():
    timeout = 3
    try:
        element_present = EC.presence_of_element_located((By.ID, 'log_count'))
        WebDriverWait(driver, timeout).until(element_present)
        element = driver.find_element_by_xpath("//*[@id = 'log_count']")
        screenshot_as_bytes = element.screenshot_as_png
        with open(os.path.join(driver_path, 'web_screenshot.png'), 'wb') as f:
            f.write(screenshot_as_bytes)
        time.sleep(4)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")


def fullPageScreenSHot():
    time.sleep(4)
    img_url = ob.full_Screenshot(driver, save_path=definition.img_path, image_name='Myimage.png')
    print(img_url)
    driver.close()

    driver.quit()


def htmlElementClipping():
    time.sleep(5)
    element = driver.find_element_by_id('src_ip')
    img_url = ob.get_element(driver, element, r'.')
    print(img_url)

    driver.close()

    driver.quit()
#checkPageIsLoaded()
# cropFromScreenShot()
#fullPageScreenSHot()
htmlElementClipping()