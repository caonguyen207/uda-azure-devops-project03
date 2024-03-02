# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

print ('Starting the browser...')
# --uncomment when running in Azure DevOps.
options = ChromeOptions()
options.add_argument("--headless") 
driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
print ('Browser started successfully. Navigating to the demo page to login.')

def login (user, password):
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_css_selector("input[id='login-button']").click()
    if driver.current_url == 'https://www.saucedemo.com/inventory.html':
        print ('Successfully logged in')
        driver.findElements(By.class("app_logo")).getText() = 'Swag Labs'
		return True
	else:
        print ('Failed to logged in')
		return False

def add_item ():
    driver.get("https://www.saucedemo.com/inventory.html")
	driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
	no_of_items = driver.find_element_by_class_name("shopping_cart_badge").text
	return no_of_items == '1'

def add_all_items():
	driver.get("https://www.saucedemo.com/inventory.html")
    items = driver.find_element_by_class_name('inventory_item')
	for item in items:
		item.find_element_by_class_name("btn_inventory").click()
	no_of_items = driver.find_element_by_class_name("shopping_cart_badge").text
    assert no_of_items == '6'

def remove_all_items():
	driver.get("https://www.saucedemo.com/cart.html")
	items = driver.find_element_by_class_name("cart_item")
	for item in items:
		item.find_element_by_class_name("cart_button").click()
	assert !driver.find_element_by_class_name("shopping_cart_badge")

login('standard_user', 'secret_sauce')

add_item()
add_all_items()
remove_all_items()