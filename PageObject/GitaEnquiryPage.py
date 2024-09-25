from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class GitaEnquiryForm:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.join_now_button_locator = (By.XPATH, "(//span[@class='font-en svelte-t3mcl'][normalize-space()='Join now'])[1]")
        self.name_text_field_locator = (By.ID, "form-field-name")
        self.phone_text_field_locator = (By.ID, "form-field-phone")
        self.email_text_field_locator = (By.ID, "form-field-email")
        self.age_text_field_locator = (By.ID, "form-field-age")
        self.gender_field_locator = (By.ID, "form-field-gender")
        self.listening_to_acharya_prashant_since_locator = (By.ID, "form-field-listening-time")
        self.profession_field_locator = (By.ID, "form-field-profession")
        self.country_field_locator = (By.ID, "form-field-country")
        self.pincode_text_field_locator = (By.ID, "form-field-pincode")
        self.address_text_field_locator = (By.ID, "form-field-address")
        self.state_field_locator = (By.ID, "form-field-state")
        self.city_field_locator = (By.ID, "form-field-search-city")
        self.city_list_locator = (By.CSS_SELECTOR, ".h-full.overflow-y-scroll")
        self.tnc_checkbox_locator = (By.ID, "form-field-disclaimer")
        self.submit_button_locator = (By.XPATH, "//span[text()='Submit']")
        self.thank_you_page_locator = (By.XPATH, "//div[@class ='mx-12 my-20 text-center text-slate-700']/div[2]")

    def click_on_join_now(self):
        join_now_button = self.wait.until(EC.element_to_be_clickable(self.join_now_button_locator))
        join_now_button.click()

    def fill_form_details(self, name, email, phone, age, gender, duration, profession, state, city):
        self.wait_for_element_to_appear(self.name_text_field_locator)
        self.driver.find_element(*self.name_text_field_locator).send_keys(name)
        self.driver.find_element(*self.email_text_field_locator).send_keys(email)
        self.driver.find_element(*self.phone_text_field_locator).send_keys(phone)
        self.driver.find_element(*self.age_text_field_locator).send_keys(age)
        self.select_by_text(self.gender_field_locator, gender)
        self.select_by_text(self.listening_to_acharya_prashant_since_locator, duration)
        self.select_by_text(self.profession_field_locator, profession)
        self.scroll_down()
        self.select_by_text(self.state_field_locator, state)
        self.select_city(city)
        self.driver.find_element(*self.tnc_checkbox_locator).click()
        self.driver.find_element(*self.submit_button_locator).click()
        self.wait_for_element_to_appear(self.thank_you_page_locator)
        self.verify_thank_you_page()

    def select_city(self, city):
        city_field = self.driver.find_element(*self.city_field_locator)
        city_field.click()
        city_input_locator = (By.ID, "form-field-search-city-input-desktop")
        self.driver.find_element(*city_input_locator).send_keys(city)

        city_list = self.driver.find_elements(*self.city_list_locator)
        for city_element in city_list:
            if city in city_element.text:
                city_element.click()
                break

    def verify_thank_you_page(self):
        thank_you_text = self.driver.find_element(*self.thank_you_page_locator).text
        assert thank_you_text == "Thank you for submitting your enquiry"

    def wait_for_element_to_appear(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def select_by_text(self, locator, text):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 500)")
