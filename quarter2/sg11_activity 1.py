# defines parent class Patients
class Patient:
    # initializes
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # methods defined
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")

# defines class for senior patient that inherits methods from the parent class
class Senior_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80 # 20% discount for senior patients

    def diplay_patient_type(self):
        print("Patient Type: Senior Patient")

# defines class for philhealth patients that inherits methods from the parent class
class Philhealth_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85 # 15% discount for philhealth patients

    def display_patient_type(self):
        print("Patient Type: Philhealth Patient")

# object/patients variables
patient1 = Patient("Juan Dela Cruz", 15000.00)
senior_patient1 = Senior_Patient("Maria Santos", 15000.00)
philhealth_patient1 = Philhealth_Patient("Pedro Reyes", 15000.00)

print("Hospital Billing System")
print("-----------------------")

# stores objects/patients in the list
patients = [patient1, senior_patient1, philhealth_patient1]

# starts a loop through each patients included in the list
for i in patients:
    # displays patient's name, og bill, and final bill (and yung print() para mas organized) for all objects
    print(f"Patient Name: {i.get_name()}") 
    i.display_patient_type()
    print(f"Original Bill: ₱{i.get_bill_amount():.2f}")
    print(f"Final Bill: ₱{i.calculate_bill():.2f}")
    print()

