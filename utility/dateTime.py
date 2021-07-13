import datetime

class DateTime:

    def convertTimeToString(self,timeTuple):

         year = str(timeTuple.timetuple()[2])
         month = str(timeTuple.timetuple()[1])
         day = str(timeTuple.timetuple()[0])

         return day+'-'+month+'-'+year

    def convertStringToTime(self,date):

         dateList = date.split("-")
         year = int(dateList[0])
         month = int(dateList[1])
         day = int(dateList[2])

         return datetime.datetime(year,month,day)