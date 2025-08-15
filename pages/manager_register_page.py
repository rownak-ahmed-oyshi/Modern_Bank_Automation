from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ManagerRegisterPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def click_register_as_manager_button(self):
        register_as_manager_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#homeRegisterManagerBtn")))
        register_as_manager_button.click()

    def enter_manager_full_name(self, full_name):
        manager_full_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#managerNameReg")))
        manager_full_name.send_keys(str(full_name))

    def enter_manager_email(self, email):
        manager_email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#managerEmailReg")))
        manager_email.send_keys(str(email))

    def enter_manager_password(self, password):
        manager_password = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#managerPasswordReg")))
        manager_password.send_keys(str(password))


    def click_manager_register_button(self):
        manager_register_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='managerRegisterForm'] button[type='submit']")))
        manager_register_button.click()

    def click_back_to_home_button(self):
        back_to_home_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='managerRegisterForm'] button[type='button']")))
        back_to_home_button.click()

    def get_validation_message(self, input_css_selector):
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_css_selector)))
        return element.get_attribute("validationMessage")

    def get_manager_registered_successful_message(self):
        manager_registered_successful_message = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#managerRegMessage")))

        return manager_registered_successful_message.text

    def get_manager_register_error_message(self):
        manager_register_error_message = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#managerRegMessage")))

        return manager_register_error_message.text

