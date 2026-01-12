from selenium import webdriver

def before_all(context):
    context.base_url = "http://13.229.208.136:5173"
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

# def before_scenario(context, scenario):
#     context.driver.delete_all_cookies()

def after_all(context):
    context.driver.quit()