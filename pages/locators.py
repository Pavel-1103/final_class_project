from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_SINGUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    DETAILS = (By.XPATH, "//a[text() = 'Детали сотрудничества']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    LOGISTIC = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")
    CURRENCY = (By.XPATH, "//select[@id='currency']")

    CURRENCY_UAH = (By.XPATH, "//select[@id='currency']/option[text()='UAH']")
    CURRENCY_USD = (By.XPATH, "//select[@id='currency']/option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//select[@id='currency']/option[text()='EUR']")
    LOGO_DESK = (By.XPATH, "//div[@class='logo logo-desk']/a/ing")
    LOGO_MOB = (By.XPATH, "//div[@class='logo logo-mob']/a/ing")
    SEARCH = (By.XPATH, "//*[@id='typehead']")
    SUBMIT = (By.XPATH, "//div[@class='header_search']//button")
    WISH = (By.XPATH, "//div[contains(@class, 'wishlist')]/div[@class='wishlist_icon']/a/img")
    CART = (By.XPATH, "//div[@class='cart']//div[@class='cart_icon']/a/img")
    HITS = (By.XPATH, "//a[@class='check-item check-hot']")
    DISCOUNTS = (By.XPATH, "//a[@class='check-item check-sale']")
    NEW_ITEMS = (By.XPATH, "//a[@class='check-item']")
    SAMSUNG_CAT = (By.XPATH, "//div[text()='Samsung']")
    SAMSUNG_J701 = (By.XPATH, "//a[@href='BrandModel/Samsung-J701']")

    SUBSCRUBE = (By.XPATH, "//button[@class='newsletter_button']")
    INPUT_SUBSCRIBE = (By.XPATH,"//input[@class='newsletter_input']")
    LOGO_FOOT = (By.XPATH, "//img[@src='images/logo-footer.png']")


