# Problem 1: Bank Account
class BankAccount:
    """
    Base class to represent a bank account.
    Encapsulates account number and balance with methods to deposit and withdraw funds.
    """
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # Encapsulated balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        Only positive amounts are allowed.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Withdrawals cannot exceed current balance.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        """Return the current balance."""
        return self.__balance


class SavingsAccount(BankAccount):
    """
    SavingsAccount inherits from BankAccount.
    It has an interest rate and method to calculate interest.
    """
    def __init__(self, account_number, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Calculate interest on current balance.
        """
        interest = self.get_balance() * self.interest_rate
        print(f"Interest calculated at rate {self.interest_rate * 100}% is: {interest}")
        return interest


class CurrentAccount(BankAccount):
    """
    CurrentAccount inherits from BankAccount.
    It enforces a minimum balance.
    """
    def __init__(self, account_number, initial_balance=0, minimum_balance=500):
        super().__init__(account_number, initial_balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        """
        Override withdraw to ensure balance doesn't go below minimum balance.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if (self.get_balance() - amount) < self.minimum_balance:
            print(f"Cannot withdraw {amount}. Minimum balance requirement of {self.minimum_balance} must be maintained.")
        else:
            # Accessing base class withdraw method for valid withdrawal
            super().withdraw(amount)


# Example usage and test
if __name__ == "__main__":
    print("Savings Account Example:")
    sav_acc = SavingsAccount("SA123", 1000, 0.05)
    sav_acc.deposit(200)
    sav_acc.withdraw(100)
    sav_acc.calculate_interest()
    print(f"Savings Account balance: {sav_acc.get_balance()}")

    print("\nCurrent Account Example:")
    cur_acc = CurrentAccount("CA123", 1500, 500)
    cur_acc.withdraw(1200)  # Should not allow since it breaks minimum balance
    cur_acc.withdraw(900)   # Should allow withdrawal
    cur_acc.deposit(300)
    print(f"Current Account balance: {cur_acc.get_balance()}")

    #Problem 2 -Employee Management

class Employee:
    """
    Base class representing an employee.
    Attributes:
        name (str): Name of the employee.
        salary (float): Base salary of the employee.
    """
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        """
        Method to calculate the salary.
        To be overridden in subclasses based on specific rules.
        """
        return self.salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.calculate_salary()}"


class RegularEmployee(Employee):
    """
    Regular employee with fixed salary.
    No special calculation needed, uses base salary.
    """
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_salary(self):
        return self.salary


class ContractEmployee(Employee):
    """
    Contract employee paid by hourly rate and hours worked.
    Attributes:
        hourly_rate (float): Payment rate per hour.
        hours_worked (int or float): Number of hours worked in pay period.
    """
    def __init__(self, name, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        # Base salary can be zero or hourly_rate * hours_worked
        super().__init__(name, hourly_rate * hours_worked)

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    """
    Manager with base salary and bonus percentage.
    Attributes:
        bonus_percentage (float): Bonus percentage applied on base salary.
    """
    def __init__(self, name, salary, bonus_percentage):
        super().__init__(name, salary)
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self):
        return self.salary + (self.salary * self.bonus_percentage / 100)


# Demonstrating usage and polymorphism
if __name__ == "__main__":
    employees = [
        RegularEmployee("Alice", 50000),
        ContractEmployee("Bob", 50, 120),  # 50 per hour, 120 hours
        Manager("Charlie", 70000, 15),     # 15% bonus
    ]

    for emp in employees:
        print(f"{emp.name} earns {emp.calculate_salary()} units")

# problem 3 - Vehicle Rental

class Vehicle:
    """
    Base class representing a vehicle.
    Attributes:
        model (str): Model name of the vehicle.
        rental_rate (float): Base rental rate per day.
    """
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        """
        Calculate rental cost for given rental duration (days).
        Should be overridden by subclasses for specific calculations.
        """
        if days <= 0:
            raise ValueError("Rental duration must be positive")
        return self.rental_rate * days

    def __str__(self):
        return f"Vehicle Model: {self.model}, Rate per day: {self.rental_rate}"


class Car(Vehicle):
    """
    Car subclass with an additional attribute for air conditioning.
    Rental cost increases by 10% if air conditioning is present.
    """
    def __init__(self, model, rental_rate, has_air_conditioning):
        super().__init__(model, rental_rate)
        self.has_air_conditioning = has_air_conditioning

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        if self.has_air_conditioning:
            return base_cost * 1.10  # 10% extra charge
        return base_cost


class Bike(Vehicle):
    """
    Bike subclass with additional attribute for helmet included.
    Rental cost has a fixed discount if helmet is included.
    """
    def __init__(self, model, rental_rate, helmet_included):
        super().__init__(model, rental_rate)
        self.helmet_included = helmet_included

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        if self.helmet_included:
            return base_cost - 5  # flat discount of 5 units
        return base_cost


class Truck(Vehicle):
    """
    Truck subclass with additional attribute for load capacity.
    Rental cost is higher by 20% if load capacity exceeds 10 tons.
    """
    def __init__(self, model, rental_rate, load_capacity_tons):
        super().__init__(model, rental_rate)
        self.load_capacity_tons = load_capacity_tons

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        if self.load_capacity_tons > 10:
            return base_cost * 1.20  # 20% extra charge
        return base_cost


# Example usage demonstrating polymorphism
if __name__ == "__main__":
    vehicles = [
        Car("Toyota Corolla", 40, True),
        Bike("Yamaha MT-15", 15, True),
        Truck("Volvo FH", 100, 12),
    ]

    rental_days = 5
    for vehicle in vehicles:
        cost = vehicle.calculate_rental(rental_days)
        print(f"{vehicle.model}: Rental cost for {rental_days} days = {cost}")
