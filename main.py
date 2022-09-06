from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from prompt_toolkit import print_formatted_text, HTML

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('log-level=3')

driver = webdriver.Chrome(chrome_options=options, service=ChromeService(executable_path=ChromeDriverManager().install()))

baseUrl = "https://r6.tracker.network/profile/pc"

def search_5(*usernames):
    global driver
    global options
    global baseUrl
    
    for u in usernames:
        
        appendedUrl = f'{baseUrl}/{u}'

        # Request the web page of that player
        driver.get('https://google.com')
        driver.get(appendedUrl)
        
        # Find current rank element by XPATH
        currentRank = driver.find_element(By.XPATH, '//*[@id="profile"]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]')
        
        # Print information to screen
        print_formatted_text(HTML(f'\n<b>[*] {u}</b>\nCurrent Rank: {currentRank.text}\n'))
        
    driver.quit()
    quit()


search_5('PsychoSmitty', 'jjheals1901', 'TheBobDuncan')