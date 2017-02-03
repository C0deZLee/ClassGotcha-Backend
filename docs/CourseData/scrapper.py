import re
import sys
import json
import os
import time
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
chromedriver = '/Users/Simo/Desktop/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
url = "http://www.work.psu.edu/ldap/"
professors = set(['simo wu'])
email_set = set(['szw184@psu.edu'])
#email_map  ={}
driver = webdriver.Chrome(chromedriver)

time.sleep(3)
with open('/Users/Simo/Documents/ClassGotcha/classgotcha/docs/CourseData/courses_data.json') as upload:
    for course in upload:
        cours = json.loads(course)
        if cours['instructor1'] != 'Staff':
            # if the professor is not in our set yet
            if cours['instructor1'] not in professors:
                professor = cours['instructor1']

                professor = re.sub('\,$','',professor)

                professors.add(professor)
                driver.get(url)
                name = driver.find_element_by_name('cn')
                name.send_keys(professor)
                full_listing = driver.find_element_by_id("full")
                full_listing.click()
                login_attempt = driver.find_element_by_name("submit")
                login_attempt.click()
                
                forms = driver.find_elements_by_xpath("html/body/div/form")
                for i in range(1,len(forms)):
                    if driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr[11]/td") !="Staff":
                        professor_email = "http://www.work.psu.edu/ldap/"
                        try:
                            # hard coded
                            while professor_email=="http://www.work.psu.edu/ldap/": 
                                email = driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr/td/a")
                                # strip the email
                                time.sleep(0.1)
                            
                                professor_email = email[0].get_attribute("href")[7:]
                            # construct the map
                            if i>1:
                                
                                for temp in range(1,14):
                                        column_name = driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/th")[0].get_attribute("innerText")
                                        if column_name =="Address:":
                                            email_map[professor+str(i)] = (professor_email,driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/td")[0].get_attribute("innerText"))
                                        else:
                                            pass
                            
                            else:
                                for temp in range(1,14):
                                        column_name = driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/th")[0].get_attribute("innerText")
                                        if column_name =="Address:":
                                            email_map[professor] = (professor_email,driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/td")[0].get_attribute("innerText"))
                                        else:
                                            pass
                            # put into email set
                            email_set.add(professor_email)
                        except:
                            pass
                    else:
                        pass
            
            else:
                
                pass
                
        try: 
            if cours['instructor2'] != 'Staff':
                if cours['instructor2'] not in professors:
                    professor = cours['instructor2']

                    professor = re.sub('\,$','',professor)
                    professors.add(professor)
                    driver.get(url)
                    name = driver.find_element_by_name('cn')
                    name.send_keys(professor)
                    full_listing = driver.find_element_by_id("full")
                    full_listing.click()
                    login_attempt = driver.find_element_by_name("submit")
                    login_attempt.click()
                    
                    forms = driver.find_elements_by_xpath("html/body/div/form")
                    for i in range(1,len(forms)):
                        if driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr[11]/td") !="Staff":
                            professor_email = "http://www.work.psu.edu/ldap/"
                            try:
                                # hard coded
                                while professor_email=="http://www.work.psu.edu/ldap/": 
                                    email = driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr/td/a")
                                    # strip the email
                                    time.sleep(0.1)
                            
                                    professor_email = email[0].get_attribute("href")[7:]
                                if i>1:
                                
                                    for temp in range(1,14):
                                        column_name = driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/th")[0].get_attribute("innerText")
                                        if column_name =="Address:":
                                            email_map[professor+str(i)] = (professor_email,driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/td")[0].get_attribute("innerText"))
                                        else:
                                            pass
                            
                                else:
                                    for temp in range(1,14):
                                        column_name = driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/th")[0].get_attribute("innerText")
                                        if column_name =="Address:":
                                            email_map[professor] = (professor_email,driver.find_elements_by_xpath("html/body/div/form["+str(i)+"]/table/tbody/tr["+str(temp)+"]/td")[0].get_attribute("innerText"))
                                        else:
                                            pass
                                # put into email set
                                email_set.add(professor_email)
                            except:
                                pass
                        else:
                            pass
                    
                    
                    
                    
        except:
            pass


