import mysql.connector

class ConnectionMangment:

        @staticmethod
        def getConnection():

            return mysql.connector.connect(host='Roshetta1.mysql.pythonanywhere-services.com',
                                           db='Roshetta1$roshettadb',
                                           user='Roshetta1',
                                           password='MedicalSystem')
