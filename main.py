import data
from data import *
from helpers import *
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None
    @classmethod
    def setup_class(cls):
        # o código que você adicionou no sprint anterior

        # não modifique, pois precisamos do registro adicional habilitado para recuperar o código de confirmação do telefone
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        if is_url_reachable(URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print( "Não foi possível conectar ao Urban Routes")

    def test_set_route(self): #"Função criada para definir rota.
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.click_call_taxi()

    def test_select_plan(self): #"Função criada para selecionar plano."
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_select_plan()
        assert routes_page.get_select_plan_text() == 'Comfort'

    def test_fill_phone_number(self): #"Função criada para preencher número de telefone."
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.PHONE_NUMBER
        routes_page.set_phone(phone_number)
        assert routes_page.get_phone() == phone_number

    def test_fill_card(self): #"Função criada para preencher cartão."
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self): #"Função criada para comentar com o motorista.")
        routes_page = UrbanRoutesPage(self.driver)
        message = data.MESSAGE_FOR_DRIVER
        routes_page.set_message_for_driver(message)
        assert routes_page.get_message_for_driver() == message

    def test_order_blanket_and_handkerchiefs(self): #"Função criada para encomendar cobertores e lençóis.")
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_handkerchiefs_option()
        assert routes_page.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self): #"Função criada para pedido de 2 sorvetes.")
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream(2)
        assert routes_page.get_amount_of_ice_cream() == 2

    def test_car_search_model_appears(self): #"Função criada para aparecer modelo de busca de carros.")
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi_button()
        routes_page.wait_order_taxi_popup()

    def test_driver_info_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_driver_info()
        name, rating, image = routes_page.get_driver_info()
        assert name
        assert rating
        assert image

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()





