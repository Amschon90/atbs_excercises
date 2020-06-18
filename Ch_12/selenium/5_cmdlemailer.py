from selenium import webdriver
import sys, time, os

# Secrets, shhhhh
gmailUser = os.environ.get('GMAIL_USER')
gmailPass = os.environ.get('GMAIL_PASS')

def sendEmail(recipient, subject, body):
    # Start browser
    driver = webdriver.Firefox()

    # Open Stack Overflow so I can authenticate.. Necessary due to Gmail detecting Selenium client.
    driver.get('https://stackoverflow.com/users/login')

    # Click the button for gmail
    driver.find_element_by_css_selector('button.s-btn__icon:nth-child(1)').click()
    try:
        # Authenticate
        driver.find_element_by_id('identifierId').send_keys(gmailUser)
        driver.find_element_by_id('identifierNext').click()
        time.sleep(1)
        driver.find_element_by_name("password").send_keys(gmailPass)
        driver.find_element_by_id('passwordNext').click()
        time.sleep(1)

        # Navigate to Gmail
        driver.get('https://gmail.com')
        time.sleep(1)

        # Open the email window and fill out email fields
        driver.find_element_by_xpath("//div[contains(text(),'Compose')]").click()
        time.sleep(1)
        driver.find_element_by_name('to').send_keys(recipient)
        driver.find_element_by_name('subjectbox').send_keys(subject)

        # Send email
        driver.find_element_by_id(':av').send_keys(body)
        driver.find_element_by_id(':9g').click()
        time.sleep(3)
        print("Email sent successfully.")

    except:
        print("There was a failure.")

    # Close browser window.
    driver.quit()

if len(sys.argv) != 4:
    print('Invalid # of arguments!')
else:
    sendEmail(sys.argv[1],sys.argv[2],sys.argv[3])