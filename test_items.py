import time


def test_for_change_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector\
        (".btn.btn-lg.btn-primary.btn-add-to-basket").is_displayed(),\
        "There is no button to adding to the basket"



#pytest --language=es test_items.py


