#coding=gbk
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


#test_log = open("C:/Users/hyasn/Desktop/test_log.txt","a+")
browser = webdriver.Chrome("E:\SetupMenu\Anaconda\chromedriver.exe") # Get local session of Chrome
browser.get("http://19.16.104.13:8080/default/index/indexBlue/index.jsp#") # Load page
assert "�㶫ʡ������Դ������칫ϵͳ" in browser.title

username = "cxh"  #�û���
password = "000000"	#�û�����
input_username = browser.find_element_by_name("userId") # ͨ��ID��ȡ�û��������
input_username.send_keys(username)	#�����û���
input_password = browser.find_element_by_name("password")	#ͨ�����ƻ�ȡ���������
input_password.send_keys(password)	#��������

input_submit = browser.find_element_by_class_name("loginBtn")	#ͨ�����ƻ�ȡ��¼��ť
input_submit.click()	#������¼

#assert "ע��" in browser.find_element_by_class_name("login_out").title
#print(username+"��¼�ɹ�")
#test_log.write(username + "��¼�ɹ�\n")

# ������Ĺ���
gwbl = browser.find_element_by_class_name("g-pt-gwbl")
gwbl.click()

# ���������										
fqgw = browser.find_element_by_class_name("g-pt-fqgw")
fqgw.click()

# ������İ���
lwbl = browser.find_element_by_class_name("g-pt-lwbl")
lwbl.click()

#�л���ǩҳ
# browser.switch_to.window("���İ���")
for handle in browser.window_handles:
   browser.switch_to.window(handle)
   #print(browser.title)

inputBt = browser.find_element_by_name("lwdj.bt")
inputBt.send_keys("���ı���")  
time.sleep(10) 
# �ϴ�����
uploadFile = browser.find_element_by_class_name("diyBtnAdd")
uploadFile.click()
time.sleep(10)
# ѡ���ļ�
pickfile = browser.find_element_by_id("picker")
pickfile.click()

#time.sleep(0.2) # Let the page load, will be added to the API
#�ǳ�
#browser.get("http://172.16.101.18:8080/default/coframe/auth/login/login.jsp")	#�ǳ�
#print(username+"�ǳ�")
#test_log.write(username + "�ǳ�\n")

#test_log.close()
#try:
#    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
#except NoSuchElementException:
#    assert 0, "can't find seleniumhq"
#browser.close()