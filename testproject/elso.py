from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://happy-sea-0a5ffef03.azurestaticapps.net/elso.html")

    height_input = driver.find_element_by_id("height")
    weight_input = driver.find_element_by_id("weight")
    submit_button = driver.find_element_by_xpath('//input[@value="computeBMI"]')

    # scenario 1 171 cm 45 kg === "Underweight"
    height_input.send_keys("171")
    weight_input.send_keys("45")
    submit_button.click()
    comment_text = driver.find_element_by_id("comment").text
    assert comment_text == "Underweight"

    # need to clear input fields before typing new data
    height_input.clear()
    weight_input.clear()

    # scenario 2 185 cm 65 kg === "Normal"
    height_input.send_keys("185")
    weight_input.send_keys("65")
    submit_button.click()
    comment_text = driver.find_element_by_id("comment").text
    assert comment_text == "Normal"

except Exception as e:
    print('Exception occured: ', e)
finally:
    driver.close()
