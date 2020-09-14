import time
from selenium import webdriver
import getpass
import pysnow

instance = input("Enter instance: ")
name = input("Enter username: ")
pwd = getpass.getpass(prompt="Enter password: ")
sd = input("Enter short description: ")

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "C:\Program Files\Google\ChromeDriver\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_binary,options=options)

url = "https://{0}.service-now.com".format(instance)
driver.get(url)
time.sleep(5)
driver.switch_to.frame("gsft_main")
username = driver.find_element_by_id("user_name")
password = driver.find_element_by_id("user_password")
username.send_keys(name)
time.sleep(1)
password.send_keys(pwd)
time.sleep(1)
driver.find_element_by_id("sysverb_login").click()

time.sleep(5)
driver.find_element_by_xpath(r'/html/body/div[5]/div/div/nav/div/div[3]/div/div/concourse-application-tree/ul/li[1]/ul/li[9]/div/div/a/div/div').click()
time.sleep(5)
driver.switch_to.frame("gsft_main")
driver.find_element_by_xpath(r'/html/body/div[1]/div[1]/span/div/div[1]/div/div[1]/button[2]').click()

time.sleep(2)
short_description = driver.find_element_by_id("incident.short_description")
short_description.send_keys(sd)
time.sleep(2)
driver.find_element_by_id("sysverb_insert").click()

p = pysnow.Client(instance=instance, user=name, password=pwd)

incident = p.resource(api_path='/table/incident')
query = pysnow.QueryBuilder()
query = query.field('opened_at').order_descending()

response = incident.get(query=query,stream=True)

resp = response.first()
incident_no = resp["number"]
impact = resp["impact"]
priority = resp["priority"]
short_description = resp["short_description"]
opened_at = resp["opened_at"]

print("New Incident raised -\nnumber:{0}\nimpact:{1}\npriority:{2}\nshort_description:{3}\nopened_at:{4}".format(incident_no, impact, priority, short_description, opened_at))
