from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка "Личный кабинет" в шапке сайта
    LK_IN_THE_HEADER = [By.LINK_TEXT, "Личный Кабинет"]
    # Кнопка "Восстановить пароль" на странице авторизации
    PASSWORD_RECOVERY_BUTTON = [By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Восстановить пароль']"]
    # Кнопка "Войти в аккаунт"
    ACCOUNT_BUTTON = [By.XPATH, ".//button[text() = 'Войти в аккаунт']"]
    # Поле "Email" в форме авторизации
    EMAIL_LOGIN = [By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @name = 'name']"]
    # Поле "Пароль" в форме авторизации
    PASSWORD_LOGIN = [By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and @name = "
                                "'Пароль']"]
    # Кнопка "Войти" в форме авторизации
    LOGIN_BUTTON = [By.XPATH, ".//button[text() = 'Войти']"]
    # Конструктор
    CONSTRUCTOR = [By.XPATH, ".//p[text() = 'Конструктор']"]
    # Конструктор в активном состоянии
    CONSTRUCTOR_ACTIV = [By.XPATH, ".//a[@class = 'AppHeader_header__link__3D_hX AppHeader_header__link_active__"
                                   "1IkJo' and @href = '/']"]
    # Лента заказов
    ORDER_FEED = [By.XPATH, ".//li[@class = 'undefined ml-2']/a"]
    # Лента заказов в активном состоянии
    ORDER_FEED_ACTIV = [By.XPATH, ".//a[@class = 'AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo' "
                                  "and @href = '/feed']"]
    # Элемент булок
    ELEMENT_BREAD = [By.XPATH, ".//img[@alt = 'Краторная булка N-200i']"]
    # Модальное окно с деталями
    MODAL_WINDOW_DETAILS = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div/div/p"]
    # Крестик для закрытия в модальном окне с деталями
    CLOSE_WINDOW_DETAILS = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div/button"]
    # Локатор закрытия модального окна с деталями
    AFTER_CLOSE_WINDOW_DETAILS = [By.XPATH, ".//section[@class = 'Modal_modal__P3_V5']/div/div[@class = 'Modal_modal__"
                                            "contentBox__sCy8X pt-10 pb-15']"]
    # Раздел "Соусы"
    SECTION_SAUCES = [By.XPATH, ".//span[text() = 'Соусы']"]
    # Элемент раздела "Соусы"
    ELEMENT_SAUCES = [By.XPATH, ".//img[@alt = 'Соус традиционный галактический']"]
    # Корзина
    BASKET = [By.XPATH, ".//section[@class = 'BurgerConstructor_basket__29Cd7 mt-25 ']"]
    # Счетчик ингредиента
    COUNTER_INGREDIENT = [By.XPATH, ".//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa74']/div/p[@class = "
                                    "'counter_counter__num__3nue1']"]
    # Кнопка "Оформить заказ"
    SET_ORDER_BUTTON = [By.XPATH, ".//button[text() = 'Оформить заказ']"]
    # Модальное окно с деталями
    MODAL_WINDOW_ID_ORDER = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
                                       "/div/div[@class = 'Modal_modal__contentBox__sCy8X pt-30 pb-30']"]
    # Крестик для закрытия модального окна с деталями заказа
    MODAL_WINDOW_ID_ORDER_CLOSE = [By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__"
                                             "close__TnseK']"]
    # ID заказа из модального окна
    ID_ORDER = [By.XPATH, ".//div[@class = 'Modal_modal__contentBox__sCy8X pt-30 pb-30']/h2"]
