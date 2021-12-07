from datetime import date
from flask import render_template, session, request, redirect, Blueprint, flash

from FlaskSource.API.Grievance import UpdateUserlist
from FlaskSource.Model.GrievanceBrief import GrievanceBrief
from FlaskSource.Model.UserDetails import UserDetails
from Database import DBQuery
import json

adminApi = Blueprint('adminApi', __name__)


# Python Flask API to Show Admin Statics
@adminApi.route('/admin')
def adminLogs():
    try:
        login_dictionary = {}
        user_list = []
        grievance_list = []
        if session.get('superAdmin'):
            login_dictionary["superAdmin"] = "true"
            user_data = DBQuery.getAllUser()
            for userData in user_data:
                userDetails = UserDetails(userData[0], userData[1], userData[2], userData[3], userData[4], userData[5],
                                          date.isoformat(userData[6]), userData[7], userData[8])

                jsonUserDump = json.dumps(userDetails.__dict__)
                user_list.append(json.loads(jsonUserDump))
            login_dictionary['userList'] = user_list
            # Fetch All the grievances from Database
            grievance_data = DBQuery.getAllGrievances()
            for grievanceFromDB in grievance_data:
                grievanceReply = ''
                if grievanceFromDB[5] is not None:
                    grievanceReply = grievanceFromDB[5]
                grievanceBrief = GrievanceBrief(grievanceFromDB[0], grievanceFromDB[1], grievanceFromDB[2],
                                                grievanceFromDB[3], grievanceFromDB[4], grievanceReply)

                jsonData = json.dumps(grievanceBrief.__dict__)
                grievance_list.append(json.loads(jsonData))

            login_dictionary['adminGrievanceList'] = grievance_list
        elif session.get('logged_in'):
            login_dictionary['logged_in'] = "true"

        return render_template('admin.html', data=login_dictionary)
    except Exception as e:
        flash('Something went wrong')
        return redirect("/")

# Python Flask API for deleting a grievance
@adminApi.route('/delete')
def deleteGrievance():
    try:
        grievanceId = request.form["grievanceId"]
        DBQuery.deleteGrievanceUsingId(grievanceId)
        flash("Grievance Deleted Successfully")
        return UpdateUserlist(request.form['raisedUser'])
    except:
        flash('Something went wrong')
        return redirect("/")