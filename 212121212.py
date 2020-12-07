#from selenium import webdriver

#browser = webdriver.Сhrome ("D:\pythonProject\chromedriver.exe")
#browser.implicitly_wait(60)
#browser.get("https://google.com")

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
    confirm_Moscow = driver.find_element_by_xpath()
    confirm_Moscow.click("//button[@data-stid='location-field-leg1-origin-result-item-button'] [1]")
    #make_text = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div[1]/div/form/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[1]/section/div/input')
    #make_text .send_keys('Moscow')


if __name__ == '__main__':
    main()