from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    ELEMENT_ORDERS_FEED = [By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']/li[1]"]
    WINDOW_DETAILS_ORDER = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div"
                                      "/div[@class = 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"]
    TOTAL_ALL = [By.XPATH, "//div[@class = 'undefined mb-15']/p[@class = 'OrderFeed_number__2MbrQ text text_type_"
                           "digits-large']"]
    ORDER_IN_WORK = [By.XPATH, ".//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/"
                               "li[@class = 'text text_type_digits-default mb-2']"]
    ELEMENT_IN_FEED = [By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']/li[1]/a/div/p[@class = "
                                 "'text text_type_digits-default']"]
    TOTAL_TODAY = [By.XPATH, ".//div[not(@class)]/p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']"]
