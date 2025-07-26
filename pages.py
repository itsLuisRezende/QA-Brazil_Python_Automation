from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR= (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, "//button[text()='Chamar um táxi']")

    SELECT_PLAN_BUTTON = (By.XPATH, "//button[@data-for='tariff-card-4']")
    TEXT_SELECT_PLAN = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

    NUMBER_PHONE = (By.XPATH, "//div[contains(@class, 'np-button') and .//div[text()='Número de telefone']]")
    NUMBER_PHONE_INPUT = (By.ID, 'phone')
    NUMBER_PHONE_CODE_INPUT = (By.ID, 'code')
    NUMBER_PHONE_NEXT_BUTTON = (By.CSS_SELECTOR, '.full')
    NUMBER_PHONE_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')
    NUMBER_PHONE_TEXT = (By.CSS_SELECTOR, "div.np-text")

    PAYMENT_METHOD_SELECT = (By.XPATH, "//div[@class='pp-button filled' and .//div[text()='Método de pagamento']]")
    ADD_CARD_CONTROL = (By.XPATH, "//div[@class='pp-row disabled' and .//div[text()='Adicionar cartão']]")
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.ID, 'code')
    CARD_PLC_IMAGE = (By.CLASS_NAME, 'plc')
    CARD_CREDENTIALS_CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Adicionar')]")
    CLOSE_BUTTON_PAYMENT_METHOD = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]' )
    CURRENT_PAYMENT_METHOD = (By.CLASS_NAME, 'pp-value-text')
    MESSAGE_FOR_DRIVER_TRIP = (By.ID, 'comment')
    OPTION_SWITCHES = (By.CLASS_NAME, 'switch')
    OPTION_SWITCHES_INPUTS = (By.CLASS_NAME, 'switch-input')
    ADD_ENUMERABLE_OPTION = (By.CLASS_NAME, 'counter-plus')
    AMOUNT_OF_ENUMERABLE_OPTION = (By.CLASS_NAME, 'counter-value')
    ORDER_CAR_BUTTON = (By.CLASS_NAME, 'smart-button-wrapper')
    ORDER_POPUP = (By.CLASS_NAME, 'order-body')
    PROGRESS_BAR = (By.CLASS_NAME, 'order-progress visible')
    DRIVER_WAIT_TIME = (By.CLASS_NAME, 'order-header-time')
    ORDER_DRIVER_RATING = (By.CLASS_NAME, 'order-btn-rating')
    ORDER_DRIVER_IMAGE = (By.XPATH, '//div[@class="order-button"]//img')
    ORDER_DRIVER_NAME = (By.XPATH, '//div[@class="order-btn-group"][1]/div[2]')

    def __init__(self,driver):
        self.driver = driver

    #FUNÇÔES DE ESPERA
    def _wait_for_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def _wait_for(self, locator, timeout=5, condition=EC.presence_of_element_located):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    #Métodos combinados
    def set_route(self, from_address, to_address): #Define o endereço
        self.enter_from_location(from_address)
        self.enter_to_location(to_address)

    #Métodos individuais
    def enter_from_location(self, from_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "from"))
        ).send_keys(from_address)

    def enter_to_location(self, to_address):
        # Inserir Para
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "to"))
        ).send_keys(to_address)

    def get_from(self):
        return self._wait_for(self.FROM_LOCATOR).get_property('value')

    def get_to(self):
        return self._wait_for(self.TO_LOCATOR).get_property('value')

    def click_call_taxi(self):
        self._wait_for_visible(self.CALL_TAXI_BUTTON).click()

    def click_select_plan(self):
        wait = WebDriverWait(self.driver, 10)

        # Etapa 1: Clica no plano "Comfort"
        comfort_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Comfort')]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comfort_card)
        comfort_card.click()

        # Etapa 2: Agora espera o botão ficar visível e clicável
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-for='tariff-card-4']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()

    def get_select_plan_text(self):
        return self._wait_for(self.TEXT_SELECT_PLAN).text

    def set_phone(self, number):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Número de telefone']"))
        ).click()
        self._wait_for(self.NUMBER_PHONE_INPUT).send_keys(number)
        self._wait_for(self.NUMBER_PHONE_NEXT_BUTTON).click()
        code = retrieve_phone_code(self.driver)
        self._wait_for(self.NUMBER_PHONE_CODE_INPUT).send_keys(code)
        self._wait_for(self.NUMBER_PHONE_CONFIRM_BUTTON).click()

    def get_phone(self):
        return self._wait_for(self.NUMBER_PHONE_TEXT).text

    def set_card(self, card_number, code):
        self.driver.find_element(*self.PAYMENT_METHOD_SELECT).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.ADD_CARD_CONTROL).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(f"{card_number}{Keys.TAB}{code}")
        self.driver.find_element(*self.CARD_PLC_IMAGE).click()
        self.driver.find_element(*self.CARD_CREDENTIALS_CONFIRM_BUTTON).click()
        self.driver.find_element(*self.CLOSE_BUTTON_PAYMENT_METHOD).click()


    def get_current_payment_method(self):
        return self._wait_for(self.CURRENT_PAYMENT_METHOD).text

    def set_message_for_driver(self, message):
        self._wait_for(self.MESSAGE_FOR_DRIVER_TRIP).send_keys(message)

    def get_message_for_driver(self):
        return self._wait_for(self.MESSAGE_FOR_DRIVER_TRIP).get_property('value')

    def click_blanket_and_handkerchiefs_option(self):
        switches = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.OPTION_SWITCHES)
        )
        switches[0].click()
        self.get_blanket_and_handkerchiefs_option_checked()

    def get_blanket_and_handkerchiefs_option_checked(self):
        switches = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.OPTION_SWITCHES_INPUTS)
        )
        return switches[0].get_property('checked')

    def add_ice_cream(self, amount: int):
        option_add_controls = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.ADD_ENUMERABLE_OPTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", option_add_controls[0])
        for _ in range(amount):
            option_add_controls[0].click()

    def get_amount_of_ice_cream(self):
        return int(WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.AMOUNT_OF_ENUMERABLE_OPTION)
        ).text)

    def click_order_taxi_button(self):
        self._wait_for(self.ORDER_CAR_BUTTON).click()

    def wait_order_taxi_popup(self):
        self._wait_for_visible(self.ORDER_POPUP)

    def wait_driver_info(self):
        WebDriverWait(self.driver,60).until(
            EC.invisibility_of_element_located(self.DRIVER_WAIT_TIME)
        )
        self._wait_for(self.ORDER_DRIVER_RATING)
        self._wait_for(self.ORDER_DRIVER_IMAGE)
        self._wait_for(self.ORDER_DRIVER_NAME)

    def get_driver_info(self):
        rating = self._wait_for(self.ORDER_DRIVER_RATING).text
        image = self._wait_for(self.ORDER_DRIVER_IMAGE).get_property('src')
        name = self._wait_for(self.ORDER_DRIVER_NAME).text
        return name, rating, image

