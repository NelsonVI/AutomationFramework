from src.locators import LocatorsCheckOut
from pages.basic_page import BasicPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class CheckOutPage(BasicPage):
    def __init__(self, driver):
        self.locator = LocatorsCheckOut
        super().__init__(driver)

    def complete_CheckOutPage(self):
        self.data_pax()
        self.data_contact()
        self.data_payment()

    def data_pax(self):
        InputNameAdult = self.find_element(*self.locator.INPUT_NAME_ADULT)
        InputLastNameAdult = self.find_element(*self.locator.INPUT_LASTNAME_ADULT)
        IdNumber = self.find_element(*self.locator.INPUT_ID_NUMBER)
        BirthDay = Select(self.find_element(*self.locator.SELECT_BIRTH_DAY))
        BirthMonth = Select(self.find_element(*self.locator.SELECT_BIRTH_MONTH))
        BithYear = Select(self.find_element(*self.locator.SELECT_BIRTH_YEAR))
        GenderAdult = self.find_element(*self.locator.GENDER_MALE_PAX)
        self.send_keys_element(InputNameAdult, "Pepe")
        self.send_keys_element(InputLastNameAdult, "Nada")
        self.send_keys_element(IdNumber, "23125645")
        try:
            BirthDay.select_by_value("12")
            BirthMonth.select_by_visible_text("enero")
            BithYear.select_by_value("1985")
        except:
            print('\nOn national flight isn´t mandatory to complete the date of birth')

        self.click_element(GenderAdult)

    def data_contact(self):
        InputContactName = self.find_element(*self.locator.INPUT_CONTACT_NAME)        
        InputContactLastName = self.find_element(*self.locator.INPUT_CONTACT_LASTNAME)
        InputContactEmail = self.find_element(*self.locator.INPUT_CONTACT_EMAIL)
        InputContactCodeAreaPhone = self.find_element(*self.locator.INPUT_CONTACT_CODEAREA)
        InputContactPhone = self.find_element(*self.locator.INPUT_CONTACT_PHONE)
        InputContactName.clear()
        self.send_keys_element(InputContactName, "Ramon")
        InputContactLastName.clear()
        self.send_keys_element(InputContactLastName, "Valdez")
        self.send_keys_element(InputContactEmail, "test@test.com")
        self.send_keys_element(InputContactCodeAreaPhone, "011")
        self.send_keys_element(InputContactPhone, "15748596")
    
    def data_payment(self, payment="Credit Card"):
        if(payment == "Credit Card"):           
            self.payment_with_credit_card()
        elif(payment == "Telephone"):
            self.paymente_with_telephone()    
        elif(payment == "Bank Transfer"):
            self.payment_with_bank_transfer()
        elif(payment == "Pago Mis Cuentas"):
            self.paymente_with_pago_mis_cuentas()    
        else:
            print("No available payment")

    def paymente_with_pago_mis_cuentas(self):
        PaymentMethod = self.find_element(*self.locator.PAYMENT_BY_PAGO_MIS_CUENTAS)
        TermsAndConditions = self.find_element(*self.locator.CHECK_ACCEPT_TERMS)
        self.click_element(PaymentMethod)
        self.click_element(TermsAndConditions)    
    
    def payment_with_bank_transfer(self):
        PaymentMethod = self.find_element(*self.locator.PAYMENT_BY_TRANSFER)
        TermsAndConditions = self.find_element(*self.locator.CHECK_ACCEPT_TERMS)
        self.click_element(PaymentMethod)
        self.click_element(TermsAndConditions)

    def paymente_with_telephone(self):
        PaymentMethod = self.find_element(*self.locator.PAYMENT_BY_TELEPHONE)
        self.click_element(PaymentMethod)
        TermsAndConditions = self.find_element(*self.locator.CHECK_ACCEPT_TERMS)
        self.click_element(TermsAndConditions)

    def payment_with_credit_card(self):
        PaymentMethod = self.find_element(*self.locator.PAYMENT_CREDIT_CARD)
        CardType = self.driver.find_element(*self.locator.CARD_TYPE)
        self.click_element(PaymentMethod)
        self.click_element(CardType)
        BankName = self.find_element(*self.locator.BANK_NAME)
        self.click_element(BankName)
        self.data_credit_card()

    def data_credit_card(self):
        InstallmentsOne = self.find_element(*self.locator.INSTALLMENTS)
        InputCreditCardNumber = self.find_element(*self.locator.INPUT_CREDIT_CARD_NUMBER)
        InputCodeCreditCardNumber = self.find_element(*self.locator.INPUT_SEC_CODE_CARD_NUMBER)
        ExpiryMonthDateCreditCard = Select(self.find_element(*self.locator.SELECT_EXPIRY_DATE_CARD_MONTH))
        ExpiryYearDateCreditCard = Select(self.find_element(*self.locator.SELECT_EXPIRY_DATE_CARD_YEAR))
        InputOwnerFullNameCreditCard = self.find_element(*self.locator.INPUT_FULL_NAME_OWNER_CREDIT_CARD)
        InputOwnerIdCreditCard = self.find_element(*self.locator.INPUT_ID_NUMBER_OWNER_CREDIT_CARD)
        GenderOwnerCreditCard = self.find_element(*self.locator.GENDER_MALE_OWNER_CREDIT_CARD)
        BirthDayOwnerCreditCard = Select(self.find_element(*self.locator.SELECT_BIRTH_DAY_OWNER_CREDIT_CARD))
        BirthMonthOwnerCreditCard = Select(self.find_element(*self.locator.SELECT_BIRTH_MONTH_OWNER_CREDIT_CARD))
        BirthYearOwnerCreditCard = Select(self.find_element(*self.locator.SELECT_BIRTH_YEAR_OWNER_CREDIT_CARD))
        AddressOwnerCreditCard = self.find_element(*self.locator.INPUT_ADRESS_OWNER_CREDIT_CARD)
        StateOwnerCreditCard = Select(self.find_element(*self.locator.SELECT_STATE_OWNER_CREDIT_CARD))
        TermsAndConditions = self.find_element(*self.locator.CHECK_ACCEPT_TERMS)
        self.click_element(InstallmentsOne)
        self.send_keys_element(InputCreditCardNumber, "4024007117003128")
        self.send_keys_element(InputCodeCreditCardNumber, "123")
        ExpiryMonthDateCreditCard.select_by_visible_text("11")
        ExpiryYearDateCreditCard.select_by_visible_text("23")
        self.send_keys_element(InputOwnerFullNameCreditCard, "Mario Monticello")
        self.send_keys_element(InputOwnerIdCreditCard, "231589")
        self.click_element(GenderOwnerCreditCard)
        BirthDayOwnerCreditCard.select_by_value("10")
        BirthMonthOwnerCreditCard.select_by_visible_text("enero")
        BirthYearOwnerCreditCard.select_by_value("1985")
        self.send_keys_element(AddressOwnerCreditCard, "742 Evergreen Terrace")
        StateOwnerCreditCard.select_by_visible_text("Buenos Aires")
        self.click_element(TermsAndConditions)
