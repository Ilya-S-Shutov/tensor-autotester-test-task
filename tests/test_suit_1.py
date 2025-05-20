import pytest

from pages.company_list_page import CompanyListPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestSuit1:
    def test_step_1(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_link_all_about_company()

        profile_page = ProfilePage(driver)
        profile_page.add_cookie('abtest-profile', 'A')

        assert profile_page.get_current_url() == 'https://saby.ru/profile'

    def test_step_2(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.skip_stage()
        company_list_page = CompanyListPage(driver)
        company_list_page.use_search('тензор')

        company_info_list = company_list_page.get_items_info(10)
        # 'Газпром, ПАО\nСанкт-Петербург\n7736050003\nМиллер А.Б.\nТопливо и Энергетика'
        result = all(map(lambda item: 'тензор' in item, company_info_list))
        assert result is True
