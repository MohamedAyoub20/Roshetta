from utility.dateTime import DateTime
from utility.base import Base
from dataAccess.doctor import DoctorDA
from utility.image import Image
from dataAccess.patient import PatientDA


class DoctorBU(Base):

    def findAll(self):

            listOfDoctor = []
            doctors = DoctorDA().findAll()

            for doctor in doctors:

                  dateOfBirth = DateTime().convertTimeToString(doctor[3])

                  dic_doctor =  {"id":doctor[0],"firstName":doctor[1],"lastName":doctor[2],"birthday":dateOfBirth,
                                "email":doctor[4],"phoneNumber":doctor[5],"master":doctor[6],"address":doctor[7],
                                "hospital":doctor[8],"gender":doctor[9],"profileImage":doctor[10]}

                  listOfDoctor.append(dic_doctor)

            return listOfDoctor


    def findById(self,id):

            listOfDoctor = []
            doctor = DoctorDA().findById(id)

            dateOfBirth = DateTime().convertTimeToString(doctor[3])
            dic_doctor = {"id":doctor[0],"firstName":doctor[1],"lastName":doctor[2],"birthday":dateOfBirth,
                                "email":doctor[4],"phoneNumber":doctor[5],"master":doctor[6],"address":doctor[7],
                                "hospital":doctor[8],"gender":doctor[9],"profileImage":doctor[10]}
            listOfDoctor.append(dic_doctor)

            return listOfDoctor

    def save(self):

        data = DoctorDA().save()

        if data[0]==True:
            Image().createFolder("user",data[1])
            Image().saveImage("user",data[1],data[2])

            return 'true'
        else:

            return 'false'

    def delete(self,id):

        data = DoctorDA().delete(id)

        if data == True:
            Image().deleteFolder("user",id)
            DoctorDA().deleteAllPatients(id)
            return True

        else:
            return False

    def update(self,id):

        data = DoctorDA().update(id)

        if data[0]==True:
          Image().updateProfileImage(data[1],data[2])
          return 'true'

        else:
            return 'false'


    def saveDigitalPrescription(self):

        data = DoctorDA().saveDigitalPrescription()

        if data[0]==True:
            PatientDA().incrementNumberOfPrescription(data[1])
            DoctorDA().savePatientIdDoctorId(data[1],data[2])
            return "true"
        else:
            return "false"



    def getAllPatients(self,doctorId):

        listOfPatientId = DoctorDA().getAllPatientId(doctorId)

        patients = DoctorDA().getAllPatients(listOfPatientId)

        listOfPatient = []

        for patient in patients:

            dateOfBirth = DateTime().convertTimeToString(patient[3])

            dic_patient = {"id":patient[0],"f_name":patient[1],"l_name":patient[2],"dateOfBirth":dateOfBirth,
                           "Email":patient[4],"phoneNumber":patient[5],"gender":patient[6],"address":patient[7],
                           "height":str(patient[8]),"weight":str(patient[9]),"state":patient[10],"blood":patient[11],"profileImage":patient[12]}

            listOfPatient.append(dic_patient)

        return listOfPatient



    def getNumberOfPatients(self,doctorId):

        listOfPatientId = DoctorDA().getAllPatientId(doctorId)

        data = len(listOfPatientId)

        return str(data)


    def getAllPatientDigitalPrescriptions(self,patientId,doctorId):

        listOfPrescription = []
        prescriptions = DoctorDA().getAllPatientDigitalPrescriptions(patientId,doctorId)
        for prescription in prescriptions:
            date = DateTime().convertTimeToString(prescription[4])
            dic_prescription = {"id":prescription[0],"filePath":prescription[1],"classification":prescription[2],
                                "RX":prescription[3],"date":date,"otherDoctorName":prescription[5],
                                "patient_id":prescription[6]}
            listOfPrescription.append(dic_prescription)
        return listOfPrescription
