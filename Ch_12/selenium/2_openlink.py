from selenium import webdriver

# custom config to make this work without error prompt
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)

# starts the browser with my options above
driver = webdriver.Chrome(options=options)

# confirm driver type
print(type(driver))

# navigate to a site
driver.get('https://inventwithpython.com')

# open link on page
linkElem = driver.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click()