class Hospital:
    def __init__(self,name):
        self.hname = name
        self.ddic = {}
        self.pdic = {}
    def addDoctor(self,gg):
        self.ddic[gg.docid] = [gg.docname,gg.expert]
    def getDoctorByID(self,id):
        templst = self.ddic[id]
        print("Doctor's ID:",id)
        print("Name:",templst[0])
        return f"Speciality: {templst[1]}"
    def addPatient(self,gg):
        self.pdic[gg.pid] = [gg.pname,gg.page,gg.pphone]
    def getPatientByID(self,id):
        lst = self.pdic[id]
        print("Patient's ID:",id)
        print("Name:",lst[0])
        print("Age:",lst[1])
        return f"Phone no: {lst[2]}"
    def allDoctors(self):
        print("All Doctors:")
        print(f"Number of Doctors: {len(self.ddic.keys())}")
        print(self.ddic)
    def allPatients(self):
        print("All Patients:")
        print(f"Number of Patients: {len(self.pdic.keys())}")
        print(self.pdic)        


class Doctor:
    def __init__(self,id,prof,name,expert):
        self.docid = id
        self.docname = name
        self.expert = expert


class Patient:
    def __init__(self,id,prof,name,age,phone):
        self.pid = id
        self.pname = name
        self.page = age
        self.pphone = phone




h = Hospital("Evercare")
d1 = Doctor("1d","Doctor", "Samar Kumar", "Neurologist")
h.addDoctor(d1)
print("=================================")
print(h.getDoctorByID("1d"))
print("=================================")
p1 = Patient("1p","Patient", "Kashem Ahmed", 35, 12345)
h.addPatient(p1)
print("=================================")
print(h.getPatientByID("1p"))
print("=================================")
p2 = Patient ("2p","Patient", "Tanina Haque", 26, 33456)
h.addPatient(p2)
print("=================================")
print(h.getPatientByID("2p"))
print("=================================")
h.allDoctors()
h.allPatients()