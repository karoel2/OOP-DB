class Employee():
	def __init__(self, name, surname, salary):
		self.name = name
		self.surname = surname
		self.salary = salary

	def __str__(self):
		return "{} {}, earn {}$".format(self.name, self.surname, self.salary)

	def __repr__(self):
		return "{} {}, earn {}$".format(self.name, self.surname, self.salary)

	def __int__(self):
		return self.salary

class ListOfEmployees():
	def __init__(self, employees=None):
		self.employees = employees

	def __str__(self):
		return str(self.employees)

	@classmethod
	def createList(cls, employeesList):
		employees = []
		for name, surname, salary in employeesList:
			employees.append(Employee(name, surname, salary))
		return cls(employees)

	def addEmployee(self, name, surname, salary):
		self.employees.append(Employee(name, surname, salary))
