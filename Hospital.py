from replit import clear 
class Patient:
    def __init__(self,id,name,age,bloodgroup):
        
        self.id = id 
        self.name = name 
        self.age = age 
        self.bloodgroup = bloodgroup 

class WRM:
    def __init__(self):
        self.arr = []

        

    def RegisterPatient(self,id,name,age,bloodgroup):
        
        temp = Patient(id,name,age,bloodgroup)
        self.arr.append(temp)
               
        print("Patient registered successfully")



    def ShowAllPatient(self):
        if len(self.arr) == 0: 
            print("No patients left")
        else:
            print("Waiting Patients list:")
            for patient in self.arr:
                print(f"Name: {patient.name},id: {patient.id}")

    def ServePatient(self):
        if len(self.arr) == 0:  
            print("No patients to serve.")
        else:
            print(f"Serverd patient Name: {self.arr[0].name} and id: {self.arr[0].id}")
            del self.arr[0]



    def CanDoctorGoHome(self):
        if len(self.arr) == 0:
            return True
        return False
    
    def CancelAll(self):
        if len(self.arr)!=0:
            del self.arr[0:len(self.arr)]
            print('All appointment canceled')
            
        elif  len(self.arr)==0:
            print('No Patient to cancel')



    


CDLL = WRM()
print("---Welcome to Waiting Room Management---")

while True:
    print("Select an Option:")
    print(f"1. Add Patient\n2. Serve Patient\n3. Show All patients\n4. Can Doctor go Home?\n5. Cancel all Appointment.\n6. Exit")

    inp = int(input("Choose option No: "))
    if inp ==1:
        id = int(input('Enter id:'))
        name = input('Enter name:')
        age = int(input('Enter age:'))
        blood = input('Enter Blood Group:')

        CDLL.RegisterPatient(id,name,age,blood)
    elif inp ==2:
        clear()
        CDLL.ServePatient()
        
    elif inp == 3:
        clear()
        CDLL.ShowAllPatient()
        
    elif inp == 4:
        clear()
        if CDLL.CanDoctorGoHome() == True:
            print('Yes')
        else:
            print('NO')
        
    elif inp == 5:
        clear()
        CDLL.CancelAll()
        
    elif inp == 6:
        print("Thank you for using. Successfully Exited")
        break

print('---------------------------------------')