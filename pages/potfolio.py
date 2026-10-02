class portfolio_cls:
    def __init__(self,page):
        self.page=page
        self.var_portfolio=page.locator('(//a[@href="https://www.tranktechnologies.com/portfolio"])[1]').click()
        self.ics_homework=page.locator('(//a[@href="https://www.icshomework.in/"])[1]')
        self.Wings_Pharma=page.locator('(//a[@href="https://www.wingspharma.com/"])[1]')
        self.Arena_Animation=page.locator('(//a[@href="https://arenasonipat.com/"])[1]')
        self.Home=page.locator('(//a[@href="https://home360stores.com/"])[1]')
        self.Cords=page.locator('(//a[@href="https://cordscable.tranktechnologies.com/"])[1]')



        