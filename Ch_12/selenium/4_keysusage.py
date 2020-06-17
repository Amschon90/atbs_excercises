from selenium import webdriver
# import as Keys to save time
from selenium.webdriver.common.keys import Keys

# custom config to make this work without error prompt
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)

# starts the browser with my options above
driver = webdriver.Chrome(options=options)

# confirm driver type
print(type(driver))

# navigate to a site
driver.get('https://nostarch.com')

# enter user/pass and submit
htmlElem = driver.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
htmlElem.send_keys(Keys.HOME)    # scrolls to top