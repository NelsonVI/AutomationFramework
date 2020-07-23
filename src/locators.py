from selenium.webdriver.common.by import By

class MainPageLocators():

    POPUP = (By.XPATH, "//*[@class='preloaded_lightbox']/div")
    FROM_CITY =By.XPATH, "//*[@id='__next']//div[1]/div/label/div/input" 
    TO_CITY = (By.XPATH, "//*[@id='__next']//div[2]/div/label/div/input")
    DEPARTURE_DATE = (By.ID, "startDate")
    ARRIVAL_DATE = (By.ID, "endDate")
    PAX_ADULT = (By.XPATH, "//*[@id='__next']//div[2]/div[2]/div/div/div")
    PAX_CHILD = (By.XPATH, "//*[@id='__next']//div[3]/div[3]/div/div/div")
    PAX_BABY = (By.XPATH, "//*[@id='__next']//div[4]/div[2]/div/div/div")
    SUBMIT_BTN = (By.CLASS_NAME, "hTioOs")

class LocatorsResultPage():

    LIST_CLUSTER = (By.CLASS_NAME, "jBsgBU")
    FOOTER = (By.CLASS_NAME, "bBTDSk")

class LocatorsCheckOut():

    INPUT_NAME_ADULT = (By.ID, "name")
    INPUT_LASTNAME_ADULT = (By.ID, "lastname")
    INPUT_ID_NUMBER = (By.ID, "pinNumber")
    SELECT_BIRTH_DAY = (By.CLASS_NAME, "day")
    SELECT_BIRTH_MONTH = (By.CLASS_NAME, "month")
    SELECT_BIRTH_YEAR = (By.CLASS_NAME, "year")
    GENDER_MALE_PAX = (By.ID, "genreMale[Adult][0]")
    GENDER_FEMALE_PAX = (By.ID, "genreFemale[Adult][0]")
    INPUT_CONTACT_NAME = (By.ID, "contactName")
    INPUT_CONTACT_LASTNAME = (By.ID, "contactLastName")
    INPUT_CONTACT_EMAIL = (By.ID, "contactEmail")
    INPUT_CONTACT_CODEAREA = (By.ID, "contactCodeArea")
    INPUT_CONTACT_PHONE = (By.ID, "contactPhone")
    PAYMENT_CREDIT_CARD = (By.ID, "paymentMethod_CreditCard")
    PAYMENT_BY_TELEPHONE = (By.ID, "paymentMethod_Telephone")
    PAYMENT_BY_TRANSFER = (By.ID, "paymentMethod_Transfer")
    PAYMENT_BY_PAGO_MIS_CUENTAS = (By.ID, "paymentMethod_PagoMisCuentas")
    CARD_TYPE = (By.XPATH, "//div[@id='creditCard']/label[@for='creditCard_0']")
    BANK_NAME = (By.XPATH, "//div[@class='av-fila-flex light']//div[@title='Banco Galicia']")
    INSTALLMENTS = (By.XPATH, "//label[@for='settlement_1']")
    INPUT_CREDIT_CARD_NUMBER = (By.ID, "cardNumber")
    INPUT_SEC_CODE_CARD_NUMBER = (By.ID, "securityCode")
    SELECT_EXPIRY_DATE_CARD_MONTH = (By.XPATH, "//*[@class='marco-vencimiento']//select[@class='month']")
    SELECT_EXPIRY_DATE_CARD_YEAR = (By.XPATH, "//*[@class='marco-vencimiento']//select[@class='year']")
    INPUT_FULL_NAME_OWNER_CREDIT_CARD = (By.ID, "holderName")
    INPUT_ID_NUMBER_OWNER_CREDIT_CARD = (By.ID, "holderPin")
    GENDER_MALE_OWNER_CREDIT_CARD = (By.ID, "genreMale")
    GENDER_FEMALE_OWNER_CREDIT_CARD = (By.ID, "genreFemale")
    SELECT_BIRTH_DAY_OWNER_CREDIT_CARD = (By.XPATH, "//div[@class='marco-input av-left marco-fecha holderB']//select[@class='day']")
    SELECT_BIRTH_MONTH_OWNER_CREDIT_CARD = (By.XPATH, "//div[@class='marco-input av-left marco-fecha holderB']//select[@class='month']")
    SELECT_BIRTH_YEAR_OWNER_CREDIT_CARD = (By.XPATH, "//div[@class='marco-input av-left marco-fecha holderB']//select[@class='year']")
    INPUT_ADRESS_OWNER_CREDIT_CARD = (By.ID, "street")
    SELECT_STATE_OWNER_CREDIT_CARD = (By.NAME, "holderState")
    CHECK_ACCEPT_TERMS = (By.XPATH, "//div[@class='av-checkbox terminos']/input")
    BUY_BUTTON = (By.XPATH, "//div[@class='buy-buttons']/button")

    