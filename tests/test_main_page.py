import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from settings import sets



@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

      #def test_login_logout(self, browser):
      #  link_to_site = browser.current_url

    def test_main_page_header(self,browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_feedback()
