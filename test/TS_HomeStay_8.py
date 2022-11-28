from POM.module import HomeStay
class TestModule:
    def test_module(self,_driver):
        lp=HomeStay(_driver)
        lp.Click_homestay()
        lp.select_place()
        lp.click_selected_place()
        lp.checkin_date()
        lp.checkout_date()
        lp.no_of_person()
        lp.click_onappyly()
        lp.click_onsearch()
        lp.select_hotel()