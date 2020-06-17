from selenium import webdriver
import sys

# custom config to make this work without error prompt
options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)

