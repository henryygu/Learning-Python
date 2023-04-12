from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new Chrome browser instance
browser = webdriver.Chrome()

# Navigate to the webpage
browser.get(
    "http://irntfs2013:8080/tfs/Monitor/Portfolio/_apps/hub/ms.vss-releaseManagement-web.hub-explorer?releaseId=12987&_a=releases&definitionId=0o"
)

wait = WebDriverWait(browser, 10)
top_entry = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="row_123_0"]')))

top_entry = browser.find_element("xpath", '//*[@id="row_123_0"]')

actions = ActionChains(browser)
actions.double_click(top_entry).perform()

logs_entry = browser.find_element(
    "xpath", '//*[@id="release-editor"]/div[1]/div[1]/ul/li[9]'
)
logs_entry.click()

UAT_deploy = browser.find_element("xpath", '//*[@id="row_79_2"]/div[2]')
UAT_deploy.click()
