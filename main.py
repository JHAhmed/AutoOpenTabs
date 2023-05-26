from selenium import webdriver
from time import sleep
import warnings

warnings.filterwarnings('ignore')

# --------------- INITIATE VARIABLES --------------- #
websitesList = ["https://www.reuters.com/", "https://www.cnbc.com/world/?region=world", "https://www.bloomberg.com/markets",
"https://www.ft.com/", "https://www.thestreet.com/", "https://www.marketwatch.com/", "https://finance.yahoo.com/",
"https://www.wsj.com/"]

# --------------- DEFINE FUNCTIONS --------------- #
def OpenWebsites (websitesList) :
    global driver
    driver.get("https://www.google.com")
    sleep(1.5)
    for i in range(len(websitesList)) :
        site = 'window.open("' + websitesList[i] + '")'
        driver.execute_script(site)
        sleep(0.5)
    sleep(0.5)
        
def LaunchChrome () :
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("user-data-dir=C:\\Users\\jamal\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path = "chromedriver.exe", options = options)
    sleep(1)
    OpenWebsites(websitesList)

# --------------- START PROGRAM --------------- #
LaunchChrome()