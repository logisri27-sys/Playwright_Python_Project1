class vertical_cls:
    def __init__(self,page):

        self.page=page
        #Verticals
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')

        #Trading
        self.Trading=page.locator('//strong[text()="Trading"]')

        #trading option
        self.StockTrading= page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.PaperTrading= page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.CFDTrading= page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.TradingApp_Development=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.Algotrading=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.Custom_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.Webportal_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.Tradinglist=[self.StockTrading,self.PaperTrading,self.CFDTrading,self.TradingApp_Development,self.Algotrading,self.Custom_trading,self.Webportal_trading]

        #Retail and commerce
        self.Retail_and_Commerce=page.locator('//strong[text()="Retail and Ecommerce"]')
 #      ecommerce_webpage_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        
        #retail commerce option
        self.ecommerce_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.Retail_list=[self.ecommerce_app_development]

        # Healthcare 
        self.Healthcare=page.locator('//strong[text()="Healthcare"]')

        # Heathcare options
        self.Diet_nutritions=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.Health_tracking=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.healthcare_list=[self.Diet_nutritions,self.Health_tracking]

        #Fintech
        self.Fintech=page.locator('//strong[text()="Fintech"]')

        #Fintech options
        self.pos_and_software=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.Crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.fintech_list=[self.pos_and_software,self.Crypto]



    def Clicking_trading_options(self):
        for i in self.Tradinglist:
            self.vertical.hover()
            self.Trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def Retail_options(self):
        for i in self.Retail_list:
            self.vertical.hover()
            self.Retail_and_Commerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def heathcare_options(self):
        for i in self.healthcare_list:
            self.vertical.hover()
            self.Healthcare.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def fintech_options(self):
        for i in self.fintech_list:
            self.vertical.hover()
            self.Fintech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def get_free_demo(self):
        # self.getfreedemo=self.page.locator('(//a[text()="Get a Free Quote"])[1]').click()
        # self.name=self.page.locator('//input[@placeholder="Your Name"]').fill("Name1")
        # self.mail=self.page.locator('//input[@placeholder="Your Mail"]').fill("abc@a.com")
        # self.otp=self.page.locator('//button[@onclick="sendcareersOTP()"]').click()
        # self.otp1=self.page.locator('//input[@placeholder="Enter OTP"]')
        # self.company=self.page.locator('//input[@placeholder="Your Company"]').fill("uncodemy")
        # self.service=self.page.locator('//select[@name="service"]').select_option("Web Development")
        # self.phone=self.page.locator('//input[@placeholder="Your Phone"]').fill("1234567890")
        # self.message=self.page.locator('//textarea[@placeholder="Message"]').fill("Good morning")
        # # self.recaptcha=self.page.locator('//span[@id="recaptcha-anchor"]').click()
        # # self.submit=self.page.locator('//input[@value="Submit"]').click()
        # self.close=self.page.locator('//div[@class="cm-close-btn"]').click()
        # self.page.wait_for_load_state("load")
#        self.country=self.page.locator('//select[@id="countrySelector"]').select_option("india")
        self.country = self.page.locator('//select[@id="countrySelector"]')
        self.country.select_option("india")

        self.page.wait_for_timeout(5000)
