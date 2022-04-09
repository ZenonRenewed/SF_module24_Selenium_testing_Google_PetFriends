import pytest


def test_pet_friends(selenium):
    # открываем стартовую станицу PetFriends:
    selenium.get("https://petfriends1.herokuapp.com/")

    # находим и кликаем на кнокпу нового пользователя
    btn_new_user = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_new_user.click()

    # кликаем на кнопку "...уже есть аккаунт"
    btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # вписываем мейл
    field_email = selenium.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("1234iop@mail.com")

    # вписываем пароль
    field_pass = selenium.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("1234iop")

    # находим и кликаем на кнопку "войти"
    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    if selenium.current_url == 'https://petfriends1.herokuapp.com/all_pets':
        # делаем скриншот
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('1234iop@mail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('1234iop')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
