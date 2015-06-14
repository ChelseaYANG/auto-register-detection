  #Author:yangyi
#date:2015-06-08
#!/usr/bin/python
# -*- coding: gbk -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time
import configure_data_paipaidai
#import selenium.chrome.ChromeDriver
#Create a new instance of the browser driver

driver = webdriver.Chrome()  ##IE(), FireFox()

# go to the google home page
driver.get("https://ac.ppdai.com/User/Register")
time.sleep(5)

#registerElement = driver.find_element_by_class_name("ui-nav-item reg-link")

#registerElement.click()



try:
    existed_counter = 1
    format_wrong_counter = 1
    sum = 1
    
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    for item in range(len(configure_data_paipaidai.USERNAME_DATA)):
        print "------------------" + "this is the " + str(sum) + " times request" + "--------------------"
        inputElement = driver.find_element_by_id("mobilephone")
        inputElement.clear()
        inputElement.send_keys(unicode(configure_data_paipaidai.USERNAME_DATA[item],"gbk"))
        time.sleep(2)
        inputElementSecond = driver.find_element_by_id("Password")
        inputElementSecond.clear()
        inputElementSecond.send_keys("QWE321_paipai")
        time.sleep(2)
        driver.refresh()
#backup
#    if driver.find_element_by_class_name("error").is_displayed() is True:
#        print "error, nickname is exist!"
#    elif driver.find_element_by_class_name("error valid").is_displayed() is True:
#        print "pass, nickname is usable!"
#    else:
#        print "error!"
        #print driver.find_element_by_class_name("ui-form-item").find_element_by_id("phone").text
        #print driver.find_element_by_css_selector("label[class=\"error\"]").text
        #print driver.find_element_by_xpath("//form[@id='reg']").text
        
        
        
        if u"手机号码已注册" in driver.find_element_by_xpath("//ul[@id='login_nav']").text:
            print "for tel number: " + configure_data_paipaidai.USERNAME_DATA[item] + "----tel is already exist!" + " registered tel sum is: " + str(existed_counter)
            existed_counter = existed_counter + 1
        elif u"请输入正确的手机号码" in driver.find_element_by_xpath("//ul[@id='login_nav']").text:
            print "for tel number: " + configure_data_paipaidai.USERNAME_DATA[item] + "----tel is usable!" + " format wrong tel sum is: " + str(format_wrong_counter)
            format_wrong_counter = format_wrong_counter + 1
        else:
            print "for tel number: " + configure_data_paipaidai.USERNAME_DATA[item] + "----fine."
        sum =sum + 1

#except:
#    print "nickname is not exist"
#else:
#    print "nickname is exist"
finally:
#   driver.quit()
    pass


#==================================
