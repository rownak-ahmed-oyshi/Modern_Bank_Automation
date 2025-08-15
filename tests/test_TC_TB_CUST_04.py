import logging

import pytest

from utils.screenshot_utils import capture_full_page_screenshot
from pages.customer_register_page import CustomerRegisterPage
from utils.data_loader import get_test_case

@pytest.mark.parametrize(
    "customer_test_case",
    [get_test_case("customer_test_data.json", "invalid_customers", 1)]  # index 1 → Rownak
) #connecting data loader


def test_tc_tb_cust_04(browser_config,customer_test_case):
    logging.info("TC_TB_CUST_04 Started..")
    driver, wait = browser_config

    # Create object for customer register page class
    customer_register_page = CustomerRegisterPage(driver,wait)

    try:
        customer_register_page.click_open_your_account_button()
        logging.info("Click on Open Your Account Button successfully.")

    except Exception as e:
        logging.info("Element 'Open Your Account' button not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Open Your Account Button !!!")

    # Enter Customer Full name field
    try:
        customer_register_page.enter_customer_full_name(customer_test_case["customer_full_name"])
        logging.info("Customer Full Name entered successfully.")

    except Exception as e:
        logging.info("Element 'Customer Full Name Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer Full Name Field !!!")

    # Enter Customer Email Address field
    try:
        customer_register_page.enter_customer_email(customer_test_case["customer_email"])
        logging.info("Customer Email Address entered successfully.")

    except Exception as e:
        logging.info("Element 'Customer Email Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer Email Field !!!")

    # Enter Customer Password Field
    try:
        customer_register_page.enter_customer_password(customer_test_case["customer_password"])
        logging.info("Customer Password Enter successfully.")

    except Exception as e:
        logging.info("Element 'Customer Password Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer Password Field !!!")

    # Enter Customer Initial Deposit Field
    try:
        customer_register_page.enter_initial_deposit(customer_test_case["initial_deposit"])
        logging.info("Customer Initial Deposit Entered successfully.")

    except Exception as e:
        logging.info("Element 'Customer Initial Deposit ' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer Initial Deposit Field !!!")

    # Click on Register Button
    try:
        customer_register_page.click_register_button()
        logging.info("Click on Register button successfully.")

    except Exception as e:
        logging.info("Element in Customer 'Register' button not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer 'Register' Button !!!")

    # Grab validation message in email separately
    try:
        validation_message = customer_register_page.get_validation_message("#customerEmailReg")
        expected_message = customer_test_case["expected_validation_message"]

        if validation_message == expected_message:
            logging.info(f"Test Passed. Email Validation message matched: '{validation_message}'")
        else:
            logging.info(f"Test Failed. Expected: '{expected_message}', Actual: '{validation_message}'")
            capture_full_page_screenshot(driver, "BUG_TC_TB_CUST_04")
            pytest.fail("Email Validation message did not match expected.")

    except Exception as e:
        logging.info("Email Validation message could not be fetched.")
        pytest.fail("Test Failed. Bug in fetching email validation message!")

