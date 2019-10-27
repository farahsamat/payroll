import os
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
from payroll import *

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Variables
cwd = os.getcwd()
current_year = datetime.now().year
current_month = datetime.now().month
#columns = ['last_name','first_name','emp_id','annual_salary','super','pay_status']
#data = pd.DataFrame(columns=columns)
#data.to_csv("{}/{}/{}/payroll.csv".format(cwd, current_year, current_month), index=False)

# Create main menu
main_menu = np.array(["View payroll data", "Generate payslip", "Pay", "Quit"])

def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print(" ")
            pass
    return num

def display_menu(options):
    print(" ")
    print("----------MAIN MENU-----------------")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i + 1, options[i]))

    option = 0
    while not (np.any(option == np.arange(len(options)) + 1)):
        option = input_number("Please choose your option: ")
        print(" ")
    return option


if __name__=="__main__":
    while True:
        choice = display_menu(main_menu)
        if choice == 1: # View records
            try:
                records = pd.read_csv("{}/{}/{}/payroll.csv".format(cwd, current_year, current_month))
                print(records)
            except ValueError:
                print("Invalid Input")

        elif choice == 2: #payslip
            try:
                last_name = input('Enter last name: ')
                first_name = input('Enter first name: ')
                emp_id = ''
                annual_rate = int(input('Enter annual rate: '))
                super_rate = int(input('Enter super rate: '))
                pay_status = ''

                view = EmployeeDetails(first_name, last_name, annual_rate, super_rate)
                annual_rate = view.annual_rate
                emp_id = view.generate_employee_id()

                gross_income = round(view.gross_income())
                income_tax = round(view.income_tax())
                net_income = gross_income - income_tax
                super_amount = round(gross_income * super_rate / 100)
                pay_amount = net_income - super_amount

                # generate payslip
                payslip_data =  [['Annual Income', annual_rate],
                                ['Gross Income', gross_income],
                                ['Income Tax', income_tax],
                                ['Net Income', net_income],
                                ['Super', super_amount],
                                ['Pay', pay_amount]]

                # view payslip
                payslip = pd.DataFrame(payslip_data, columns=['--{} {}--'.format(view.first_name.upper(), view.last_name.upper()),
                                                              '[{}/{}]'.format(current_month, current_year)])
                print("============================")
                print(payslip)
                print("============================")

                # append new data
                data = pd.read_csv("{}/{}/{}/payroll.csv".format(cwd, current_year, current_month))
                new_data = data.append(
                    pd.DataFrame([[last_name, first_name, emp_id, annual_rate, super_rate, pay_status]],
                                 columns=data.columns))
                new_data.to_csv("{}/{}/{}/payroll.csv".format(cwd, current_year, current_month), index=False)

            except ValueError:
                print("Invalid input")


        elif choice == 3: #pay
            try:
                new_data = pd.read_csv("{}/{}/{}/payroll.csv".format(cwd, current_year, current_month))
                emp_id = input("Enter employee ID: ")
                row_idx = new_data[new_data['emp_id'] == emp_id.lower()].index.item()
                emp_pay_status = new_data.iloc[row_idx, new_data.columns.get_loc('pay_status')]
                if emp_pay_status != 'paid':
                    pay = input('Pay employee: Y/N?')
                    if pay.upper() == 'Y':
                        new_data.loc[new_data.index[row_idx], 'pay_status'] = 'paid'
                        new_data.to_csv("{}/{}/{}/payroll.csv".format(cwd, current_year, current_month), index=False)
                    else:
                        print("Have a nice day!")
                else:
                    print("*****Employee has been paid for the month of {}/{}*****".format(current_month, current_year))

            except ValueError:
                print("Invalid input")


        elif choice == 4:
            break










