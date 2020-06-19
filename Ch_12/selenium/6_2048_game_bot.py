# Plays the game @ https://gabrielecirulli.github.io/2048/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def status_ck(driver):
    try:
        driver.find_element_by_class_name('game-over')
        return True
    except:
        pass

k = [Keys.ARROW_UP,Keys.ARROW_RIGHT,Keys.ARROW_DOWN,Keys.ARROW_LEFT]

driver = webdriver.Firefox()
driver.get('https://gabrielecirulli.github.io/2048/')
game = driver.find_element_by_tag_name('html')

while not status_ck(driver):
    for i in range(4):
        game.send_keys(k[i])

driver.quit()
print("Game over!")