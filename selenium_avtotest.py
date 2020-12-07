
from selenium import webdriver
def main ():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('https://www.expedia.com/')
    btn_flights = driver.find_element_by_xpath("//a[@aria-controls='wizard-flight-pwa']")
    btn_flights.click()
    btn_one_way = driver.find_element_by_xpath("//span[text()='One-way']")
    btn_one_way.click()
    make_text_leaving_from = driver.find_element_by_xpath("//button[@aria-label='Leaving from']")
    make_text_leaving_from.send_keys('Moscow')
    confirm_Moscow = driver.find_element_by_xpath("//button[@data-stid='location-field-leg1-origin-result-item-button']")
    confirm_Moscow.click()
    make_text_going_to = driver.find_element_by_xpath("//button[@aria-label='Going to']")
    make_text_going_to.send_keys("Dortmund")
    confirm_Dortmund = driver.find_element_by_xpath("//button[@data-stid='location-field-leg1-destination-result-item-button']")
    confirm_Dortmund.click()
    btn_Serch = driver.find_element_by_xpath("//button[@data-testid='submit-button']")
    btn_Serch.click()

if __name__ == '__main__':
    main()