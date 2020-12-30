from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager())
driver = webdriver.Firefox()
driver.get("file:///C:/Users/Daniel_Lepszy/Tools/PythonLearningProject/PythonLearnCode/automation_testing/tasks/CH02/html_code_02.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()
