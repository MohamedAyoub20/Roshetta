from utility.base import Base
from dataAccess.pharmacist import PharmacistDA
from utility.image import Image

class PharmacistBU(Base):

    def findAll(self):

        listOfPharmacists = []
        pharmacists = PharmacistDA().findAll()

        for pharmacist in pharmacists:

            dic_patient = {"id":pharmacist[0],"firstName":pharmacist[1],"lastName":pharmacist[2],"email":pharmacist[3],
                           "phoneNumber":pharmacist[4],"pharmacyName":pharmacist[5],"delivery":pharmacist[6],"address":pharmacist[7],
                            "workHours":pharmacist[8],"profileImage":pharmacist[9]}

            listOfPharmacists.append(dic_patient)

        return listOfPharmacists

    def findById(self,id):

            listOfPharmacists = []
            pharmacist = PharmacistDA().findById(id)

            dic_patient = {"id":pharmacist[0],"firstName":pharmacist[1],"lastName":pharmacist[2],"email":pharmacist[3],
                           "phoneNumber":pharmacist[4],"pharmacyName":pharmacist[5],"delivery":pharmacist[6],"address":pharmacist[7],
                            "workHours":pharmacist[8],"profileImage":pharmacist[9]}

            listOfPharmacists.append(dic_patient)

            return listOfPharmacists

    def save(self):

        data = PharmacistDA().save()

        if data[0]==True:
          Image().createFolder("user",data[1])
          Image().saveImage("user",data[1],data[2])

          return 'true'

        else:
            return 'false'

    def delete(self,id):

        Image().deleteFolder("user",id)

        num = PharmacistDA().delete(id)
        if num != 0:
            return True
        else:
            return False

    def update(self,id):

        data = PharmacistDA().update(id)

        if data[0]==True:
          Image().updateProfileImage(data[1],data[2])
          return 'true'

        else:
            return 'false'


