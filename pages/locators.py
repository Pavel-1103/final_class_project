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



class MainPageLocators:
    SCREEN_SLIDER = (By.XPATH, "//div[@class='screen_slider']")
    CAT_ZARYADKI = (By.XPATH, "//a[@href='category/zaryadki']")
    SUB_CAT_POWER_BANK = (By.XPATH, "//ul[@class='cat_menu']/li[5]/ul/li[6]")

    INFO_BLOCK_VOZVRAT_SREDSTV = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[1]/div")
    INFO_BLOCK_DOSTAVKA = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[2]/div")
    INFO_BLOCK_OTSROCHKA = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[3]/div")
    INFO_BLOCK_SUPPORT = (By.XPATH, "//div[@class='characteristics']//div[@class='row']/div[4]/div")
    BUTTON_SHOW_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals_title clearfix']//a[@href='main/showNew']")
    BUTTON_PREV_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals']//div[@class='arrivals_nav arrivals_prev']")
    BUTTON_NEXT_NEW_PRODUCTS = (By.XPATH, "//div[@class='new_arrivals']//div[@class='arrivals_nav arrivals_next']")
    SECTION_NEW_PRODUCTS = (By.XPATH, "//div[@class='nes_arrivals']//div[@class='slick-list draggable']")
    NEW_PRODUCT_8 = (By.XPATH, "//div[@class='new_arrivals']//div[@class='slick-list draggable']/div/div[3]div[2]")
    BUTTON_SHOW_HITS = (By.XPATH, "//div[@class='best_sellers']//a[@href='main/showHit']")
    BUTTON_PREV_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='best_prev best_nav']/i")
    BUTTON_NEXT_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='best_next best_nav']/i")
    SECTION_HITS = (By.XPATH, "//div[@class='best_sellers']//div[@class='bestsellers_panel panel_active']")
    BUTTON_PREV_TREND = (By.XPATH, "//div[@class='trends']//div[@class='trends_prev trendsna_nav slick-arrow']/i")
    BUTTON_NEXT_TREND = (By.XPATH, "//div[@class='trends']//div[@class='trends_next trends_nav slick-arrow']/i")