class devlopment_cls:
    def __init__(self,page):
        self.page=page

        #Web devlopment options
        self.CMS_Website_Development =page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.Custom_Web_Portal_Development =page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        #Web devlopment list
        self.Web_Development_list=[self.CMS_Website_Development,self.Custom_Web_Portal_Development]

        # UI/UX design options
        self.Mobile_App_Design =page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.Responsive_Web_Design =page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.Brand_Identity_Design =page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')

        #UI/UX design list
        self.UI_UX_Design_list=[self.Mobile_App_Design,self.Responsive_Web_Design,self.Brand_Identity_Design]

        #app devlopment options
        self.iOS_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        # Android_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        #  app_devlopment=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.Hybrid_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"])')
        self.Cross_Platform_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"])')
        self.Progressive_Web_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"])')

        # app devlopment list
        self.app_devlopment_list=[self.iOS_App_Development,self.Hybrid_Mobile_App_Development,self.Cross_Platform_App_Development,self.Progressive_Web_App_Development]

        #Graphic design options
        self.Logo_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/logo-design-company"])')
        self.Banner_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/banner-design-company"])')
        self.Packaging_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/packaging-design-company"])')
        self.Business_cards_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/business-cards-design-company"])')

        #graphic design list
        self.Graphic_Design_list=[self.Logo_Design,self.Banner_Design,self.Packaging_Design,self.Business_cards_Design]

        #Social media locator
        self.about=page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        self.facebook=page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkedin=page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.insta=page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pin=page.locator('//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.twitter=page.locator('//a[@href="https://twitter.com/tranktechno"]')
        self.youtube=page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"]')
        self.quora=page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')

        # social media list
        self.socialmediaList=[self.facebook,self.linkedin,self.insta,self.pin,self.twitter,self.youtube,self.quora]
    def web_Dev(self):
        for i in self.Web_Development_list:
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        self.page.wait_for_timeout(5000)

    def ui_ux(self):        
        for i in self.UI_UX_Design_list:
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        self.page.wait_for_timeout(5000)

    def app_Dev(self):
        for i in self.app_devlopment_list:
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        self.page.wait_for_timeout(5000)
    def graphic_design(self):
        for i in self.Graphic_Design_list:
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
        self.page.wait_for_timeout(5000)

    # def social_media(self):
    #     self.page.locator('(//a[@href="https://in.linkedin.com/company/trank-technologies-official"])').click()
    #     self.page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]').click()

    def socialmediapageclick(self):
        self.about.click()
        self.page.wait_for_load_state(state="load")
        
        for social_media_link in self.socialmediaList:
            with self.page.context.expect_page() as new_page_info:
                social_media_link.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()