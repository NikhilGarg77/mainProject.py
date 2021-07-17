# This class will include details of all visitors/user
# Before scheduling appointment user need to create his/her own profile

import User
import pymongo

#insert new user
def insertNewUser(user_name,passport,email,password):
        userAlreadyExists = userExistsCheck(user_name,passport)
        if userAlreadyExists:
            return False
        else:
            connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
            my_client = pymongo.MongoClient(connection_string)
            db = my_client["Vaccine_Finder"]
            vaccine = db["Appointments"]
            newUser = {"user_name": user_name, "passport": passport, "email": email, "password": password,"bookingDate":"0000-00-00"}
            vaccine.insert_one(newUser)
            return True
        return False


# validate User already exists
def userExistsCheck(user_name, passport):
    connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["Vaccine_Finder"]
    mycol = db["Appointments"]
    clms = {"user_name","passport"}
    result = mycol.find_one({'$and' : [{'user_name':user_name}, {'passport':passport}]},clms)
    if result is None:
        print("No such user exists. Registration can be done.")
        return False
    else:
        print("User already exists. Registration cannot be done.")
        for x in result:
            print(x)
        return True
    return False


# validate registration
def vaidateRegistrarion(user_name, passport, password):
    connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["Vaccine_Finder"]
    mycol = db["Appointments"]
    clms = {"user_name","passport","password"}
    result = mycol.find_one({'$and' : [{'user_name':user_name}, {'passport':passport}, {'password':password}]},clms)
    if result is None:
        return False
    else:
        for x in result:
            print(x)
            return True
    return False



# validate Booking
def vaidateBooking(user_name, passport, password):
    connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["Vaccine_Finder"]
    mycol = db["Appointments"]
    clms = {"bookingDate"}
    result = mycol.find({'$and' : [{'user_name':user_name}, {'passport':passport}, {'password':password}]})
    print("In validate booking")
    if result is None:
        return False
    else:
        for x in result:
            print(x.get('bookingDate'))
            if x.get('bookingDate') == "0000-00-00":
                return True
    return False


# Method will create user profile based on info from client side
def intiate_appointment():
    pass

# Method will update existing appointment
def update_appointment():
    pass


# Method will retrieve all appointments from Database based on unique id
def get_appointment_details_byId():
    pass


# Method to retrieve all appointments
def get_all_appointment_details():
    pass



