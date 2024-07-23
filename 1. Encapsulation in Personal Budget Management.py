# 1. Encapsulation in Personal Budget Management
# Objective: The aim of this assignment is to reinforce the 
# understanding of encapsulation in Python, 
# focusing on the use of private attributes and getters and setters.

#Problem Statement: You are required to build a 
# Personal Budget Management application. 
# The application will manage budget categories like food, 
# entertainment, utilities, etc., ensuring that budget details remain 
# private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class Create a class `BudgetCategory` 
# with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.

class BudgetCategory:
    def __init__(self, name, budget=0, budget_type=None):
        self.__category_name = name
        self.__allocated_budget = budget
        self.__remaining_budget = budget
        self.__budget_type = budget_type
        self.__expenses = []



# - Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters 
# - Write getter and setter methods for both the category name and the allocated budget. 
# - Ensure that the setter methods include validation (e.g., budget should be a positive number).

    def get_category(self):
        return self.__category_name
    
    def set_category(self, name):
        self.__category_name = ("Food")
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, budget):
        if budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget
        else:
            raise ValueError
        

# - Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task 3: Add Budget Functionality Implement a method to add 
# expenses to a category and adjust the budget accordingly. 
# - Validate the expense amount before making deductions from the budget.

    def add_expenses(self, amount):
        if amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
            self.__expenses.append(amount)
        else:
            raise ValueError("Expenses should be positive number.")
    


# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details Create a method to display the details of a 
# budget category, including the name, allocated budget, and remaining budget after expenses.
  
    def display_cat(self):
        print(f"Category: {self.get_category()}")
        print(f"Allocated Budget {self.get_allocated_budget()}")
        expenses = 

    def budget_details(self):
        print(f"Category: {self.__category_name}, Allocated Budget: {self.__allocated_budget}, Remaining Budget: {self.__remaining_budget}")

# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.


