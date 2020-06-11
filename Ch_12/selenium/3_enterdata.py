from selenium import webdriver

# custom config to make this work without error prompt
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)

# starts the browser with my options above
driver = webdriver.Chrome(options=options)

# confirm driver type
print(type(driver))

# navigate to a site
driver.get('https://login.metafilter.com')

# enter user/pass and submit
userElem = driver.find_element_by_id('user_name')
userElem.send_keys('lebronfan23')
passwordElem = driver.find_element_by_id('user_pass')
passwordElem.send_keys('12345678')
passwordElem.submit()