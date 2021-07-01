from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://happy-sea-0a5ffef03.azurestaticapps.net/masodik.html")
    add_new_todo_input = driver.find_element_by_xpath('//input[@placeholder="Add new todo"]')
    # add new todo
    add_new_todo_input.send_keys("0000 this is my new todo")
    add_new_todo_input.send_keys("\n")
    # delete a todo
    todo_element = driver.find_element_by_xpath('//i[@class="fa fa-trash"]').click()
except Exception as e:
    print('Exception occured: ', e)
finally:
    pass
    # driver.close()
