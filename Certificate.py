# This class will include details of all visitors/user
# Before scheduling appointment user need to create his/her own profile

import User
import pymongo



# validate registration
def userCheck(userName,passport,password):
    connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string)
    db = my_client["Vaccine_Finder"]
    mycol = db["Certificate"]
    clms = {"userName","passport","password"}
    result = mycol.find_one({'$and' : [{'user_name':userName}, {'passport':passport},{'password': password}]},clms)
    if result is None:
        print("No such user exists.")
        return False
    else:
        print("User already exists. ")
        for x in result:
            print(x)
        return True
    return False



