from flask import request
from dataAccess.connectionMangment import ConnectionMangment
from utility.base import Base
from utility.dateTime import DateTime
import mysql.connector
import random

class PatientDA(Base):

    def __init__(self):
        self.conn = ConnectionMangment.getConnection()
        self.cursor = self.conn.cursor()

    def findAll(self):

            self.cursor.execute("select * from patient")
            patients = self.cursor.fetchall()

            self.conn.commit()
            self.conn.close()

            return patients


    def findById(self,id):

            self.cursor.execute("select * from patient where id = %s",(id,))
            patient = self.cursor.fetchone()

            self.conn.commit()
            self.conn.close()

            return patient


    def save(self):

            try:
               ID = request.form['id']
               f_name = request.form['f_name']
               l_name = request.form['l_name']
               dateOfBirth = DateTime().convertStringToTime(request.form['DOB'])
               email = request.form['email']
               phoneNumber = request.form['phoneNumber']
               gender = request.form['gender']
               address = request.form['address']
               height = request.form['height']
               weight = request.form['weight']
               state = request.form['state']
               blood = request.form['blood']
               profileImage = request.files['profileImage']


               patient_tuple = (ID,f_name,l_name,dateOfBirth,email,phoneNumber,
                                gender,address,height,weight,state,blood,
                                profileImage.filename,0)
               sql = """insert into patient(ID,f_name,l_name,DOB,Email,phoneNumber,
                        gender,address,height,weight,state,blood,profileImage,
                        numberOfNewPrescription)
                         values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
               self.cursor.execute(sql,patient_tuple)

               self.conn.commit()
               self.conn.close()

               return [True,ID,profileImage]
            except mysql.connector.IntegrityError:
                return [False]

    def delete(self,id):

        try:

            self.cursor.execute("delete from patient where ID = %s",(id,))

            self.conn.commit()
            self.conn.close()

            return True

        except mysql.connector.IntegrityError:

            return False


    def update(self,id):

            try:

               f_name = request.form['f_name']
               l_name = request.form['l_name']
               dateOfBirth = DateTime().convertStringToTime(request.form['DOB'])
               email = request.form['email']
               phoneNumber = request.form['phoneNumber']
               gender = request.form['gender']
               address = request.form['address']
               height = int(request.form['height'])
               weight = int(request.form['weight'])
               state = request.form['state']
               blood = request.form['blood']
               profileImage = request.files['profileImage']

               patient_tuple = (f_name,l_name,dateOfBirth,email,phoneNumber,gender,address,height,weight,state,blood,profileImage.filename,id)

               sql = """update patient
                        set f_name = %s,l_name = %s,DOB = %s,Email = %s,phoneNumber = %s,gender = %s,address = %s,height = %s,weight = %s,
                        state = %s,blood = %s,profileImage = %s
                        WHERE ID = %s """

               self.cursor.execute(sql,patient_tuple)

               self.conn.commit()
               self.conn.close()

               return [True,id,profileImage]

            except mysql.connector.IntegrityError:

                return [False]


    def findByPhoneNumber(self,phoneNumber):

        self.cursor.execute("select * from patient where phoneNumber = %s",(phoneNumber,))
        patient = self.cursor.fetchone()

        self.conn.commit()
        self.conn.close()

        return patient


    def savePrescription(self):

        try:

           prescription_id = str(int(random.random()*1000000000000))
           otherDoctorName = request.form['otherDoctorName']
           patient_id = request.form['patient_id']
           image = request.files['image']
           date = DateTime().convertStringToTime(request.form['date'])
           classification = request.form['classification']

           tuple_presc = (prescription_id,image.filename,classification,'null',date,patient_id,otherDoctorName)
           sql = """insert into prescription(prescid,filePath,classification,RX,date,patient_prescription_ID,otherDoctorName)
                    values(%s,%s,%s,%s,%s,%s,%s)"""
           self.cursor.execute(sql,tuple_presc)

           self.conn.commit()
           self.conn.close()

           return [True,patient_id,image]

        except mysql.connector.IntegrityError:

           return [False]



    def getAllPrescriptions(self,patientId):

        self.cursor.execute("select * from prescription where patient_prescription_ID = %s and filePath != 'null' order by date desc",(patientId,))
        prescriptions = self.cursor.fetchall()

        self.conn.commit()
        self.conn.close()

        return prescriptions




    def getAllPrescriptionsByOtherDoctorName(self,patientId,otherDoctorName):

        self.cursor.execute("select * from prescription where patient_prescription_ID = %s and  otherDoctorName LIKE %s order by date desc",
                             (patientId,"%" + otherDoctorName + "%"))
        prescriptions = self.cursor.fetchall()

        self.conn.commit()
        self.conn.close()

        return prescriptions



    def getAllPrescriptionsByClassification(self,patientId,classification):

        self.cursor.execute("select * from prescription where patient_prescription_ID = %s and classification = %s order by date desc",
                             (patientId,classification,))
        prescriptions = self.cursor.fetchall()

        self.conn.commit()
        self.conn.close()

        return prescriptions




    def getAllDigitalPrescriptions(self,patientId):

        self.cursor.execute("""select doctor.ID,doctor.firstName,doctor.lastName,doctor.email,doctor.phoneNumber,doctor.master,doctor.profileImage,
                               prescription.classification,prescription.RX,prescription.date from prescription
                               inner join doctor on doctor.ID=prescription.doctor_prescription_ID
                               where prescription.patient_prescription_ID = %s
                               order by date desc""",(patientId,))
        prescriptions = self.cursor.fetchall()
        self.cursor.execute("UPDATE patient SET numberOfNewPrescription = 0  WHERE ID = %s",(patientId,))
        self.conn.commit()
        self.conn.close()

        return prescriptions




    def getAllDigitalPrescriptionsByDoctorName(self,patientId,doctorName):

        length = len(doctorName.split())

        if length==1:

             firstName = doctorName.split()[0]
             self.cursor.execute("""select doctor.ID,doctor.firstName,doctor.lastName,doctor.email,doctor.phoneNumber,doctor.master,
                                    doctor.profileImage,prescription.classification,prescription.RX,prescription.date from prescription
                                    inner join doctor on doctor.ID=prescription.doctor_prescription_ID
                                    where prescription.patient_prescription_ID = %s and doctor.firstName LIKE %s or doctor.lastName LIKE %s
                                    order by date desc""",(patientId,"%" + firstName + "%","%" + firstName + "%"))

        else:

            firstName = doctorName.split()[0]
            lastName = doctorName.split()[1]
            self.cursor.execute("""select doctor.ID,doctor.firstName,doctor.lastName,doctor.email,doctor.phoneNumber,doctor.master,doctor.profileImage,
                                   prescription.classification,prescription.RX,prescription.date from prescription
                                   inner join doctor on doctor.ID=prescription.doctor_prescription_ID
                                   where prescription.patient_prescription_ID = %s and doctor.firstName LIKE %s and doctor.lastName LIKE %s
                                   order by date desc""",(patientId,"%" + firstName + "%","%" + lastName + "%"))

        prescriptions = self.cursor.fetchall()

        self.conn.commit()
        self.conn.close()

        return prescriptions



    def getAllDigitalPrescriptionsByMaster(self,patientId,master):

        self.cursor.execute("""select doctor.ID,doctor.firstName,doctor.lastName,doctor.email,doctor.phoneNumber,doctor.master,doctor.profileImage,
                               prescription.classification,prescription.RX,prescription.date from prescription
                               inner join doctor on doctor.ID=prescription.doctor_prescription_ID
                               where prescription.patient_prescription_ID = %s and doctor.master = %s
                               order by date desc""",(patientId,master))

        prescriptions = self.cursor.fetchall()

        self.conn.commit()
        self.conn.close()

        return prescriptions




    def incrementNumberOfPrescription(self,patientId):

        self.cursor.execute("""UPDATE patient SET numberOfNewPrescription = numberOfNewPrescription + 1 WHERE ID = %s""",(patientId,))
        self.conn.commit()
        self.conn.close()


    def getNumberOfNewPrescription(self,patientId):

        self.cursor.execute("select numberOfNewPrescription from patient  WHERE ID = %s",(patientId,))
        data = self.cursor.fetchone()[0]
        self.conn.commit()
        self.conn.close()

        return str(data)


    def getNumberOfPrescription(self,patientId):

        self.cursor.execute("select count(*) from prescription  WHERE patient_prescription_ID = %s and filePath !='null'",(patientId,))
        data = self.cursor.fetchone()[0]
        self.conn.commit()
        self.conn.close()

        return data


    def getNumberOfDigitalPrescription(self,patientId):

        self.cursor.execute("select count(*) from prescription  WHERE patient_prescription_ID = %s and filePath ='null'",(patientId,))
        data = self.cursor.fetchone()[0]
        self.conn.commit()
        self.conn.close()

        return data




    def deleteAllDoctors(self,patientId):

            self.cursor.execute("delete from patient_doctor where patient_id=%s",(patientId,))
            self.conn.commit()
            self.conn.close()
