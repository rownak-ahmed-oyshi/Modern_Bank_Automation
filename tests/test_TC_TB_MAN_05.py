import logging

import pytest

from utils.screenshot_utils import capture_full_page_screenshot
from pages.manager_register_page import ManagerRegisterPage
from utils.data_loader import get_test_case

@pytest.mark.parametrize(
    "manager_test_case",
    [get_test_case("manager_test_data.json", "invalid_manager", 2)]  # index 2 → Rownak Ahmed Oyshi
) #connecting data loader

def test_tc_tb_man_05(browser_config,manager_test_case):
    logging.info("TC_TB_MAN_05 Started..")
    driver, wait = browser_config

    # Create object for Manager register page class
    manager_register_page = ManagerRegisterPage(driver,wait)

    try:
        manager_register_page.click_register_as_manager_button()
        logging.info("Click on Register as Manager successfully.")

    except Exception as e:
        logging.info("Element 'Register as Manager' button not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Register as Manager Button !!!")

    # Enter Manager Full name field
    try:
        manager_register_page.enter_manager_full_name(manager_test_case["manager_full_name"])
        logging.info("Manager Full Name entered successfully.")

    except Exception as e:
        logging.info("Element 'Manager Full Name Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Manager Full Name Field !!!")

    # Enter Manager Email Address field
    try:
        manager_register_page.enter_manager_email(manager_test_case["manager_email"])
        logging.info("Manager Email Address entered successfully.")

    except Exception as e:
        logging.info("Element 'Manager Email Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Manager Email Field !!!")

    # Enter Manager Password Field
    try:
        manager_register_page.enter_manager_password(manager_test_case["manager_password"])
        logging.info("Manager Password Enter successfully.")

    except Exception as e:
        logging.info("Element 'Manager Password Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Manager Password Field !!!")

    # Click on Register Button
    try:
        manager_register_page.click_manager_register_button()
        logging.info("Click on Register button successfully.")

    except Exception as e:
        logging.info("Element in Manager 'Register' button not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Manager 'Register' Button !!!")

    # Grab validation message in for SQL injection in Email separately
    try:
        validation_message = manager_register_page.get_validation_message("#managerEmailReg")
        expected_message = manager_test_case["expected_validation_message"]

        if validation_message == expected_message:
            logging.info(f"Test Passed. Manager Email Error Validation message matched for SQL injection: '{validation_message}'")
        else:
            logging.info(f"Test Failed. Expected: '{expected_message}', Actual: '{validation_message}'")
            capture_full_page_screenshot(driver, "BUG_TC_TB_MAN_05")
            pytest.fail("Manager Email Error Validation message for SQL injection did not match expected.")

    except Exception as e:
        logging.info("Manager Email Error Validation message for SQL injection could not be fetched.")
        pytest.fail("Test Failed. Bug in fetching manager Email Error validation message for SQL injection!")