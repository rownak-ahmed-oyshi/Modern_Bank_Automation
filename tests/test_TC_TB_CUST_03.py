import logging

import pytest

from utils.screenshot_utils import capture_full_page_screenshot
from pages.customer_register_page import CustomerRegisterPage
from utils.data_loader import get_test_case

@pytest.mark.parametrize(
    "customer_test_case",
    [get_test_case("customer_test_data.json", "valid_customers", 1)]  # index 1 → Rownak Ahmed Oyshi
) #connecting data loader

def test_tc_tb_cust_03(browser_config,customer_test_case):
    logging.info("TC_TB_CUST_03 Started..")
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
        logging.info("Element 'Customer Email Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer Password Field !!!")

    # Enter Customer Initial Deposit Field
    try:
        customer_register_page.enter_initial_deposit(customer_test_case["initial_deposit"])
        logging.info("Customer Initial Deposit Entered successfully.")

    except Exception as e:
        logging.info("Element 'Customer Email Field' not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer Initial Deposit Field !!!")

    # Click on Register Button
    try:
        customer_register_page.click_register_button()
        logging.info("Click on Register button successfully.")

    except Exception as e:
        logging.info("Element in Customer 'Register' button not found with Explicit wait.")
        pytest.fail("Test Failed. Bug found for Customer 'Register' Button !!!")

    # Input the same values for the second time to check Email Duplicacy
    customer_register_page.enter_customer_full_name(customer_test_case["customer_full_name"])
    customer_register_page.enter_customer_email(customer_test_case["customer_email"])
    customer_register_page.enter_customer_password(customer_test_case["customer_password"])
    customer_register_page.enter_initial_deposit(customer_test_case["initial_deposit"])
    customer_register_page.click_register_button()
    logging.info("Input the same values for the second time to check Email Duplicacy")


    # Validate Customer Registration Error Message
    expected_message = customer_test_case["expected_error_message"]
    actual_message = customer_register_page.get_customer_register_error_message()


    if expected_message == actual_message:
        logging.info(f"Test Passed. Message matched: '{actual_message}'")
    else:
        logging.info(f"Test Failed. Expected: '{expected_message}', Actual: '{actual_message}'")
        capture_full_page_screenshot(driver, "BUG_TC_TB_CUST_03")
        pytest.fail("Customer registration message did not match expected.")

