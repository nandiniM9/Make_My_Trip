# import pytest
# from selenium import webdriver
# from Library.config import config
# @pytest.fixture()
# def _driver():
#     driver=webdriver.Chrome(config.Chrome_path)
#     # driver=webdriver.Edge(config.edge_path)
#     # driver=webdriver.Firefox(r'C:\Users\Vishi\OneDrive\Desktop\sprint-2\chromedriver_win32\geckodriver.exe')
#     driver.get(config.url)
#     driver.maximize_window()
#     yield driver


import pytest
from selenium import webdriver
from Library.config import config
# path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options

#Cross Browsing
# firefox_Driver_path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\geckodriver.exe"
@pytest.fixture(params=["Edge","Chrome"])
def _driver(request):
    # if request.param == "Firefox":
    #     options = Options()
    #     options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #     driver = webdriver.Firefox(executable_path=firefox_Driver_path,options=options)
    if request.param == "Edge":
        driver = webdriver.Edge(config.edge_path)
    elif request.param == "Chrome":
        driver = webdriver.Chrome(config.Chrome_path)
    driver.get(config.url)
    driver.maximize_window()
    yield driver

    print(driver.title)
    # driver.save_screenshot("text_loginpage.png")
    driver.close()