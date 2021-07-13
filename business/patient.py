from utility.dateTime import DateTime
from utility.base import Base
from dataAccess.patient import PatientDA
from utility.image import Image



class PatientBU(Base):

    def findAll(self):

            listOfPatient = []
            patients = PatientDA().findAll()

            for patient in patients:

                  dateOfBirth = DateTime().convertTimeToString(patient[3])

                  dic_patient = {"id":patient[0],"f_name":patient[1],"l_name":patient[2],"dateOfBirth":dateOfBirth,
                  "Email":patient[4],"phoneNumber":patient[5],"gender":patient[6],"address":patient[7],
                  "height":str(patient[8]),"weight":str(patient[9]),"state":patient[10],"blood":patient[11],"profileImage":patient[12]}

                  listOfPatient.append(dic_patient)

            return listOfPatient

    def findById(self,id):

            listOfPatient = []
            patient = PatientDA().findById(id)

            dateOfBirth = DateTime().convertTimeToString(patient[3])
            dic_patient = {"id":patient[0],"f_name":patient[1],"l_name":patient[2],"dateOfBirth":dateOfBirth,
                  "Email":patient[4],"phoneNumber":patient[5],"gender":patient[6],"address":patient[7],
                  "height":str(patient[8]),"weight":str(patient[9]),"state":patient[10],"blood":patient[11],"profileImage":patient[12]}
            listOfPatient.append(dic_patient)

            return listOfPatient

    def save(self):

        data = PatientDA().save()

        if data[0]==True:
          Image().createFolder("user",data[1])
          Image().saveImage("user",data[1],data[2])
          Image().createFolder("prescription",data[1])
          return 'true'

        else:
            return 'false'

    def delete(self,id):

        data = PatientDA().delete(id)

        if data == True:
            Image().deleteFolder("prescription",id)
            Image().deleteFolder("user",id)
            PatientDA().deleteAllDoctors(id)
            return True
        else:
            return False


    def update(self,id):
        data = PatientDA().update(id)
        if data[0]==True:
          Image().updateProfileImage(data[1],data[2])
          return 'true'
        else:
            return 'false'


    def findByPhoneNumber(self,phoneNumber):
            listOfPatient = []
            patient = PatientDA().findByPhoneNumber(phoneNumber)
            if patient is None :
                return listOfPatient
            else:
                dateOfBirth = DateTime().convertTimeToString(patient[3])
                dic_patient = {"id":patient[0],"f_name":patient[1],"l_name":patient[2],"dateOfBirth":dateOfBirth,
                  "Email":patient[4],"phoneNumber":patient[5],"gender":patient[6],"address":patient[7],
                  "height":str(patient[8]),"weight":str(patient[9]),"state":patient[10],"blood":patient[11],"profileImage":patient[12]}
                listOfPatient.append(dic_patient)

                return listOfPatient


    def savePrescription(self):

        data = PatientDA().savePrescription()

        if data[0]==True:
          Image().saveImage("prescription",data[1],data[2])
          return 'true'

        else:
            return 'false'


    def getAllPrescriptions(self,patient_id):
        listOfPrescription = []
        prescriptions = PatientDA().getAllPrescriptions(patient_id)
        for prescription in prescriptions:
            date = DateTime().convertTimeToString(prescription[4])
            dic_prescription = {"id":prescription[0],"filePath":prescription[1],"classification":prescription[2],
                                "RX":prescription[3],"date":date,"otherDoctorName":prescription[5],
                                "patient_id":prescription[6]}
            listOfPrescription.append(dic_prescription)
        return listOfPrescription




    def getAllPrescriptionsByOtherDoctorName(self,patientId,otherDoctorName):

        listOfPrescription = []
        prescriptions = PatientDA().getAllPrescriptionsByOtherDoctorName(patientId,otherDoctorName)
        for prescription in prescriptions:
            date = DateTime().convertTimeToString(prescription[4])
            dic_prescription = {"id":prescription[0],"filePath":prescription[1],"classification":prescription[2],
                                "RX":prescription[3].strip(),"date":date,"otherDoctorName":prescription[5],
                                "patient_id":prescription[6]}
            listOfPrescription.append(dic_prescription)
        return listOfPrescription



    def getAllPrescriptionsByClassification(self,patientId,classification):

        listOfPrescription = []
        prescriptions = PatientDA().getAllPrescriptionsByClassification(patientId,classification)
        for prescription in prescriptions:
            date = DateTime().convertTimeToString(prescription[4])
            dic_prescription = {"id":prescription[0],"filePath":prescription[1],"classification":prescription[2],
                                "RX":prescription[3].strip(),"date":date,"otherDoctorName":prescription[5],
                                "patient_id":prescription[6]}
            listOfPrescription.append(dic_prescription)
        return listOfPrescription



    def getAllDigitalPrescriptions(self,patientId):

        listOfPrescription = []
        prescriptions = PatientDA().getAllDigitalPrescriptions(patientId)
        for prescription in prescriptions:
            date = DateTime().convertTimeToString(prescription[9])
            dic_prescription = {"doctorId":prescription[0],"doctorFirstName":prescription[1],"doctorLastName":prescription[2],"doctorEmail":prescription[3],
                                "doctorPhoneNumber":prescription[4],"doctorMaster":prescription[5],"doctorProfileImage":prescription[6],
                                "prescriptionClassification":prescription[7],"prescriptionRX":prescription[8],"prescriptionDate":date}
            listOfPrescription.append(dic_prescription)
        return listOfPrescription




    def getAllDigitalPrescriptionsByDoctorName(self,patientId,doctorName):

        listOfPrescription = []
        prescriptions = PatientDA().getAllDigitalPrescriptionsByDoctorName(patientId,doctorName)
        for prescription in prescriptions:
            date = DateTime().convertTimeToString(prescription[9])
            dic_prescription = {"doctorId":prescription[0],"doctorFirstName":prescription[1],"doctorLastName":prescription[2],"doctorEmail":prescription[3],
                                "doctorPhoneNumber":prescription[4],"doctorMaster":prescription[5],"doctorProfileImage":prescription[6],
                                "prescriptionClassification":prescription[7],"prescriptionRX":prescription[8],"prescriptionDate":date}
            listOfPrescription.append(dic_prescription)
        return listOfPrescription



    def getAllDigitalPrescriptionsByMaster(self,patientId,master):

        listOfPrescription = []
        prescriptions = PatientDA().getAllDigitalPrescriptionsByMaster(patientId,master)
        for prescription in prescriptions:
            date = DateTime().convertTimeToString(prescription[9])
            dic_prescription = {"doctorId":prescription[0],"doctorFirstName":prescription[1],"doctorLastName":prescription[2],"doctorEmail":prescription[3],
                                "doctorPhoneNumber":prescription[4],"doctorMaster":prescription[5],"doctorProfileImage":prescription[6],
                                "prescriptionClassification":prescription[7],"prescriptionRX":prescription[8],"prescriptionDate":date}
            listOfPrescription.append(dic_prescription)
        return listOfPrescription



    def getNumberOfNewPrescription(self,patientId):

        data = PatientDA().getNumberOfNewPrescription(patientId)
        return str(data)




    def getNumberOfAllPrescriptions(self,patientId):

        prescription = PatientDA().getNumberOfPrescription(patientId)
        digitalPrescriptions = PatientDA().getNumberOfDigitalPrescription(patientId)

        return str(prescription)+','+str(digitalPrescriptions)
