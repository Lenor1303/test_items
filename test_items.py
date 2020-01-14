import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#проверка наличия кнопки "добавить корзину"
def test_see_login_add_button(browser):
    browser.get(link)
    time.sleep(3)
    button = len(browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0 , 'Элемент по данному селектору отсутсвует'