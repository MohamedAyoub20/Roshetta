from flask import request
from dataAccess.connectionMangment import ConnectionMangment
from utility.base import Base
from utility.dateTime import DateTime
import mysql.connector
import random
from datetime import date

class DoctorDA(Base):

    def __init__(self):
        self.conn = ConnectionMangment.getConnection()
        self.cursor = self.conn.cursor()

    def findAll(self):
            self.cursor.execute("select * from doctor")
            doctors = self.cursor.fetchall()

            self.conn.commit()
            self.conn.close()
            return doctors

    def findById(self,id):
            self.cursor.execute("select * from doctor where ID = %s",(id,))
            doctor = self.cursor.fetchone()

            self.conn.commit()
            self.conn.close()
            return doctor

    def save(self):

        try:
            id = request.form['id']
            email = request.form['email']
            address = request.form['address']
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            birthday = DateTime().convertStringToTime(request.form['birthday'])
            master = request.form['master']
            hospital = request.form['hospital']
            gender = request.form['gender']
            phoneNumber = request.form['phoneNumber']
            profileImage = request.files['profileImage']


            patient_tuple = (id,email,address,firstName,lastName,birthday,master,hospital,gender,phoneNumber,profileImage.filename)
            sql = """insert into doctor(ID,email,address,firstName,lastName,birthday,master,hospital,gender,phoneNumber,profileImage)
                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            self.cursor.execute(sql,patient_tuple)

            self.conn.commit()
            self.conn.close()

            return [True,id,profileImage]

        except mysql.connector.IntegrityError:

            return [False]



    def delete(self,id):

        try:

            self.cursor.execute("delete from doctor where ID= %s",(id,))
            self.conn.commit()
            self.conn.close()

            return True

        except mysql.connector.IntegrityError:
            return False



    def update(self,id):

        try:
            email = request.form['email']
            address = request.form['address']
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            birthday = DateTime().convertStringToTime(request.form['birthday'])
            master = request.form['master']
            hospital = request.form['hospital']
            gender = request.form['gender']
            phoneNumber = request.form['phoneNumber']
            profileImage = request.files['profileImage']


            patient_tuple = (email,address,firstName,lastName,birthday,master,hospital,gender,phoneNumber,profileImage.filename,id)

            sql = """update doctor
                     set email = %s,address = %s,firstName = %s,lastName = %s,birthday = %s,master = %s,hospital = %s,gender = %s,
                     phoneNumber = %s,profileImage = %s
                     where ID = %s"""

            self.cursor.execute(sql,patient_tuple)

            self.conn.commit()
            self.conn.close()

            return [True,id,profileImage]

        except mysql.connector.IntegrityError:

            return [False]


    def saveDigitalPrescription(self):

        try:

           prescription_id = int(random.random()*100000000000)
           patient_id = request.form['patient_id']
           doctor_id = request.form['doctor_id']
           classfication = request.form['classfication']
           rx = request.form['rx']

           tuple_presc = (prescription_id,'null',classfication,rx,date.today(),patient_id,'null',doctor_id)
           sql = """insert into prescription(prescid,filePath,classification,RX,date,patient_prescription_ID,otherDoctorName,doctor_prescription_ID)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)"""
           self.cursor.execute(sql,tuple_presc)

           self.conn.commit()
           self.conn.close()

           return [True,patient_id,doctor_id]

        except mysql.connector.IntegrityError:

          return [False]


    def savePatientIdDoctorId(self,patientId,doctorId):

           tupl = (patientId,doctorId,patientId,doctorId)
           sql = "insert into patient_doctor(patient_id,doctor_id) values(%s,%s) on duplicate key update patient_id=%s,doctor_id=%s"
           self.cursor.execute(sql,tupl)

           self.conn.commit()
           self.conn.close()


    def getAllPatientId(self,doctorId):

           self.cursor.execute("select patient_id from patient_doctor where doctor_id=%s",(doctorId,))
           listOfPatientId = self.cursor.fetchall()
           self.conn.commit()
           self.conn.close()

           return listOfPatientId



    def getAllPatients(self,listPatientId):

            listOfPatients = []

            for patientId in listPatientId:
                self.cursor.execute("select * from patient where ID=%s",(patientId[0],))
                patient = self.cursor.fetchone()
                listOfPatients.append(patient)

            self.conn.commit()
            self.conn.close()

            return listOfPatients



    def deleteAllPatients(self,doctorId):

            self.cursor.execute("delete from patient_doctor where doctor_id=%s",(doctorId,))
            self.conn.commit()
            self.conn.close()



    def getAllPatientDigitalPrescriptions(self,patientId,doctorId):

            self.cursor.execute("select * from prescription where patient_prescription_ID=%s and doctor_prescription_ID=%s",(patientId,doctorId))
            listOfDigitalPrescriptions = self.cursor.fetchall()
            self.conn.commit()
            self.conn.close()

            return listOfDigitalPrescriptions


