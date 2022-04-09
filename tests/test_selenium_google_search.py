def test_chrome_google_search(selenium):
    # открываем сайт
    selenium.get('https://google.com')

    # ищем поисковое поле с помощью его уникального атрибута name и заключаем его в переменную search_input
    search_input = selenium.find_element_by_name('q')

    # очищаем заранее поисковое поле и вводим в него запрос
    search_input.clear()
    search_input.send_keys('my first selenium test for web ui')

    # ищем кнопку поиска по name и заключаем ее в переменную search button
    search_button = selenium.find_element_by_xpath("(//input[@name='btnK'])[2]")
    search_button = selenium.find_element_by_xpath("(//input[@name='btnK'])[2]")
    # кликаем по кнопке для поиска
    search_button.click()

    # делаем скриншот результата
    selenium.save_screenshot('result.png')


# альтернативный вариант
def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')

    # Find the field for search text input:
    search_input = selenium.find_element_by_name('q')

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    # здесь мы используем submit, так как выпадающая строка загораживает кнопку поиска
    # Click Search:
    search_button = selenium.find_element_by_name('btnK')
    search_button.submit()

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')
