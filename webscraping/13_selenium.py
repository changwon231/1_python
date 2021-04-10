from selenium import webdriver
import time
# 로그인 

browser = webdriver.Chrome()

# 네이버 이동
browser.get("http://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("tlsckdnjs")
browser.find_element_by_id("pw").send_keys("400wks")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 딜레이
time.sleep(1)
# 4-1 기존 아이디 지우기
browser.find_element_by_id("id").clear()

# 5. id 새로 입력
browser.find_element_by_id("id").send_keys("new_ID")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit()


