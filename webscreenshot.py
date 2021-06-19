import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

img_dir = 'screenshot'
img_path = os.path.join(os.getcwd(), img_dir)

driver_dir = 'drivers'
driver_path = os.path.join(os.getcwd(),driver_dir)

DRIVER = os.path.join(driver_path, 'chromedriver.exe')
driver = webdriver.Chrome(DRIVER)
driver.maximize_window()
driver.implicitly_wait(20)


def test_fullpage_screenshot():
    driver.get('http://localhost:3000/7')
    time.sleep(20)
    element = driver.find_element_by_id("log_count")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '1_log_count.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("nw_traffic")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '2_nw_traffic.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("src_ip")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '3_src_ip.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("dest_ip")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '4_dest_ip.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("threat_metric")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '5_threat_metric.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("threat_table")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '6_threat_table.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("threat_bar")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '7_threat_bar.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("category_bar")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '8_category_bar.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("user_metric")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '9_user_metric.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("user_bar")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '10_user_bar.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("admin_bar")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '11_admin_bar.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("error_table")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '12_error_table.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("req_cat_table")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '13_req_cat_table.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("sys_access_bar")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '14_sys_access_bar.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    element = driver.find_element_by_id("priority_bar")
    screenshot_as_bytes = element.screenshot_as_png
    with open(os.path.join(img_path, '15_priority_bar.png'), 'wb') as f:
        f.write(screenshot_as_bytes)
    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
    test_fullpage_screenshot()
