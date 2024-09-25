import unittest
from selenium import webdriver
from PageObject.GitaEnquiryPage import GitaEnquiryForm


class GitaEnquiryTest(unittest.TestCase):

    def setUp(self):
        # Set up WebDriver (assuming Chrome for this example)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_gita_enquiry(self):
        self.driver.get("https://dev-main-master2.vedant.life/en/enquiry-gita")
        gita_form = GitaEnquiryForm(self.driver)
        gita_form.fill_form_details(
            "ekta", "ekta99@yopmail.com", "9310980049", "20", "Female",
            "1 to 3 months", "Other", "Delhi", "New Delhi"
        )

    def test_vbc_enquiry(self):
        self.driver.get("https://dev-main-master2.vedant.life/en/enquiry-vedant-english")
        gita_form = GitaEnquiryForm(self.driver)
        gita_form.fill_form_details(
            "ekta", "ekta99@yopmail.com", "9310980049", "20", "Female",
            "1 to 3 months", "Other", "Delhi", "New Delhi"
        )

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

