class Technologies_cls:
    def __init__(self,page):
        self.page=page

        #Technologies
        self.Technologies = page.locator('(//a[text()="Technologies"])[1]')

        #technologies options1
        self.eCommerce_Development = page.locator('(//strong[text()="eCommerce Development"])[1]')

        #technologies_Ecommerce options
        self.Magneto = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.Codeigniter_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.BigCommerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.CS_Cart_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.Nop_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.Opencart_Devlopment = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.Wordpress_devlopment = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.Shopify_Devlopment = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.nodejs_devlopment = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.woo_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')

        #technologies options2
        self.Mobile_app = page.locator('(//strong[text()="Mobile App Development"])[1]')

         #technologies Mobile_app options
        self.React_native = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarin = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutter = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swiftapp = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.enterprise = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlin = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.iconic = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.Appointment = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

        #technologies options3
        self.ai = page.locator('//strong[text()="Artificial Intelligence"]')
        #ecommerce list
        self.ecommerce_list = [
            self.Magneto,
            self.Codeigniter_Development,
            self.BigCommerce,
            self.CS_Cart_Development,
            self.Nop_Commerce,
            self.Opencart_Devlopment,
            self.Wordpress_devlopment,
            self.Shopify_Devlopment,
            self.nodejs_devlopment,
            self.woo_commerce
        ]

        #Mobile list
        self.Mobile_app_list=[self.React_native,self.xamarin,self.flutter,self.swiftapp,self.enterprise,self.kotlin,self.iconic,self.Appointment]

    def ecommerce_options(self):
        for i in self.ecommerce_list:
            self.Technologies.hover()
            self.eCommerce_Development.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        self.page.wait_for_timeout(5000)


    def Mobile_app_options(self):
        for i in self.Mobile_app_list:
            self.Technologies.hover()
            self.Mobile_app.hover()
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        self.page.wait_for_timeout(5000)

    def ai_options(self):
        self.Technologies.hover()
        self.ai.hover()