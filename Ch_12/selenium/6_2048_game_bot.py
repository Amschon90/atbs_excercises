# Python script that plays the game @ https://gabrielecirulli.github.io/2048/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def status_ck(driver):
    # Checks to see if the game over message is displayed, and if not continues playing
    try:
        driver.find_element_by_class_name('game-over')
        return True
    except:
        pass

# Different keystroke values..
k = [Keys.ARROW_UP,Keys.ARROW_RIGHT,Keys.ARROW_DOWN,Keys.ARROW_LEFT]

# Setting up browser window..
driver = webdriver.Firefox()
driver.get('https://gabrielecirulli.github.io/2048/')
game = driver.find_element_by_tag_name('html')

# While the "Game over" message isn't present, loop through same 4 key strokes in the same order.
while not status_ck(driver):
    for i in range(4):
        game.send_keys(k[i])

# Print game over.
print("Game over!")