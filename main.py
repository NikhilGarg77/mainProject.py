
from flask import Flask, request, render_template
import pymongo
import Profile
import User
import Appointments
import Organisations
import AdminPortal
from flask import Flask, session

app = Flask(__name__)

def intiate_mongoDb_conn():
    connection_string = "mongodb+srv://dbUser:dbUser@cluster0.w78tt.mongodb.net/Vaccine_Finder?retryWrites=true&w=majority"
    mongo_client = pymongo.MongoClient(connection_string)



@app.route("/")
def index():
    return render_template('homepage.html')


@app.route("/admin", methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'GET':
        return render_template('login-page.html')
    else:
        return render_template('homepage.html')


@app.route("/admin-login", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user_name = request.form.get("username")
        password = request.form.get("password")
        admin = AdminPortal.AdminPortal()
        action = admin.authenticate(user_name, password)
        appointment_list_status = admin.getAppointmentStatus()
        vaccination_status = admin.getVaccinationStatus()
        if action:
            return render_template('login-success.html', username=user_name.upper(), og_appointment=appointment_list_status[0], upg_appointment=appointment_list_status[1], cld_appointment=appointment_list_status[2], ttl_appointment=appointment_list_status[3], available_vc=vaccination_status[0], unused_vc=vaccination_status[1], expired_vc=vaccination_status[2], days_vc=vaccination_status[3])
        else:
            return render_template('login-fail.html')
    else:
        return render_template('login-fail.html')


# Started by Dashmeet Kaur

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return render_template('homepage.html')


@app.route("/register-login", methods=['GET', 'POST'])
def register_login():
    if request.method == 'POST' and request.form["btn"] == "Register":
        print("Register clicked")
        user_name = request.form.get("name")
        session['user_name'] = user_name
        passport = request.form.get("passport")
        session['passport'] = passport
        email = request.form.get("email")
        session['email'] = email
        password = request.form.get("inputPassword")
        session['password'] = password
        action = Appointments.insertNewUser(user_name,passport,email,password)
        if action:
            return render_template('login-success-book.html', username=user_name.upper())
        else:
            return render_template('user-already-exists.html')

    elif request.method == 'POST' and request.form["btn"] == "Sign In":
        print("Sign in clicked")
        user_name = request.form.get("name")
        session['user_name'] = user_name
        passport = request.form.get("passport")
        session['passport'] = passport
        email = request.form.get("email")
        session['email'] = email
        password = request.form.get("inputPassword")
        session['password'] = password
        action = Appointments.vaidateRegistrarion(user_name, passport, password)
        if action:
            action = Appointments.vaidateBooking(user_name, passport, password)
            if action:
                print("going to sign in")
                return render_template('login-success-book.html', username=user_name.upper())
            else:
                return render_template('login-success-signin.html', username=user_name.upper())
        else:
            return render_template('user-login-fail.html')



@app.route("/book-my-apptmnt", methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        print("in book appointment clicked")
        booking_date = request.form.get("book-date")
        print(booking_date)
        user_name = session['user_name']
        passport = session['passport']
        email = session['email']
        password = session['password']
        return render_template('booking-success.html', username=user_name.upper(),booking_date=booking_date)
    else:
        return render_template('login-fail.html')



@app.route("/cert", methods= ['GET','POST'])
def Certificate():
    if request.method=='GET':
        return render_template('Certificate.html')
    else:
        return render_template('homepage.html')
@app.route('/get-certificate', methods=['GET','POST'])
def get_certificate():
    if request.method == 'POST':
        user_name = request.form.get('userName')
        passport = request.form.get('passport')
        password = request.form.get('password')
        find= Certificate.userCheck(user_name,passport,password)
        if find:
            return render_template('certificate-found.html')
        else:
            return render_template('user-login-fail.html')

@app.route('/about_us', methods=['GET','POST'] )
def about_us():
    if request.method=='GET':
        return render_template('FAQ.html')
    else:
        return render_template('homepage.html')
        
    






if __name__ == "__main__":
    app.config['SECRET_KEY'] = "abcd"
    app.run()
    intiate_mongoDb_conn()
