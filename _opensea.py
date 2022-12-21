from selenium import webdriver
from selenium.webdriver.common.by import By

def refresh_metadata(contract, from_id, to_id):

    # setup
    driver = webdriver.Chrome()
    url = "https://opensea.io/assets/optimism/{}/{}"

    for id in range(from_id, to_id+1):

        # browse item
        driver.get(url.format(contract, id))

        # click more
        element = driver.find_element(By.CSS_SELECTOR, '.item--collection-toolbar-wrapper button:nth-child(3)')
        element.click()

        # click refresh metadata
        element = driver.find_element(By.CSS_SELECTOR, '.tippy-content button')
        element.click()
