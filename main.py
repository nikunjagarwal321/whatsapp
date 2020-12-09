from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys 
import time 
  

driver = webdriver.Chrome('./chromedriver') 
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  

friend = "Lonely"
  
# Message to be sent
string = "Message sent using Python!!!"
time.sleep(10)
person = driver.find_element_by_xpath('//span[@title="{}"]'.format(friend))
# person.click()

unread_elements = driver.find_elements_by_class_name("_31gEB")
# print("Unread = " + (str)(unread_elements))

for unread_element in unread_elements: 
    print("Hiiiiiiiiiiiiiiiiiiiii")
    msg = " "
    parent = unread_element.find_element_by_xpath('../../../../..') #_2kHpK
    name_time_parent = parent.find_element_by_class_name("_3dtfX")
    msg_parent = parent.find_element_by_class_name("_2iq-U")
    # print("parent = "+ (str)(parent))
    print("msg_parent" + msg_parent.text)
    name_element = name_time_parent.find_element_by_class_name("_3CneP")
    time_element = name_time_parent.find_element_by_class_name("m61XR")
    name_of_person = name_element.text
    time = time_element.text
    
    msg = msg_parent.find_element_by_xpath('//span[@class="_3ko75 _5h6Y_ _3Whw5"]')
    print(name_of_person + ", " + time + ", " + (str)(msg))

# class for unread = _31gEB
# last message = class = _2iq-U
