import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("./chromedriver.exe")
#enter the url in chrome
enter_url= driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print("Title is "+driver.title)


#Maximize the window
driver.maximize_window()
driver.implicitly_wait(5)


#select radio button 2 and assert
radio_button1= driver.find_element_by_css_selector("input[value='radio2']")
if radio_button1.is_selected():
    print("Radio button 2 is already selected")
else:
    radio_button1.click()


#Select Indonesia from suggestion dropdown and assert
text_field= driver.find_element_by_id("autocomplete").send_keys("Ind")
list_of_countries = driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li")
for options in list_of_countries:
    if options.text== 'Indonesia':
        options.click()


#Select option 2 from static option dropdown and assert
dropdown_list1 = Select(driver.find_element_by_id('dropdown-class-example'))
dropdown_list1.select_by_visible_text('Option2')


#Select check box 1,3 and assert
checkbox1= driver.find_element_by_id("checkBoxOption1")
checkbox1.click()
checkbox2= driver.find_element_by_id("checkBoxOption3")
checkbox2.click()
time.sleep(3)


#Enter your name in text box(under Switch To Alert Example)
name1= "Abhi"
name2= "Anju"
name_textfield= driver.find_element_by_id("name")
name_textfield.send_keys(name1)


#Click alert button and assert alert message should have your name in alert message.Then accept alert box.
driver.find_element_by_id("alertbtn").click()
time.sleep(3)
driver.implicitly_wait(2)
alert_obj= driver.switch_to.alert
alert_text= alert_obj.text
print("Alert message is: "+alert_text)
if alert_text.__contains__(name1):
    print(name1+" is present")
else:
    print(name1+" is not present")
alert_obj.accept()
driver.implicitly_wait(2)


#Enter your name in text box(under Switch To Alert Example)
#Click confirm button and assert alert message should have your name in alert message.
# Then cancel alert box.
name_textfield.send_keys(name2)
driver.find_element_by_id("confirmbtn").click()
alert_obj2= driver.switch_to.alert
alert_text2= alert_obj2.text
print("Second Alert message is: "+alert_text2)
if alert_text2.__contains__(name2)        :
    print(name2+" is present")
else:
    print(name2+" is not present")
alert_obj2.dismiss()


#Click on open window button, and switch to new window (child window) and assert title.
# Then switch back to original window.
original_window_title= driver.title
print("Title of Original window: "+original_window_title)

driver.find_element_by_id("openwindow").click()
driver.switch_to.window(driver.window_handles[1])
new_window_title= driver.title
print("Title of New window: "+new_window_title)
if original_window_title== new_window_title:
    print("Control is still in old window, please switch to new window")
    driver.switch_to.window(driver.window_handles[1])
    print("Title of New window is: "+driver.title)
else:
    print("Control is in new window. Now you can switch back to original window")
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)


#Click on open tab button, and switch to new tab(child window) and assert title. Then switch back to original window.
driver.find_element_by_id("opentab").click()
driver.switch_to.window(driver.window_handles[1])
new_tab_title= driver.title
print("Title of New Tab: "+new_tab_title)
if original_window_title== new_tab_title:
    print("Control is still in old tab itself, please switch to new tab")
    driver.switch_to.window(driver.window_handles[1])
    print("Title of New window is: "+driver.title)
else:
    print("Control is in new tab. Now you can switch back to original tab")
driver.close()
driver.switch_to.window(driver.window_handles[0])


#Interrogate the web table and get the rows which has 'selenium' in it. Get the count of courses having ‘selenium’ as substring.
table_path=driver.find_elements_by_xpath(("//table[@id='product']/tbody/tr"))
print(type(table_path))
rows = []
for i in table_path:
    textRow = i.text;
    if "Selenium" in textRow:
        rows.append(textRow)
print(rows)
print("{}{}".format("Count of courses having selenium in it is: ",sum('Selenium' in s for s in rows)))



#Enter your name in text box under 'Element Displayed Example'.
#Click Hide button and assert the text box is not shown
name3= "Abhinsree"
text_box= driver.find_element_by_id("displayed-text")

if text_box.is_displayed():
    print("Text box is displayed")
    text_box.send_keys(name3)
    driver.find_element_by_id("hide-textbox").click()
else:
    print("Text box is not displayed")


#Click Show button and assert the text box is shown and assert text value with value that we entered.
driver.find_element_by_id("show-textbox").click()
if text_box.is_displayed():
    print("Text box is displayed")
    print(text_box.get_attribute('value'))
else:
    print("Text box is hidden")


#Mouse hover the 'Mouse hover' button get the all the options and log in console.
mouse_hover= driver.find_element_by_id("mousehover")
ActionChains(driver).move_to_element(mouse_hover).perform()
get_list= driver.find_elements_by_xpath("/html/body/div[4]/div/fieldset/div/div/a")
for i in get_list:
    mouse_hover_list= i.text
    print(mouse_hover_list)


#Get the total count of iframe/frame/frameset present in current page.
seq= driver.find_elements_by_tag_name("iframe")
print("No of frames present in the web page are: ",+len(seq))


#Switch to first iframe and get all list of urls in iframe and switch back to main window.
list_of_links= list()
driver.switch_to.frame(0)
links= driver.find_elements_by_tag_name("a")
for i in links:
    url=i.get_attribute('a')
    list_of_links.append(url)
print(list_of_links)
driver.switch_to.default_content()


#Close the main windows and all child windows
driver.quit()





