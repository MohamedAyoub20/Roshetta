import os
import requests

class Image:

    def __init__(self):

        self.UPLOAD_FOLDER_Prescription ='/home/Roshetta1/prescriptionImages'
        self.UPLOAD_FOLDER_User ='/home/Roshetta1/profileImages'


    def saveImage(self,userType,user_id,image):

        if userType == "prescription":
            path = image.filename
            folder = self.UPLOAD_FOLDER_Prescription+'/'+user_id
            image.save(os.path.join(folder, path))

        elif userType == "user":
             path = image.filename
             folder = self.UPLOAD_FOLDER_User+'/'+user_id
             image.save(os.path.join(folder, path))


    def deleteImage(self,user_id,image_name):
        path = self.UPLOAD_FOLDER_Prescription+'/'+user_id
        if image_name in os.listdir(path):
            os.remove(path+'/'+image_name)

    def updateProfileImage(self,user_id,image):
        folder = self.UPLOAD_FOLDER_User+'/'+user_id
        path = image.filename
        profileImageName = os.listdir(folder)
        os.remove(folder+'/'+profileImageName[0])
        image.save(os.path.join(folder,path))


    def deleteFolder(self,userType,user_id):

        if userType == "prescription":
            path = self.UPLOAD_FOLDER_Prescription+'/'+user_id
            os.system(r"rm -r %s" %(path))

        elif userType == "user":
            path = self.UPLOAD_FOLDER_User+'/'+user_id
            os.system(r"rm -r %s" %(path))


    def createFolder(self,userType,user_id):

        if userType == "prescription":
            folder = self.UPLOAD_FOLDER_Prescription+'/'+user_id
            os.mkdir(folder)

        elif userType == "user":
            folder = self.UPLOAD_FOLDER_User+'/'+user_id
            os.mkdir(folder)


    def sendImageToModel(self,image):
        image.save(os.path.join('/home/Roshetta1', image.filename))
        url = 'http://1c5423ee27ff.ngrok.io'
        myfiles = {'image': open('/home/Roshetta1/'+image.filename,'rb')}
        os.remove('/home/Roshetta1/'+image.filename)
        return str(requests.post(url, files = myfiles).content, encoding='utf-8')

