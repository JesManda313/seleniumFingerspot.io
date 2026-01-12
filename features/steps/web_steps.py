from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the "Login Page"')
def step_impl(context):
    context.driver.get(f"{context.base_url}/login")

@when('I login with email "{email}" and password "{password}"')
def step_impl(context, email, password):
    driver = context.driver
    wait = WebDriverWait(driver, 15)

    email_field = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    password_field = driver.find_element(By.NAME, "password")

    email_field.clear()
    email_field.send_keys(email)

    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Login')]")
    login_button.click()

@then('I should be redirected to the "{page}" page')
def step_impl(context, page):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains(f"/{page.lower()}"))

@when('I click the "{period}" navigation button')
def step_impl(context, period):
    driver = context.driver
    wait = WebDriverWait(driver, 10)

    period_button = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        f"//button[contains(@class,'MuiButton') and normalize-space()='{period}']"
    )))

    period_button.click()
    time.sleep(1)

@when("I perform logout")
def step_impl(context):
    driver = context.driver
    wait = WebDriverWait(driver, 20)

    sidebar = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'MuiDrawer-root')]" )))

    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", sidebar)
    time.sleep(1)

    btn_lainnya = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//text()[contains(., 'Lainnya')]]")))

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn_lainnya)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", btn_lainnya)

    btn_pengaturan = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/setting']")))
    driver.execute_script("arguments[0].click();", btn_pengaturan)

    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Keluar')]")))

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", logout_btn)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", logout_btn)
    time.sleep(4)

