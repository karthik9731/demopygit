from selenium import webdriver
from time import sleep
import pytest


@pytest.mark.parametrize('username,password',[('karthik','karthik@12C')])
def test_add(username,password,):
    assert username == 'karthik',"invalid username"
    assert password == "karthik@12C", 'invalid password'
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opt)
    driver.get("https://en.wikipedia.org/wiki/File:Okay.gif")
    sleep(5)
    driver.close()
    return driver


@pytest.fixture(params=["Chrome","Firefox"])
def launch(request):
    if request.param == "Chrome":
        global driver
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver

def test_sub(launch):
    driver.get("https://en.wikipedia.org/wiki/File:Okay.gif")

