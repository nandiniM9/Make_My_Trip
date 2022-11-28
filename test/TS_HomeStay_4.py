from POM.module import HomeStay
class TestModule:
    def test_module(self,_driver):
        lp=HomeStay(_driver)
        lp.Click_homestay()
        lp.select_place()
        lp.click_selected_place()
        lp.checkin_date()
        lp.checkout_date()