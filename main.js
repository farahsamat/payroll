function calculate_tax(annual_salary) {
		if (annual_salary >= 18201 && annual_salary <= 37000){
				return Math.round(0.19*(annual_salary-18200)/12);
			}
			else if(annual_salary >= 37001 && annual_salary <= 80000){
				return Math.round((3572 + 0.325*(annual_salary-37000))/12);
			}
			else if(annual_salary >= 80001 && annual_salary <= 180000){
				return Math.round((17547 + 0.37*(annual_salary-80000))/12);
			}
			else if(annual_salary >= 180001){
				return Math.round((54547 + 0.45*(annual_salary-180000))/12);
			}
			else {
				return 0;
			}
		}
	
	 function view_payslip() {
		var first_name = (document.getElementById("first_name").value).toUpperCase();
		var last_name = (document.getElementById("last_name").value).toUpperCase();
		var annual_rate = document.getElementById("annual_rate").value;
		var gross_income = Math.round(annual_rate/12);
		var income_tax = Math.round(0.3*gross_income);
		var net_income = gross_income-income_tax;
		var super_amount = Math.round((document.getElementById("super_rate").value)/100*net_income);
	 	var pay = net_income-super_amount;
		 
	 	field1 = "Employee's Name : " + first_name + " " + last_name;
		field2 ="Annual Income : $" + annual_rate;
		field3 ="Gross Income : $" + gross_income;
		field4 ="Income tax: $" + income_tax; 	
		field5 ="Net Income : $" + net_income;
		field6 ="Super : $" + super_amount; 
		field7 ="Pay : $" + pay;
		field8 ="Status: "; 
		
	 	document.getElementById("field1").innerHTML = field1;
		document.getElementById("field2").innerHTML = field2;
		document.getElementById("field3").innerHTML = field3;	
		document.getElementById("field4").innerHTML = field4; 
		document.getElementById("field5").innerHTML = field5;
		document.getElementById("field6").innerHTML = field6;
		document.getElementById("field7").innerHTML = field7;	
		document.getElementById("field8").innerHTML = field8; 
	 }