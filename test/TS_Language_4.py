from POM.module import HomeStay
class TestModule:
    def test_module(self,_driver):
        lp=HomeStay(_driver)
        lp.click_language1()
        lp.select_india()
        lp.select_india_click()
        lp.select_hindi_lan()
        lp.india_tamil_lan()
