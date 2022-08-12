from selenium import webdriver
import pyautogui
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(options=options)

def test_login():
    driver.get("https://stg-oauth.privy.id/login?client_id=v5SCIvXPW1ZO7LLj_Fu2Vj-RIkKUBjR_qkvNymBg4Co&redirect_uri=http%3A%2F%2Flocalhost%2Fauth%2Fcallback&response_type=code&state=eyJyZWRpcmVjdFVybCI6Ii9sb2dpbi92ZW5kcG9pbnQifQ%3D%3D&scope=public")
    driver.find_element_by_name("user[privyId]").send_keys("HJF9731")
    time.sleep(1)
    driver.find_element_by_css_selector("button.btn-alt").click()
    driver.find_element_by_css_selector("button.btn-alt").click()
    time.sleep(1)
    driver.find_element_by_name("user[secret]").send_keys("aha84c4")
    time.sleep(1)
    driver.find_element_by_css_selector("button.btn-alt").click()
    driver.find_element_by_css_selector("button.btn-alt").click()
    time.sleep(3)

def test_actor():
    driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[2]/div/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/input').send_keys("Subscriber Example")
    time.sleep(1)
    driver.find_element_by_css_selector(".v-treeview-node.v-treeview-node--leaf.v-treeview-node--click").click()
    time.sleep(4)

def test_analytics():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]').click()
    time.sleep(3)

def test_uploaddoc():
    driver.find_element_by_link_text("Upload Doc").click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/span/div/div[1]/div/form/div/div[2]/div/div/span/div/div/div[1]/div/input').send_keys("tes")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/main/div/div[2]/div[1]/span/div/div[1]/div/form/div/div[6]/div/div/button/div[1]/div/div/div[2]/button/span').click()
    time.sleep(2)
    pyautogui.write("tes.pdf")
    pyautogui.press("enter") 
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/span/div/div[1]/div/form/div/div[6]/div/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div/div/div/div[1]/div/div[1]').click()
    time.sleep(2)          
    #click document categories
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[1]/div/form/div/div[6]/div/div/div/div/div[3]/div[1]/div/span/div/div/div[1]/div[1]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_id("documents[0].category1").click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[1]/div/form/div/div[6]/div/div/div/div/div[3]/div[2]/div/span/div/div/div[1]/div[1]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_id("documents[0].sub_category1").click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[1]/div/form/div/div[6]/div/div/div/div/div[3]/div[3]/div/div/span/div/div/div/div/input').send_keys("tes")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[1]/div/form/div/div[6]/div/div/div/div/div[3]/div[5]/div/div/span/div/div/div/div/textarea').send_keys("tes")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/span/div/div[3]/button[2]/span').click()
    time.sleep(2)
    driver.find_element_by_id("user_name").send_keys("Hendrikus juan")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/div/div').click()
    time.sleep(2)
    #button 2
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[2]/div[2]/button[2]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[3]/div/table/tbody/tr/td[5]/div/div/div/div/div').click()
    time.sleep(2)
    #button 3
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div[2]/div[2]/button[2]/span').click()
    time.sleep(2)
    driver.find_element_by_css_selector("[test-id='btn:upload-doc/step4/signer/SUBSCRIBER/HJF9731']").click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div/div[2]/div/div/div[3]/div[2]/div/button[1]/span/i').click()
    time.sleep(2)                 
    driver.find_element_by_css_selector("[test-id='btn:next-or-sumbit']").click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[3]/button[2]/span').click()
    time.sleep(23)

def test_waitingsigner():
    driver.find_element_by_link_text("Waiting Signer").click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div[1]/input').send_keys("tes")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/input').send_keys("Category 1")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/div/div/span').click()
    time.sleep(1)                  
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/input').send_keys("Sub Category 1 1")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div/div/span').click()
    time.sleep(1)                 
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/input[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/input[1]').send_keys("YES")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div/div/div/span').click()
    time.sleep(1)
    driver.find_element_by_css_selector('i.v-icon.notranslate.mdi.mdi-dots-horizontal.theme--light').click()
    time.sleep(1)
    driver.find_element_by_css_selector("[test-id='btn:waiting-signer/list/0/action/details']").click()
    time.sleep(8)

def test_approve():
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/nav/div[1]/div[2]/div[1]/div[2]/a[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/input').send_keys("tes")
    time.sleep(1)                 
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/input').send_keys("Category 1")
    time.sleep(1)        
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/div/div/span').click()
    time.sleep(1)      
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/input').send_keys("Sub Category 1 1")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div/div/span').click()
    time.sleep(1)   
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/input[1]').send_keys("YES")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div/div/div/span').click()
    time.sleep(1)                       
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div[3]').click()
    time.sleep(1)

def test_reject():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/nav/div[1]/div[2]/div[1]/div[2]/a[2]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/input').send_keys("tes")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/input').send_keys("Category 1")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/div/div/span').click()
    time.sleep(1)  
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/input').send_keys("Sub Category 1 1")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div/div/span').click()
    time.sleep(1) 
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/input[1]').send_keys("YES")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div/div/div/span').click()
    time.sleep(1)     
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div[3]').click()
    time.sleep(1)

def test_drop():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/nav/div[1]/div[2]/div[1]/div[2]/a[3]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/input').send_keys("tes")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/input').send_keys("Category 1")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div/div/div/span').click()
    time.sleep(1)  
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/input').send_keys("Sub Category 1 1")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div/div/span').click()
    time.sleep(1) 
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/input[1]').send_keys("YES")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div/div/div/span').click()
    time.sleep(1)    
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div[3]').click()
    time.sleep(1)

def test_Settings():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/nav/div[1]/div[2]/div[3]/div[1]/div[2]/div').click()
    time.sleep(1)

def test_Subscriberuser():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/nav/div[1]/div[2]/div[3]/div[2]/a[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div[1]/div/div[2]/div/div[3]').click()
    time.sleep(1)

def test_product():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/nav/div[1]/div[2]/div[3]/div[2]/a[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[1]/div/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[1]/div/div/div/span/div/div/div[1]/div/input').send_keys("tes 95")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[2]/div[2]/div[1]/div/span/div/div/div[1]/div/input').send_keys("HJF9731")
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[3]/div/div/span/div/div/div/div[1]/div[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="dashboard-app"]/div[3]/div/div/div[2]/div/form/div[4]/div/button[2]/span').click()
    time.sleep(5)       
    driver.find_element_by_xpath("(//button[@id='btn:base-dialog/close']/span/i)[2]").click()
    time.sleep(2)                   
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[3]/div/div[1]/div/div/div/div[1]/input').send_keys("tes 95")
    time.sleep(1)          
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[3]/div/div[3]/div/div/div[1]/div[1]/div[1]').click()
    time.sleep(1)         
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[5]/div/div[3]/div/div').click()
    time.sleep(2)                 

def test_seelistproject():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[5]/div/button[2]/span').click()
    time.sleep(1)                              
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[1]/div/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[2]/div/span/div/div/span/div/div/div[1]/div/input').send_keys("tes 95")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[3]/div[2]/div[1]/div/span/div/div/div[1]/div/input').send_keys("HJF9731")
    time.sleep(4)                 
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[5]/div/button[2]/span').click()
    time.sleep(5)
    driver.find_element_by_xpath("(//button[@id='btn:base-dialog/close']/span/i)[2]").click()
    time.sleep(2) 

def test_user():
    driver.find_element_by_link_text("User").click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/div[2]/button/span').click()
    time.sleep(3)                        
    driver.find_element_by_xpath("//div[@id='dashboard-app']/div[3]/div/div/div[2]/div/form/div[2]/div/div/span/div/div/div/div/input").send_keys("DYD7573")
    time.sleep(3)                 
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[4]/div/span/div/div/div/div/input').send_keys("tes")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[6]/div/span/div/div/div/div/input').send_keys("tes")
    time.sleep(1)             
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[7]/div[2]/span/div/div/div/div[1]/div[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div[2]/div/form/div[12]/div/button[2]').click()
    time.sleep(5)
    driver.find_element_by_css_selector("i.v-icon.notranslate.mdi.mdi-close.theme--light").click()
    time.sleep(1)                 
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[1]/input').send_keys("Dendy")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/table/tbody/tr/td[11]/button/span/i').click()
    time.sleep(3)              
    driver.find_element_by_css_selector("[test-id='btn:settings/user/add-user/list/0/action/delete']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[2]/div[2]/button/span").click()
    time.sleep(5)                 
    driver.find_element_by_css_selector("i.v-icon.notranslate.mdi.mdi-close.theme--light").click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/div[3]').click()
    time.sleep(1)
    driver.find_element_by_css_selector("[test-id='btn:settings/user/change-representative/change-representative']").click()
    time.sleep(1)
    driver.find_element_by_css_selector("[test-id='input:settings/user/change-request-dialog/privyid']").send_keys("DYD7573")
    time.sleep(4)
    driver.find_element_by_css_selector("[test-id='btn:settings/user/change-request-dialog/save']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("i.v-icon.notranslate.mdi.mdi-close.theme--light").click()
    time.sleep(1)

def test_inviteuser():
    driver.find_element_by_link_text("Invite User").click()
    time.sleep(2)
    driver.find_element_by_css_selector("[test-id='input:filter/invite-user/name']").send_keys("Dendy")
    time.sleep(1)                       

def test_activitylog():
    driver.find_element_by_link_text("Activity Log").click()
    time.sleep(2)
    driver.find_element_by_css_selector("[test-id='input:filter/activity-log/name']").send_keys("Get List User Subscriber")
    time.sleep(1)

def test_invoice():
    driver.find_element_by_css_selector("[test-id='nav:/dashboard/invoice']").click()
    time.sleep(3)

def test_notification():
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/header/div/button/span/div/span/i').click()
    time.sleep(1)
    #driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/div[1]/button/span').click()
    #time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/footer/button/span').click()
    time.sleep(1)

def test_subscriberdata():
    driver.find_element_by_xpath("//div[@id='dashboard-app']/div/header/div/div[5]/div/div[2]/div[2]").click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div[1]/div[2]').click()
    time.sleep(3)
    driver.find_element_by_css_selector('i.v-icon.notranslate.bg-secondary--icon.mdi.mdi-download.theme--light').click()
    time.sleep(2)