from POM.module import HomeStay
class TestModule:
    def test_module(self,_driver):
        lp = HomeStay(_driver)
        lp.click_language1()