from selenium.webdriver.common.by import By


class HeaderLocators(object):
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign In")
    IMAGE_CART = (By.NAME, "img_cart")
    IMAGE_LOGO = (By.XPATH, "//*[@id='LogoContent']/a/img")
    HELP_LINK = (By.LINK_TEXT, "?")
    SEARCH_BOX = (By.NAME, "keyword")
    SEARCH_BUTTON = (By.NAME, "searchProducts")
    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My Account")
    FISH_LINK = (By.XPATH, "//img[@src='../images/sm_fish.gif']")
    DOGS_LINK = (By.XPATH, "//img[@src='../images/sm_dogs.gif']")
    REPTILES_LINK = (By.XPATH, "//img[@src='../images/sm_reptiles.gif']")
    CATS_LINK = (By.XPATH, "//img[@src='../images/sm_cats.gif']")
    BIRDS_LINK = (By.XPATH, "//img[@src='../images/sm_birds.gif']")


class SignInPageLocators(object):
    USER_NAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "signon")
    REGISTER_LINK = (By.LINK_TEXT, "Register Now!")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='Content']/ul[@class='messages']/li")


class RegisterPageLocators(object):
    USER_ID_FIELD = (By.NAME, "username")
    NEW_PASSWORD_FIELD = (By.NAME, "password")
    REPEATED_PASSWORD_FIELD = (By.NAME, "repeatedPassword")
    FIRST_NAME_FIELD = (By.NAME, "account.firstName")
    LAST_NAME_FIELD = (By.NAME, "account.lastName")
    EMAIL_FIELD = (By.NAME, "account.email")
    PHONE_FIELD = (By.NAME, "account.phone")
    ADDRESS1_FIELD = (By.NAME, "account.address1")
    ADDRESS2_FIELD = (By.NAME, "account.address2")
    CITY_FIELD = (By.NAME, "account.city")
    STATE_FIELD = (By.NAME, "account.state")
    ZIP_FIELD = (By.NAME, "account.zip")
    COUNTRY_FIELD = (By.NAME, "account.country")
    LANGUAGE_PREFERENCE_SELECT_LIST = (By.NAME, "account.languagePreference")
    FAVOURITE_CATEGORY_SELECT_LIST = (By.NAME, "account.favouriteCategoryId")
    ENABLE_MY_LIST_CHECKBOX = (By.NAME, "account.listOption")
    ENABLE_MY_BANNER_CHECKBOX = (By.NAME, "account.bannerOption")
    NEW_ACCOUNT_BUTTON = (By.NAME, "newAccount")


class AddressPageLocators(object):
    SHIP_FIRST_NAME_FIELD = (By.NAME, "order.shipToFirstName")
    SHIP_LAST_NAME_FIELD = (By.NAME, "order.shipToLastName")
    SHIP_ADDRESS1_FIELD = (By.NAME, "order.shipAddress1")
    SHIP_ADDRESS2_FIELD = (By.NAME, "order.shipAddress2")
    SHIP_CITY_FIELD = (By.NAME, "order.shipCity")
    SHIP_STATE_FIELD = (By.NAME, "order.shipState")
    SHIP_ZIP_FIELD = (By.NAME, "order.shipZip")
    SHIP_COUNTRY_FIELD = (By.NAME, "order.shipCountry")


class CartPageLocators(object):
    CART_PAGE_DIV = (By.ID, "Cart")
    UPDATE_CART_BUTTON = (By.NAME, "updateCartQuantities")
    CHECK_OUT_BUTTON = (By.LINK_TEXT, "Proceed to Checkout")
    REMOVE_BUTTON = (By.LINK_TEXT, "Remove")


class CategoryPageLocators(object):
    RETURN_TO_HOMEPAGE_BUTTON = (By.LINK_TEXT, "Return to Main Menu")


class ConfirmPageLocators(object):
    CONFIRM_BUTTON = (By.LINK_TEXT, "Confirm")


class FooterPageLocators(object):
    POWERED_BY_LINK = (By.LINK_TEXT, "www.mybatis.org")


class HomePageLocators(object):
    HOME_PAGE_DIV = (By.ID, "Main")


class ItemPageLocators(object):
    ADD_TO_CART_BUTTON = (By.LINK_TEXT, "Add to Cart")


class MyAccountLocators(object):
    NEW_PASSWORD_FIELD = (By.NAME, "password")
    REPEATED_PASSWORD_FIELD = (By.NAME, "repeatedPassword")
    FIRST_NAME_FIELD = (By.NAME, "account.firstName")
    LAST_NAME_FIELD = (By.NAME, "account.lastName")
    EMAIL_FIELD = (By.NAME, "account.email")
    PHONE_FIELD = (By.NAME, "account.phone")
    ADDRESS1_FIELD = (By.NAME, "account.address1")
    ADDRESS2_FIELD = (By.NAME, "account.address2")
    CITY_FIELD = (By.NAME, "account.city")
    STATE_FIELD = (By.NAME, "account.state")
    ZIP_FIELD = (By.NAME, "account.zip")
    COUNTRY_FIELD = (By.NAME, "account.country")
    LANGUAGE_PREFERENCE_SELECT_LIST = (By.NAME, "account.languagePreference")
    FAVOURITE_CATEGORY_SELECT_LIST = (By.NAME, "account.favouriteCategoryId")
    ENABLE_MY_LIST_CHECKBOX = (By.NAME, "account.listOption")
    ENABLE_MY_BANNER_CHECKBOX = (By.NAME, "account.bannerOption")
    EDIT_ACCOUNT_BUTTON = (By.NAME, "editAccount")
    MY_ORDERS_LINK = (By.LINK_TEXT, "My Orders")


class PaymentPageLocators(object):
    CARD_TYPE_SELECT_LIST = (By.NAME, "order.cardType")
    CREDIT_CARD_NUMBER_FIELD = (By.NAME, "order.creditCard")
    EXPIRY_DATE_FIELD = (By.NAME, "order.expiryDate")
    BILL_FIRST_NAME_FIELD = (By.NAME, "order.billToFirstName")
    BILL_LAST_NAME_FIELD = (By.NAME, "order.billToLastName")
    BILL_ADDRESS1_FIELD = (By.NAME, "order.billAddress1")
    BILL_ADDRESS2_FIELD = (By.NAME, "order.billAddress2")
    BILL_CITY_FIELD = (By.NAME, "order.billCity")
    BILL_STATE_FIELD = (By.NAME, "order.billState")
    BILL_ZIP_FIELD = (By.NAME, "order.billZip")
    BILL_COUNTRY_FIELD = (By.NAME, "order.billCountry")
    SHIPPING_TO_DIFFERENT_ADDRESS_CHECKBOX = (By.NAME, "shippingAddressRequired")
    CONTINUE_BUTTON = (By.NAME, "newOrder")


class ProductPageLocators(object):
    RETURN_TO_CATEGORY_PAGE_LINK = (By.PARTIAL_LINK_TEXT, "Return to")


class SearchPageLocators(object):
    CATALOG_DIV = (By.ID, "Catalog")
