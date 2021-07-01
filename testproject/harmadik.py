from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://happy-sea-0a5ffef03.azurestaticapps.net/harmadik.html")
    banner_message_div = driver.find_element_by_id("banner-message")
    # the blue button on white background is the default css style with no additional class attribute filled
    assert banner_message_div.get_attribute("class") is ''
    button = driver.find_element_by_xpath("//button")
    button.click()
    banner_message_div = driver.find_element_by_id("banner-message")
    # the white button on blue background is the alt css style, thus the class attribute should be 'alt'
    assert banner_message_div.get_attribute("class") == "alt"
except Exception as e:
    print('Exception occured: ', e)
finally:
    driver.close()
