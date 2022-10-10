from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
ab=input('Input Your ID\n')
cd=input('Input your PW\n')

cno=input("갤러리 cno를 입력해주세요\n")
postcoment=int(input("게시글을 지우려면 1, 댓글을 지우려면 2를 입력해주세요\n"))
waittime=int(input("대기시간 입력, 7~10초 권장\n"))
repeatNum=int(input("지울 횟수 입력\n"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(time_to_wait=1000)

driver.get('https://www.dcinside.com/')
driver.find_element("xpath",'//*[@id="user_id"]').send_keys(ab)
driver.find_element("xpath",'//*[@id="pw"]').send_keys(cd)
driver.find_element("xpath",'//*[@id="login_ok"]').click()

if postcoment == 1:
	driver.get('https://gallog.dcinside.com/'+ab+'/posting/index?cno='+cno)
	for i in range(repeatNum):
		driver.find_element("xpath",'//*[@id="container"]/article/div/div[3]/section/div[1]/div/ul/li[1]/div/div/button').click()
		driver.switch_to.alert.accept()
		time.sleep(waittime)
if postcoment == 2:
	for i in range(repeatNum):
		driver.get('https://gallog.dcinside.com/'+ab+'/comment/index?cno='+cno)
		driver.find_element("xpath", '//*[@id="container"]/article/div/div[3]/section/div[1]/div/ul/li[1]/div/div/button').click()
		driver.switch_to.alert.accept()
		time.sleep(waittime)	
