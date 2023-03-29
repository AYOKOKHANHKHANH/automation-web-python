from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOpt

def get_driver(browser):
    if browser == 'Chrome':
        driver = chrome_driver_init()
    if browser == 'Firefox':
        driver = firefox_driver_init()
    elif browser == 'Edge':
        driver = edge_driver_init()
    return driver
    
def chrome_driver_init():
    driver = webdriver.Chrome(executable_path='.\driver\ChromeDriver\chromedriver.exe') 
    
    driver.implicitly_wait(30)
    driver.maximize_window()
    print('Open Chrome browser')
    return driver

def firefox_driver_init():
    opt = firefoxOpt()
    opt.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path=".\driver\FirefoxDriver\geckodriver.exe", options=opt)
    driver.implicitly_wait(30)
    driver.maximize_window()
    print('Open Firefox browser')
    return driver

def edge_driver_init():
    driver = webdriver.Edge(executable_path='.\driver\EdgeDriver\msedgedriver.exe')
    
    driver.implicitly_wait(30)
    driver.maximize_window()
    print('Open Edge browser')
    return driver