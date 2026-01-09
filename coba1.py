from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    driver = setup_driver()
    base_url = "http://13.229.208.136:5173"
    
    try:
        user_data = {
            'full_name': 'Jason Santoso',
            'company_name': 'PT CAHAYA ABADI',
            'company_email': 'haniatester@gmail.com',
            'password': 'Admin@123',
            'password_confirmation': 'Admin@123',
            'address': 'Jalan Tunjungan 12334',
        }
        # registerrr
        driver.get(f"{base_url}")
        # register(driver, base_url, user_data)

        #loginnn
        # login(driver, base_url, "it.fingerspotmagang3@gmail.com", "halosemua123@")
        # login(driver, base_url, "haniatester@gmail.com", "Admin@1234")
        login(driver, base_url, "haniatester@gmail.com", "Admin@123")
        logout(driver,base_url)
        
        print("Menunggu 10 detik untuk melihat hasil...")
        time.sleep(10)
        

    except Exception as e:
        print(f"Terjadi error di fungsi utama: {e}")
    
    finally:
        print("Menutup browser...")
        driver.quit()

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def register(driver,url, user_data):
    wait = WebDriverWait(driver, 10)
    driver.get(url)

    btn_pindah_reg = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Buat akun di sini')]")
    ))
    btn_pindah_reg.click()

    wait.until(EC.presence_of_element_located((By.NAME, "full_name"))).send_keys(user_data['full_name'])
    
    driver.find_element(By.NAME, "company_name").send_keys(user_data['company_name'])
    driver.find_element(By.NAME, "company_email").send_keys(user_data['company_email'])
    driver.find_element(By.NAME, "password").send_keys(user_data['password'])
    driver.find_element(By.NAME, "password_confirmation").send_keys(user_data['password_confirmation'])
    driver.find_element(By.NAME, "address").send_keys(user_data['address'])

    time.sleep(1)

    btn_daftar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit' and contains(., 'Daftar akun')]")
    ))
    btn_daftar.click()

def login(driver,url, email, password):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    try:
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Login')]")

        email_field.clear()
        email_field.send_keys(email)
        time.sleep(1)
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(1)
        login_button.click()

        wait.until(EC.url_contains("/home"))
        
    except Exception as e:
        print(f"Gagal saat proses login:{e}")

def logout(driver, url):
    try:
        wait = WebDriverWait(driver, 15)
        wait.until(EC.url_contains("/home"))

        btn_lainnya = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Lainnya')]")))

        is_expanded = False
        try:
            pengaturan_check = driver.find_element(By.XPATH, "//a[@href='/setting']")
            if pengaturan_check.is_displayed():
                is_expanded = True
        except:
            is_expanded = False

        if not is_expanded:
            driver.execute_script("arguments[0].click();", btn_lainnya)
            time.sleep(1.5)

        btn_pengaturan = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/setting']")))
        btn_pengaturan.click()

        wait.until(EC.url_contains("/setting"))
        time.sleep(2)

        logout_xpath = "//button[contains(., 'Keluar')]"
        logout_button = wait.until(EC.presence_of_element_located((By.XPATH, logout_xpath)))
        
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout_button)
        time.sleep(2)

        driver.execute_script("arguments[0].click();", logout_button)

        wait.until(EC.url_contains("/login"))
        print("Logout Berhasil")

    except Exception as e:
        print(f"Logout Error: {e}")

if __name__ == "__main__":
    main()