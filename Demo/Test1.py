'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options,
executable_path="../drivers/chromedriver 2")
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
#driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
#driver.quit()
#print("Completed")
 '''

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver 2")

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Hello world")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').click()

print(driver.title)

driver.close()
driver.quit()
print("completed")




