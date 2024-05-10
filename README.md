# BIA101 CAP II
# PIT(Personal Income Tax) CALCULATOR APPLICATION

## submission By Hema Luitel, 03230070

This Python code is a simplified personal income tax (PIT) calculator. It allows users to input various financial details such as income, deductions, and allowances, and calculates their tax liability based on Bhutanese tax laws. Here's a breakdown of how the code works:

1.  Employee Class: It defines an 'Employee' class to store employee details like name, age, marital status, organization type, and employee type. It also calculates the number of children if the employee is married.

2. TaxCalculator Class: This class is responsible for computing the tax amount based on the provided financial details and employee information. It takes into account various deductions and tax slabs specified by Bhutanese tax regulations.

3. Input Gathering: The program prompts the user to enter their personal and financial details such as name, age, marital status, organization type, employee type, income, GIS contributions, life insurance premium, self-education allowance, donations, and bonus amount.

4. Tax Calculation: After gathering all necessary inputs, the code instantiates a 'TaxCalculator' object with the provided financial details and calculates the tax amount using the 'calculate_tax' method.

5. Output: Finally, the program displays the calculated tax amount to the user.

This code helps individuals estimate their personal income tax liability based on their financial situation, providing transparency and clarity regarding their tax obligations.