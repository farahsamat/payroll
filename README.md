# PAYROLL APP
The task is to build a payroll app that can generate and display employee monthly payslip, pay employee salary and update records so that are no redundant payments. This app can also display the overall payroll record for the current month.

## Getting Started
* Ensure Python 3 is [installed](https://www.python.org/downloads/).
* Clone this repository: `git clone https:://github.com/farahsamat/payroll.git`
## Running tests
On the terminal, run: `python -m unittest`

We mainly test for the income tax calculation module, ensuring it returns the right figure according to the income brackets. 


## Using the app
Run `python main_app.py` on CLI.

When the app is run, the app main menu will be displayed on the terminal.
![menu](https://github.com/farahsamat/payroll/blob/master/images/main_menu.png)

To generate and view employee payslip, choose option 2.
![option2](https://github.com/farahsamat/payroll/blob/master/images/gen_payslip.png)

![payslip](https://github.com/farahsamat/payroll/blob/master/images/payslip.png)

The input is stored in the monthly payroll record. Choose option 1 to view the record.
![option1](https://github.com/farahsamat/payroll/blob/master/images/view_payroll.png)

To pay a salary, choose option 3. User will be asked to enter the respective `employee ID` and confirm payment action (`Y/N`).
![option3](https://github.com/farahsamat/payroll/blob/master/images/pay_employee.png)

To verify the payment, choose option 1. The `pay_status` for `Jane Doe` has now been updated to `'paid'`
![paid](https://github.com/farahsamat/payroll/blob/master/images/paid.png)



## Future work
1) Ideally we want to have an automatic unique employee ID generator, but for the project demo purposes we generate unique employee IDs manually.
2) We would like build the app using a different framework instead of Python.
3) We assume there are no typos in salary/super input which could cause error in calculations.
