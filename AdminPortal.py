import pymongo


class AdminPortal:

    def authenticate(self, username, password):
        if str(username).lower() == 'ayush' and str(password).lower() == 'admin01234':
            return True
        else:
            return False

    def getAppointmentStatus(self):
        connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
        my_client = pymongo.MongoClient(connection_string)
        db = my_client["Vaccine_Finder"]
        vaccine = db["Appointments"]
        ongoing = 2400
        upcoming = 728
        cancelled = 289
        total = 3417
        list_To_Return = [ongoing, upcoming, cancelled, total]
        return list_To_Return

    def getVaccinationStatus(self):
        connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
        my_client = pymongo.MongoClient(connection_string)
        db = my_client["Vaccine_Finder"]
        vaccine = db["Appointments"]
        available_vc = 240
        unused = 32
        expired = 8
        days = 2
        vaccination_status = [available_vc, unused, expired, days]
        return vaccination_status

