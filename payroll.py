class EmployeeDetails:
    def __init__(self, first_name='', last_name='', annual_rate=0, super_rate=0):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_rate = annual_rate
        self.super_rate = super_rate
        return

    def user_input(self, first, last, annual_salary, super_rate):
        self.first_name = first
        self.last_name = last
        self.annual_rate = annual_salary
        self.super_rate = super_rate

    def generate_employee_id(self):
        l = self.last_name.lower()
        f = self.first_name.lower()
        e_id = f+l
        return e_id

    def gross_income(self):
        return self.annual_rate/12

    def income_tax(self):
        if self.annual_rate >= 18201 and self.annual_rate <= 37000:
            return 0.19*(self.annual_rate-18200)/12
        elif self.annual_rate >= 37001 and self.annual_rate <= 80000:
            return (3572 + 0.325*(self.annual_rate-37000))/12
        elif self.annual_rate >= 80001 and self.annual_rate <= 180000:
            return (17547 + 0.37*(self.annual_rate-80000))/12
        elif self.annual_rate >= 180001:
            return (54547 + 0.45*(self.annual_rate-180000))/12
        else:
            return 0



