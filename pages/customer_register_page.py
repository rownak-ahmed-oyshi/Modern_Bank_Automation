from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CustomerRegisterPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def click_open_your_account_button(self):
        open_your_account_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#homeRegisterCustomerBtnMain")))
        open_your_account_button.click()

    def enter_customer_full_name(self, full_name):
        customer_full_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerNameReg")))
        customer_full_name.send_keys(str(full_name))

    def enter_customer_email(self, email):
        customer_email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerEmailReg")))
        customer_email.send_keys(str(email))

    def enter_customer_password(self, password):
        customer_password = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#customerPasswordReg")))
        customer_password.send_keys(str(password))

    def enter_initial_deposit(self, deposit):
        initial_deposit = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#initialDepositReg")))
        initial_deposit.send_keys(str(deposit))

    def click_register_button(self):
        register_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='customerRegisterForm'] button[type='submit']")))
        register_button.click()

    def click_back_to_home_button(self):
        back_to_home_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='customerRegisterForm'] button[type='button']")))
        back_to_home_button.click()

    def get_validation_message(self, input_css_selector):
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_css_selector)))
        return element.get_attribute("validationMessage")

    def get_customer_registered_successful_message(self):
        customer_registered_successful_message = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#customerRegMessage")))

        return customer_registered_successful_message.text

    def get_customer_register_error_message(self):
        customer_register_error_message = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#customerRegMessage")))

        return customer_register_error_message.text

