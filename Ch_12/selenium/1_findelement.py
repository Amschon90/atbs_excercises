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

try:
    elem = driver.find_element_by_class_name('cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')