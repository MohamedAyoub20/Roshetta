from flask import Flask,jsonify,send_from_directory,request
from business.patient import PatientBU
from business.doctor import DoctorBU
from business.pharmacist import PharmacistBU
from utility.image import Image


app = Flask(__name__)



@app.route('/<object>', methods = ['GET'])
def findAll(object):

    if object=='pharmacists':
        return jsonify(PharmacistBU().findAll())

    elif object=='patients':
        return jsonify(PatientBU().findAll())

    elif object=='doctors':
        return jsonify(DoctorBU().findAll())



@app.route('/<object>/id=<id>', methods = ['GET'])
def findById(object,id):

    if object=='pharmacist':
        return jsonify(PharmacistBU().findById(id))

    elif object=='patient':
        return jsonify(PatientBU().findById(id))

    elif object=='doctor':
        return jsonify(DoctorBU().findById(id))




@app.route('/<object>',methods = ['POST'])
def save(object):

    if object=='prescription':
        return PatientBU().savePrescription()

    elif object=='digitalPrescription':
        return DoctorBU().saveDigitalPrescription()

    elif object=='pharmacist':
        return PharmacistBU().save()

    elif object=='patient':
        return PatientBU().save()

    elif object=='doctor':
        return DoctorBU().save()



@app.route('/<object>/id=<id>',methods = ['DELETE'])
def delete(object,id):

    if object=='pharmacists':
        return jsonify(PharmacistBU().delete(id))

    elif object=='patients':
        return jsonify(PatientBU().delete(id))

    elif object=='doctors':
        return jsonify(DoctorBU().delete(id))



@app.route('/<object>/id=<id>',methods = ['PUT'])
def update(object,id):

    if object=='pharmacist':
        return PharmacistBU().update(id)

    elif object=='patient':
        return PatientBU().update(id)

    elif object=='doctor':
        return DoctorBU().update(id)



@app.route('/<key>/patientid=<patientId>', methods = ['GET'])
def getPrescriptionsByPatientId(key,patientId):

    if key=='Prescriptions':
        return jsonify(PatientBU().getAllPrescriptions(patientId))

    elif key=='digitalPrescriptions':
        return jsonify(PatientBU().getAllDigitalPrescriptions(patientId))



@app.route('/patient/phoneNumber=<phoneNumber>', methods = ['GET'])
def findPatientByPhoneNumber(phoneNumber):
    return jsonify(PatientBU().findByPhoneNumber(phoneNumber))



@app.route('/patientPrescriptionClassfication/patientId=<patientId>/classification=<classification>', methods = ['GET'])
def getAllPrescriptionsByClassfication(patientId,classification):
        return jsonify(PatientBU().getAllPrescriptionsByClassification(patientId,classification))



@app.route('/patientDigitalPrescriptionMaster/patientId=<patientId>/master=<master>', methods = ['GET'])
def getAllPrescriptionsByMaster(patientId,master):
         return jsonify(PatientBU().getAllDigitalPrescriptionsByMaster(patientId,master))



@app.route('/patientPrescriptionOtherDoctorName/patientId=<patientId>/otherDoctorName=<otherDoctorName>', methods = ['GET'])
def getAllPrescriptionsByOtherDoctorName(patientId,otherDoctorName):
        return jsonify(PatientBU().getAllPrescriptionsByOtherDoctorName(patientId,otherDoctorName))



@app.route('/patientDigitalPrescriptionDoctorName/patientId=<patientId>/doctorName=<doctorName>', methods = ['GET'])
def getAllPrescriptionsByDoctorName(patientId,doctorName):
        return jsonify(PatientBU().getAllDigitalPrescriptionsByDoctorName(patientId,doctorName))



@app.route('/numberOfNewPrescriptions/id=<patientid>', methods = ['GET'])
def getNumberOfNewPrescription(patientid):
    return PatientBU().getNumberOfNewPrescription(patientid)



@app.route('/numberOfPrescriptions/id=<patientid>', methods = ['GET'])
def getNumberOfPrescription(patientid):
    return PatientBU().getNumberOfAllPrescriptions(patientid)



@app.route('/doctorPatient/id=<doctorId>', methods = ['GET'])
def getAllPatients(doctorId):
    return jsonify(DoctorBU().getAllPatients(doctorId))



@app.route('/doctorPatientPrescription/patientId=<patientId>/doctorId=<doctorId>', methods = ['GET'])
def getAllPatientDigitalPrescriptions(patientId,doctorId):
    return jsonify(DoctorBU().getAllPatientDigitalPrescriptions(patientId,doctorId))



@app.route('/connectionBetweenMLAndMobileApp', methods = ['POST'])
def connectionBetweenMLAndMobileApp():

    image = request.files['image']
    return Image().sendImageToModel(image)


@app.route('/showprescriptionimage/<user_id>/<imageName>',methods = ['GET'])
def showPrescriptionImage(user_id,imageName):
    return send_from_directory('/home/Roshetta1/prescriptionImages/'+user_id,imageName)



@app.route('/showprofileimage/<user_id>/<imageName>',methods = ['GET'])
def showProfileImage(user_id,imageName):
    return send_from_directory('/home/Roshetta1/profileImages/'+user_id,imageName)


