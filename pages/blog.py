class blog_cls:
    def __init__(self,page):
        self.page=page
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]').click()
        self.page.wait_for_timeout(2000)
        self.contact_us=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]').click()
        self.page.wait_for_timeout(2000)
        
        self.firstname=page.locator('(//input[@placeholder="Your Name"])[2]').fill('xxx')
        self.email=page.locator('(//input[@placeholder="Your Mail"])[2]').fill('abc@a.com')
        self.otp=page.locator('(//button[@type="button"])[2]').click()
        self.otp1=page.locator('(//input[@placeholder="Enter OTP"])[2]').fill('123')
        self.Company=page.locator('(//input[@placeholder="Your Company"])[2]').fill('uncodemy')
        self.service=page.locator('(//select[@name="service"])[2]').select_option(label='Web Development')
        self.phno=page.locator('(//input[@placeholder="Your Phone"])[2]').fill('1234567890')
        self.message=page.locator('(//textarea[@placeholder="Message"])[2]').fill('Good morning')
        self.submit=page.locator('(//input[@value="Submit"])[2]').click()
        self.page.wait_for_timeout(5000)