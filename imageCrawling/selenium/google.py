from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q") #위에서 찾은 구글 주소에 개발자 도구란에 요소 q로 찾음.#
elem.send_keys("테니스")  # 키보드 입력값 전송#
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[1].click()
driver.find_elements_by_css_selector(".n3VNCb.KAlRDb")

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
