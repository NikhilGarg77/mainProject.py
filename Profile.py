# This class will include details of all visitors/user
# Before scheduling appointment user need to create his/her own profile

import User

# Method will create user profile based on info from client side
def create_user(mongo_client): # REGISTER AND SIGN UP
    # Insert one
    # print(my_client)
    db = mongo_client["vaccine_finder"]
    # print(db.list_collection_names())
    collection_user = db["user"]
    myData = {"address": "New Delhi", "borough": "Kalkaji", "cuisine": "Indian", "name": "Dashmeet",
              "restaurant_id": "12341234"}
    x = collection_user.insert_one(myData)

    # Insert many
    mylist = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Sandy", "address": "Ocean blvd 2"}
    ]
    x = collection_user.insert_many(mylist)
    # print list of the _id values of the inserted documents:
    print(x.inserted_ids)

    # Insert many with ID
    mylist = [
        {"_id": 100, "name": "John", "address": "Uttam Nagar"},
        {"_id": 200, "name": "Peter", "address": "Lowstreet 27"},
        {"_id": 300, "name": "Amy", "address": "Apple st 652"}
    ]
    x = collection_user.insert_many(mylist)
    # print list of the _id values of the inserted documents:
    print(x.inserted_ids)

# Method will update profile based on unique Id from client side
def update_user(): # GET CERTIFICATE MODULE
    pass


# Method will retrieve from Database user info based on unique id
def get_user_details_byId(): # GET CERTIFICATE MODULE
    pass


# Method to retrieve all users data
def get_all_users_details():
    pass



