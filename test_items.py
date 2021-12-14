import time

def test_check_if_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(5)
    
    button_folder = browser.find_elements_by_class_name("btn-add-to-basket")

    assert len(button_folder) > 0, "There is no basket button"