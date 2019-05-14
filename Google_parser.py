from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome(executable_path='/home/deepzeedi/Python/chromedriver')

# Открываем Chrome и переходим на стартовую страницу Google
browser.get('https://www.google.com/')

# Подключаем ActionChains ввода
action = ActionChains(browser)

# Ищем на странице поле ввода и кнопку поиска
search_form = browser.find_element_by_name('f')
search_button = browser.find_element_by_xpath('//div/center/input')

def send_form():

    '''request and sending query'''
    request = input('\nЧто ищем?: ')
    action.click(search_form)
    action.send_keys(request)
    action.pause(1)
    action.move_to_element(search_button)
    action.click(search_button)
    action.perform()

# Отправляем запрос в Google
send_form()

print('')

# Выбираем поисковые результаты
titles = browser.find_elements_by_xpath('//div/a/h3')
links = browser.find_elements_by_xpath('//cite')
quotes = browser.find_elements_by_xpath('//div/span[@class="st"]')
# Печатаем в консоль результаты поиска
for title, link, quote, in zip(titles, links, quotes):
    print(f'\n{title.text.upper()}\n{link.text}\n{quote.text}\n')

input('\nPress enter to exit...')
browser.quit()

