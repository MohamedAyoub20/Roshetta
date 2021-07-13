from flask import request
from dataAccess.connectionMangment import ConnectionMangment
from utility.base import Base
import mysql.connector

class PharmacistDA(Base):

      def __init__(self):
          self.conn = ConnectionMangment.getConnection()
          self.cursor = self.conn.cursor()

      def findAll(self):

              self.cursor.execute("select * from pharmacist")
              pharmacists = self.cursor.fetchall()

              self.conn.commit()
              self.conn.close()

              return pharmacists


      def findById(self,id):

              self.cursor.execute("select * from pharmacist where ID = %s",(id,))
              pharmacist = self.cursor.fetchone()

              self.conn.commit()
              self.conn.close()

              return pharmacist


      def save(self):

        try:

          id = request.form['id']
          firstName = request.form['firstName']
          lastName = request.form['lastName']
          email = request.form['email']
          phoneNumber = request.form['phoneNumber']
          pharmacyName = request.form['pharmacyName']
          address = request.form['address']
          delivery = request.form['delivery']
          workHours = int(request.form['workHours'])
          profileImage = request.files['profileImage']

          tuple_pharmacist = (id,firstName,lastName,email,phoneNumber,pharmacyName,address,delivery,workHours,profileImage.filename)
          sql = """insert into pharmacist(ID,firstName,lastName,email,phoneNumber,pharmacyName,address,delivery,workHours,profileImage)
                 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
          self.cursor.execute(sql,tuple_pharmacist)
          self.conn.commit()
          self.conn.close()

          return [True,id,profileImage]

        except mysql.connector.IntegrityError:

          return [False]

      def delete(self,id):

              self.cursor.execute("delete from pharmacist where ID = %s",(id,))

              self.conn.commit()
              self.conn.close()

              return self.cursor.rowcount


      def update(self,id):

        try:

          firstName = request.form['firstName']
          lastName = request.form['lastName']
          email = request.form['email']
          phoneNumber = request.form['phoneNumber']
          pharmacyName = request.form['pharmacyName']
          address = request.form['address']
          delivery = request.form['delivery']
          workHours = request.form['workHours']
          profileImage = request.files['profileImage']

          tuple_pharmacist = (firstName,lastName,email,phoneNumber,pharmacyName,address,delivery,workHours,profileImage.filename,id)

          sql = """update pharmacist
                   set firstName= %s,lastName= %s,email= %s,phoneNumber= %s,pharmacyName= %s,address= %s,delivery= %s,workHours= %s,profileImage= %s
                   where ID = %s"""

          self.cursor.execute(sql,tuple_pharmacist)
          self.conn.commit()
          self.conn.close()

          return [True,id,profileImage]

        except mysql.connector.IntegrityError:

          return [False]
