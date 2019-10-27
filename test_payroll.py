import unittest
from payroll import EmployeeDetails

class PayrollTest(unittest.TestCase):
    def test_print_correct_user_input(self):
        emp = EmployeeDetails('John', 'Doe', 10000, 9)
        self.assertEqual(emp.first_name, 'John')
        self.assertEqual(emp.last_name, 'Doe')
        self.assertEqual(emp.annual_rate, 10000)
        self.assertEqual(emp.super_rate, 9)

    def test_generate_employee_id(self):
        emp = EmployeeDetails('Jo', 'Ngang', 120000, 9)
        self.assertEqual(emp.generate_employee_id(), 'jongang')

    def test_calculate_correct_gross_income_rounded_to_the_nearest_dollar(self):
        emp = EmployeeDetails('Jane', 'Doe', 120000, 9)
        self.assertEqual(round(emp.gross_income()), 10000)

    def test_calculate_income_tax_for_15000_salary_return_zero(self):
        emp = EmployeeDetails('Jane', 'Doe', 15000, 9)
        self.assertEqual(emp.income_tax(), 0)

    def test_calculate_income_tax_for_30000_salary_rounded_to_the_nearest_dollar(self):
        emp = EmployeeDetails('Jane', 'Doe', 30000, 9)
        self.assertEqual(round(emp.income_tax()), 187)

    def test_calculate_income_tax_for_60050_salary_rounded_to_the_nearest_dollar(self):
        emp = EmployeeDetails('Jane', 'Doe', 60050, 9)
        emp.income_tax()
        self.assertEqual(round(emp.income_tax()), 922)

    def test_calculate_income_tax_for_115000_salary_rounded_to_the_nearest_dollar(self):
        emp = EmployeeDetails('Jane', 'Doe', 115000, 9)
        emp.income_tax()
        self.assertEqual(round(emp.income_tax()), 2541)

    def test_calculate_income_tax_for_250000_salary_rounded_to_the_nearest_dollar(self):
        emp = EmployeeDetails('Jane', 'Doe', 250000, 9)
        emp.income_tax()
        self.assertEqual(round(emp.income_tax()), 7171)

