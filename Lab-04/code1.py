class Patient:
    def __init__(self,next,prev,id,name,age,bloodgroup):
        
        self.next = next 
        self.prev = prev
        self.id = id 
        self.name = name 
        self.age = age 
        self.bloodgroup = bloodgroup 

class WRM:
    def __init__(self):
        self.dh = Patient(None,None,None,None,None,None) 
        self.dh.next = self.dh
        self.dh.prev = self.dh
        

    def RegisterPatient(self,id,name,age,bloodgroup):
        
        temp = Patient(None,None,id,name,age,bloodgroup)
        last = self.dh.prev
        temp.next = self.dh 
        temp.prev = last
        self.dh.prev = temp 
        last.next = temp
               
        print("Patient registered successfully")



    def ShowAllPatient(self):
        if self.dh.next == self.dh:  
            print("No patients left")
        else:
            p = self.dh.next
            print("Waiting patients:")
            while p != self.dh:
                print("ID:", p.id)
                p = p.next

    def ServePatient(self):
        if self.dh.next == self.dh:  
            print("No patients to serve.")
        else:
            served_patient = self.dh.next
            self.dh.next = served_patient.next
            served_patient.next.prev = self.dh
            print("Serving patient:", served_patient.id)


    def CanDoctorGoHome(self):
        if self.dh.next == self.dh:
            return True
        return False
    def CancelAll(self):
        if self.dh.next != self.dh:
            self.dh.next = self.dh  
            self.dh.prev = self.dh 
            print('All appointment canceled')
            
        elif  self.dh.next == self.dh:
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
        CDLL.ServePatient()
    elif inp == 3:
        CDLL.ShowAllPatient()
    elif inp == 4:
        if CDLL.CanDoctorGoHome() == True:
            print('Yes')
        else:
            print('NO')
    elif inp == 5:
        CDLL.CancelAll()
    elif inp == 6:
        print("Thank you for using. Successfully Exited")
        break

print('---------------------------------------')