from Data import reading_objects
import time
apply_value=reading_objects.read_locators()

class HomeStay:
    def __init__(self, _driver):
        self.driver=_driver

    #language selector hindi
    def click_language1(self):
        # self.driver.find_element('xpath', '//span[@data-cy="myIconWhite"]').click()
        # self.driver.find_element('xpath','//div[@id="SW"]').click()
        self.driver.find_element(*apply_value['click_language1']).click()
        time.sleep(1)
    def select_india(self):
        self.driver.find_element(*apply_value['select_india']).click()
        time.sleep(1)
    def select_india_click(self):
        self.driver.find_element(*apply_value['select_india_click']).click()
        time.sleep(1)
    def select_hindi_lan(self):
        self.driver.find_element(*apply_value['select_hindi_lan']).click()
    def hindi_btn(self):
        self.driver.find_element(*apply_value['hindi_btn']).click()

    #language selector India-tamil
    def click_language3(self):
        # self.driver.find_element('xpath', '//span[@data-cy="myIconWhite"]').click()
        # self.driver.find_element('xpath', '//div[@id="SW"]').click()
        self.driver.find_element(*apply_value['click_language3']).click()
        time.sleep(1)
    def india_tamil_lan(self):
        self.driver.find_element(*apply_value['india_tamil_lan']).click()
    def india_tamil_btn(self):
        self.driver.find_element(*apply_value['india_tamil_btn']).click()

    #language selector uae-urdu

    def click_language4(self):
        # self.driver.find_element('xpath', '//span[@data-cy="myIconWhite"]').click()
        # self.driver.find_element('xpath', '//div[@id="SW"]').click()
        self.driver.find_element(*apply_value['click_language4']).click()
        time.sleep(1)
    def select_UAE(self):
        self.driver.find_element(*apply_value['select_india']).click()
        time.sleep(1)
    def select_uae_click(self):
        self.driver.find_element(*apply_value['select_uae_click']).click()
        time.sleep(1)
    def uae_urdu_lan(self):
        self.driver.find_element(*apply_value['uae_urdu_lan']).click()

    def uae_urdu_btn(self):
        self.driver.find_element(*apply_value['uae_urdu_btn']).click()

    #language selector uae-english
    def click_language5(self):
        # self.driver.find_element('xpath', '//span[@data-cy="myIconWhite"]').click()
        # self.driver.find_element('xpath', '//div[@id="SW"]').click()
        self.driver.find_element(*apply_value['click_language5']).click()
        time.sleep(1)

    def uae_english_lan(self):
        self.driver.find_element(*apply_value['uae_english_lan']).click()

    def uae_english_btn(self):
        self.driver.find_element(*apply_value['uae_english_btn']).click()

    #language selector usa-english
    def click_language6(self):
        # self.driver.find_element('xpath', '//span[@data-cy="myIconWhite"]').click()
        # self.driver.find_element('xpath', '//div[@id="SW"]').click()
        self.driver.find_element(*apply_value['click_language6']).click()
        time.sleep(1)
    def select_usa(self):
        self.driver.find_element(*apply_value['select_india']).click()
        time.sleep(1)
    def select_usa_click(self):
        self.driver.find_element(*apply_value['select_usa_click']).click()
        time.sleep(1)
    def usa_english_lan(self):
        self.driver.find_element(*apply_value['usa_english_lan']).click()

    def usa_english_btn(self):
        self.driver.find_element(*apply_value['uae_english_btn']).click()

    # language selector india-english

    def click_language2(self):
        # self.driver.find_element('xpath', '//span[@data-cy="myIconWhite"]').click()
        # self.driver.find_element('xpath', '//div[@id="SW"]').click()
        self.driver.find_element(*apply_value['click_language2']).click()
        time.sleep(1)

    def select_india1(self):
        self.driver.find_element(*apply_value['select_india']).click()
        time.sleep(1)
    def select_india1_click(self):
        self.driver.find_element(*apply_value['select_india1_click']).click()
        time.sleep(1)

    def india_english_lan(self):
        self.driver.find_element(*apply_value['india_english_lan']).click()

    def india_english_btn(self):
        self.driver.find_element(*apply_value['uae_english_btn']).click()


    def Click_homestay(self):
        self.driver.find_element(*apply_value['Click_homestay']).click()
        time.sleep(2)
    def select_place(self):
        self.driver.find_element(*apply_value['select_place']).send_keys('delhi')
        time.sleep(2)
        self.driver.find_element(*apply_value['select_place']).send_keys('delhi')

    def click_selected_place(self):
        try:
            self.driver.find_element(*apply_value['click_selected_place']).click()
            time.sleep(2)
        except:
            self.driver.find_element('xpath', '//p[text()="Delhi"]').click()
    def checkin_date(self):
        self.driver.find_element(*apply_value['checkin_date']).click()
        time.sleep(2)
    def checkout_date(self):
        self.driver.find_element(*apply_value['checkout_date']).click()
        time.sleep(2)
    def no_of_person(self):
        self.driver.find_element(*apply_value['no_of_person']).click()
        time.sleep(2)
    def click_onappyly(self):
        self.driver.find_element(*apply_value['click_onappyly']).click()
        time.sleep(2)
    def click_onsearch(self):
        self.driver.find_element(*apply_value['click_onsearch']).click()
        time.sleep(2)
    def select_hotel(self):
        self.driver.find_element(*apply_value['select_hotel']).click()
        time.sleep(2)


