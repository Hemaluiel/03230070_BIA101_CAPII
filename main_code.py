
#main code
class Employee:
    def __init__(self, name, age, organization_type, marital_status, employee_type):
        self.name = name
        self.age = age
        self.organization_type = organization_type
        self.employee_type = employee_type
        self.marital_status = marital_status
        if marital_status.lower() == "married":
            self.num_children = self.get_num_children()
        else:
            self.num_children = 0

    def get_num_children(self):
        while True:
            try:
                return int(input("Enter the number of your children: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

print("Personal Income Tax (PIT) Calculator")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# To if age is below 18, if so, user does not have to calcutale PIT and exit the program
if age < 18:
    print("You are below 18 years old. You are not required to pay taxes.")
    exit()

marital_status = input("Enter your marital status (Married/Single): ")
organization_type = input("Enter the organization type (Government/Private): ")
employee_type = input("Enter the employee type (Regular/Contract): ")


class TaxCalculator:
    def __init__(self, income, gis_contributions, life_insurance_premium, self_education_allowance, donations, bonus_amount, employee_type, organization_type):
        self.income = income
        self.gis_contributions = gis_contributions
        self.life_insurance_premium = life_insurance_premium
        self.self_education_allowance = self_education_allowance
        self.donations = donations
        self.bonus_amount = bonus_amount
        self.pf_contributions = 0 if employee_type.lower() == "contract" and organization_type.lower() == "government" else gis_contributions

    def calculate_tax(self, num_children):
        total_income = self.income

        # Deduct PF and GIS contributions
        total_income -= self.pf_contributions
        total_income -= self.gis_contributions

        child_edu_allowances = []
        sponsored_edu_expenses = []

        for child in range(num_children):
            child_edu_allowance = float(input(f"Enter education allowance for child {child + 1} (max Nu. 350,000): "))
            child_edu_allowances.append(min(child_edu_allowance, 350000))

            goes_to_school = input(f"Does your child {child + 1} go to school? (y/n): ").lower()
            if goes_to_school == "y":
                sponsored_edu_expense = float(input(f"Enter your sponsored education expense for your child {child + 1} (max Nu. 350,000): "))
                sponsored_edu_expenses.append(min(sponsored_edu_expense, 350000))
            else:
                sponsored_edu_expenses.append(0)

        # Apply general deductions
        total_income -= sum(child_edu_allowances)
        total_income -= self.life_insurance_premium
        total_income -= min(self.self_education_allowance, 350000)
        total_income -= min(self.donations, 0.05 * total_income)
        total_income -= sum(sponsored_edu_expenses)
        total_income -= self.bonus_amount

        # Apply tax slabs
        tax_amount = 0
        if total_income <= 300000:
            tax_amount = 0
        elif total_income <= 400000:
            tax_amount = (total_income - 300000) * 0.1
        elif total_income <= 650000:
            tax_amount = (total_income - 400000) * 0.15 + 10000
        elif total_income <= 1000000:
            tax_amount = (total_income - 650000) * 0.2 + 45500
        elif total_income <= 1500000:
            tax_amount = (total_income - 1000000) * 0.25 + 130500
        else:
            tax_amount = (total_income - 1500000) * 0.3 + 280500

        # Apply surcharge if applicable
        if total_income >= 1000000:
            tax_amount += tax_amount * 0.1

        return tax_amount

income = float(input("Enter your annual gross salary: "))
gis_contributions = float(input("Enter your GIS contributions: "))
life_insurance_premium = float(input("Enter your life insurance premium: "))
self_education_allowance = float(input("Enter your self education allowance, if any: "))
donations = float(input("Enter your donations (if any): "))
bonus_amount = float(input("Enter your bonus amount : "))

num_children = Employee(name, age, organization_type, marital_status, employee_type).num_children if marital_status.lower() == "married" else 0

tax_calculator = TaxCalculator(income, gis_contributions, life_insurance_premium, self_education_allowance, donations, bonus_amount, employee_type, organization_type)
tax_amount = tax_calculator.calculate_tax(num_children)
print("Your tax amount is:", tax_amount)
