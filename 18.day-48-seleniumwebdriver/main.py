from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\sviluppo\\chrome_driver\\v111\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.it/dp/B0BP7NX32J?pd_rd_i=B0BP7NX32J&pf_rd_p=e5ca4edb-7ec1-4087-b0ab-8e6fea189268&pf_rd_r=S2VVXHR78SDBY6KA9ES2&pd_rd_wg=hDvhc&pd_rd_w=G2eL1&pd_rd_r=88998eee-7608-41aa-88db-8686c08d5eb5")
price = driver.find_element(By.CSS_SELECTOR, "span.priceToPay > span.a-offscreen")

money_price = price.get_attribute("innerText")

print(f"Prezzo: {money_price}")

driver.get("https://python.org")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)

# driver.close()  # Close a single tab
driver.quit()   # Close all tabs
