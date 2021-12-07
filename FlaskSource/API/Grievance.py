from flask import render_template, session, request, redirect, Blueprint, flash
from FlaskSource.Model.GrievanceBrief import GrievanceBrief
from FlaskSource.Model.UserDetails import UserDetails
from Database import DBQuery
import json
import ast
from datetime import date
import smtplib
import ssl

grievanceApi = Blueprint('grievanceApi', __name__)

# Python Flask API for home page
@grievanceApi.route('/')
def homePage():
    try:
        login_dictionary = {}
        if session.get('logged_in'):
            login_dictionary['logged_in'] = "true"
        elif session.get('superAdmin'):
            login_dictionary["superAdmin"] = "true"
        return render_template('index.html', data=login_dictionary)
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for list page
@grievanceApi.route('/list')
def list():
    try:
        login_dictionary = {}
        if session.get('logged_in'):
            login_dictionary['logged_in'] = "true"
        elif session.get('superAdmin'):
            login_dictionary["superAdmin"] = "true"

        user_name = session['user'][2]
        userData = DBQuery.getUserByUserName(user_name)
        grievance_list = []
        user_list = []
        if userData:
            userDetails = UserDetails(userData[0], userData[1], userData[2], userData[3], userData[4], userData[5],
                                      date.isoformat(userData[6]),
                                      userData[7], userData[8])
            if userDetails.getUserName() != 'admin':
                if userDetails.getGrievances() is None:
                    userDetails.setGrievances([])
                    jsonUserDump = json.dumps(userDetails.__dict__)
                    user_list.append(json.loads(jsonUserDump))
                else:
                    jsonUserDump = json.dumps(userDetails.__dict__)
                    user_list.append(json.loads(jsonUserDump))
                    for value in ast.literal_eval(userDetails.getGrievances()):
                        if value['reply'] is None:
                            value['reply'] = ''
                        grievanceBrief = GrievanceBrief(value['id'], value['category'], value['status'],
                                                        value['description'], value['raisedUser'], value['reply'])
                        jsonDump = json.dumps(grievanceBrief.__dict__)
                        grievance_list.append(json.loads(jsonDump))
        login_dictionary['grievanceList'] = grievance_list
        login_dictionary['user'] = user_list
        return render_template('list.html', data=login_dictionary)
    except:
        flash('Something went wrong')
        return redirect("/")

@grievanceApi.route('/email')
def sendEmail(login_details):
    try:
        user = (login_details['user'][0])
        grievance = (login_details['grievanceList'][-1])
        if user['userName'] != 'admin':
            email = 'chandana2594@gmail.com' # admin mail
            message = "Grievance Description: " + grievance['description']
        else:
            email = ""
            message = ""

        sender_email = "OGMS.college@gmail.com"
        receiver_email = email
        message = """\
        Subject: OGMS\
        """ + message

        # Send email here

        port = 465  # For SSL
        password = "ogms@1234"

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("OGMS.college@gmail.com", password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        flash('Something went wrong')
        return redirect("/")


@grievanceApi.route('/emailUpdate')
def sendUpdateEmail(login_details):
    try:
        if session['superAdmin']:
            grievanceId = login_details['grievanceList']
            user_name = login_details['user']
            userData = DBQuery.getUserByUserName(user_name)
            if userData:
                userDetails = UserDetails(userData[0], userData[1], userData[2], userData[3], userData[4],
                                          userData[5],
                                          date.isoformat(userData[6]),
                                          userData[7], userData[8])
            grievance = DBQuery.getGrievancesById(grievanceId)
            email = userDetails.getEmail()
            message = "Reply: " + grievance[5]

        sender_email = "OGMS.college@gmail.com"
        receiver_email = email
        message = """\
        Subject: OGMS\
        """ + message

        # Send email here

        port = 465  # For SSL
        password = "ogms@1234"

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("OGMS.college@gmail.com", password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        flash('Something went wrong')
        return redirect("/")

# Python Flask API for adding a product
@grievanceApi.route('/add', methods=['GET', 'POST'])
def addGrievances():
    try:
        if request.method == "POST":
            postAction = request.form["postAction"]
            if postAction == 'cancel':
                return redirect("/list")

            Category = request.form["Category"]
            Status = request.form["Status"]
            Description = request.form["Description"]
            RaisedUser = session['userName']
            if Category and Status and Description:
                DBQuery.addGrievance('grievance',  Category.title(), Status.title(), Description.title(), RaisedUser)
                grievance_data = DBQuery.getlastAddedGrievance()
                latestGrievanceBrief = GrievanceBrief(grievance_data[0], grievance_data[1], grievance_data[2], grievance_data[3], grievance_data[4], grievance_data[5])
                jsonData = json.dumps(latestGrievanceBrief.__dict__)

                user_name = session['user'][2]
                userData = DBQuery.getUserByUserName(user_name)
                grievance_list = []
                user_list = []
                login_dictionary = {}
                if userData:
                    userDetails = UserDetails(userData[0], userData[1], userData[2], userData[3], userData[4],
                                              userData[5],
                                              date.isoformat(userData[6]),
                                              userData[7], userData[8])
                    if userDetails.getUserName() != 'admin':
                        if userDetails.getGrievances() is None:
                            userDetails.setGrievances([])
                            jsonUserDump = json.dumps(userDetails.__dict__)
                            user_list.append(json.loads(jsonUserDump))
                        else:
                            jsonUserDump = json.dumps(userDetails.__dict__)
                            user_list.append(json.loads(jsonUserDump))
                            for value in ast.literal_eval(userDetails.getGrievances()):
                                if value['reply'] is None:
                                    value['reply'] = ''
                                grievanceBrief = GrievanceBrief(value['id'], value['category'], value['status'],
                                                                value['description'], value['raisedUser'],
                                                                value['reply'])
                                jsonDump = json.dumps(grievanceBrief.__dict__)
                                grievance_list.append(json.loads(jsonDump))

                grievance_list.append(json.loads(jsonData))
                DBQuery.updateGrievances(grievance_list, RaisedUser)
                flash("Grievance Added Successfully")
                login_dictionary['grievanceList'] = grievance_list
                login_dictionary['user'] = user_list
                sendEmail(login_dictionary)
                return redirect("/list")
            else:
                flash('Please fill in all the details')
                return redirect("/add")
        return render_template('add.html')
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for Update User list
@grievanceApi.route('/updateUserList')
def UpdateUserlist(user):
    try:
        user_name = user
        userGData = DBQuery.getAllGrievances()
        grievance_list = []
        for grievanceValue in userGData:
            if grievanceValue[4] == user_name:
                grievanceBrief = GrievanceBrief(grievanceValue[0], grievanceValue[1],
                                                grievanceValue[2], grievanceValue[3],
                                                grievanceValue[4], grievanceValue[5])

                jsonDump = json.dumps(grievanceBrief.__dict__)
                grievance_list.append(json.loads(jsonDump))
                DBQuery.updateUserGrievance(user_name, grievance_list)
        if session.get('superAdmin'):
            return redirect("/admin")
        return redirect("/list")
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for updating a product
@grievanceApi.route('/update', methods=['GET', 'POST'])
def updateGrievance():
    try:
        grievanceId = request.args.get('id')
        grievance = []
        loginData = {}
        # Fetch grievance from Database using grievance ID
        if grievanceId is not None:
            grievanceFromDB = DBQuery.getGrievancesById(grievanceId)
            if grievanceFromDB[5] is None:
                grievanceReply = ''
            else:
                grievanceReply = grievanceFromDB[5]
            grievanceBrief = GrievanceBrief(grievanceFromDB[0], grievanceFromDB[1], grievanceFromDB[2],
                                            grievanceFromDB[3], grievanceFromDB[4], grievanceReply)
            grievance.append(grievanceBrief.__dict__)
            jsonData = json.dumps(grievance)
            loginData['GrievanceList'] = json.loads(jsonData)
        else:
            if request.method == "POST":
                postAction = request.form["postAction"]
                if postAction == 'cancel':
                    if session.get('superAdmin'):
                        return redirect("/admin")
                    return redirect("/list")
                if postAction == 'delete':
                    return deleteGrievance()
                category = request.form["category"]
                status = request.form["status"]
                reply = request.form["reply"]
                raisedUser = request.form["raisedUser"]
                description = request.form["description"]
                grievanceId = request.form['grievanceId']
                if category and status and description:
                    DBQuery.updateGrievance(grievanceId, category, status, description, raisedUser, reply)
                    flash("Grievance Updated Successfully")
                    if session.get('superAdmin'):
                        loginGrievanceData = {'grievanceList': grievanceId, 'user': raisedUser}
                        sendUpdateEmail(loginGrievanceData)
                    return UpdateUserlist(raisedUser)
                else:
                    flash('Please fill in all the details')
                    return redirect("/update")

        if session.get('logged_in'):
            loginData['AdminUser'] = 'False'
        elif session.get('superAdmin'):
            loginData['AdminUser'] = str(session['superAdmin'])
        return render_template('update.html', update=loginData)
    except:
        flash('Something went wrong')
        return redirect("/")


# Python Flask API for deleting a grievance
@grievanceApi.route('/delete')
def deleteGrievance():
    try:
        grievanceId = request.form["grievanceId"]
        DBQuery.deleteGrievanceUsingId(grievanceId)
        flash("Grievance Deleted Successfully")
        return UpdateUserlist(request.form['raisedUser'])
    except:
        flash('Something went wrong')
        return redirect("/")
