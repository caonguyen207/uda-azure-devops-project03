# #!/usr/bin/env python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

print('Starting the browser...')
driver = webdriver.Chrome(ChromeDriverManager().install())
print('Browser started successfully. Navigating to the demo page to login.')


def login(user, password):
  driver.get('https://www.saucedemo.com/')
  driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
  driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
  driver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()
  if driver.current_url == 'https://www.saucedemo.com/inventory.html':
    print('Successfully logged in with user: ' + user)
    logo = driver.find_element(By.CSS_SELECTOR, ".header_label>.app_logo").text
    return "${logo}" == "Swag Labs"
  else:
    print ('Failed to logged in')
    return False

def add_item ():
  driver.get("https://www.saucedemo.com/inventory.html")
  driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
  no_of_items = driver.find_element(By.CSS_SELECTOR, "span.shopping_cart_badge").text
  return no_of_items == '1'

def remove_item ():
  driver.get("https://www.saucedemo.com/inventory.html")
  driver.find_element(By.ID,'remove-sauce-labs-backpack').click()
  items = driver.find_elements(By.CLASS_NAME, "cart_item")
  return len(items) == 0

def add_all_items():
  driver.get("https://www.saucedemo.com/inventory.html")
  items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
  for item in items:
    item.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
  no_of_items = driver.find_element(By.CSS_SELECTOR, "span.shopping_cart_badge").text
  assert no_of_items == '6'

def remove_all_items():
  driver.get("https://www.saucedemo.com/cart.html")
  items = driver.find_elements(By.CLASS_NAME, "cart_item")
  for item in items:
    item.find_element(By.CLASS_NAME, "cart_button").click()
  items = driver.find_elements(By.CLASS_NAME, "cart_item")
  return len(items) == 0

try:
  login('standard_user', 'secret_sauce')

  add_item()
  remove_item()
  add_all_items()
  remove_all_items()
except:
  # Close the driver
  driver.close()