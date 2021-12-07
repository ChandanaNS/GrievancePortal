from Database import DBConnection

# Fetch all the grievances from Database
def getAllGrievances():
    cur = DBConnection.connection().cursor()
    cur.execute("SELECT * FROM grievance")
    data = cur.fetchall()
    cur.close()
    return data

# # Fetch all the Grievance from UserDatabase
# def getUserGrievances(user):
#     db_connection = DBConnection.connection()
#     cur = db_connection.cursor()
#     cur.execute("SELECT Grievances FROM users where UserName=%s" + user)
#     data = cur.fetchall()
#     cur.close()
#     return data

# Add grievance to Database
def addGrievance(tableName, category, status, description, raisedBy):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "INSERT INTO " + tableName + "( GrievanceCategory, GrievanceStatus ,Description, RaisedUser) VALUES (%s,%s,%s,%s)",
        (category, status, description, raisedBy))
    db_connection.commit()
    cur.close()


# Fetch Product using Product ID
def getGrievancesById(id):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM grievance where GrievanceID=" + str(id))
    data = cur.fetchone()
    db_connection.commit()
    cur.close()
    return data
#
# # Fetch grievance using user name
# def getGrievancesByUser(user_name):
#     print("Raised User", user_name)
#     db_connection = DBConnection.connection()
#     cur = db_connection.cursor()
#     cur.execute("SELECT * FROM grievance WHERE RaisedUser=%s" + str('mon'))
#     data = cur.fetchall()
#     print(data)
#     db_connection.commit()
#     cur.close()
#     return data


# Fetch Product using Product ID
def getlastAddedGrievance():
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM grievance ORDER BY GrievanceID DESC LIMIT 1")
    data = cur.fetchone()
    db_connection.commit()
    cur.close()
    return data

# Delete  Grievance using GrievanceID
def deleteGrievanceUsingId(grievanceId):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute("DELETE from grievance where GrievanceID=" + grievanceId)
    db_connection.commit()
    cur.close()


# Update grievance using grievance ID
def updateGrievance(grievanceId, category, status, description, raisedUser, reply):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "UPDATE grievance SET GrievanceCategory=%s,GrievanceStatus=%s,Description=%s,RaisedUser=%s,Reply=%s where GrievanceID=%s",
        (category, status, description, raisedUser, reply, grievanceId))
    db_connection.commit()
    cur.close()

# Update grievance for users
def updateUserGrievance(user, data):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "UPDATE users SET Grievances=%s where UserName=%s",
        (str(data), str(user)))
    db_connection.commit()
    cur.close()

# update password using userName
def updatePassword(userName, newPassword):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "UPDATE users SET Password=%s where userName=%s",
        (newPassword, userName))
    db_connection.commit()
    cur.close()

#
# Fetch all users
def getAllUser():
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "Select * from users")
    data = cur.fetchall()
    db_connection.commit()
    cur.close()
    return data


# Create User in Database
def createUser(name, userName, password, email, gender, dob, phoneNumber):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "INSERT INTO users (FullName,UserName, Password,Email,Gender,DateOfBirth,PhoneNumber) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (name, userName, password, email, gender, dob, phoneNumber))
    db_connection.commit()
    cur.close()


# Get User by User Name
def getUserByUserName(userName):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute(
        "SELECT * FROM users WHERE UserName=%s", str(userName))
    data = cur.fetchone()
    # data = cur.fetchall()
    db_connection.commit()
    cur.close()
    return data


# update user grievance
def updateGrievances(grievance_list, user_name):
    db_connection = DBConnection.connection()
    cur = db_connection.cursor()
    cur.execute("UPDATE users SET Grievances=%s WHERE UserName=%s", (str(grievance_list), str(user_name)))
    db_connection.commit()
    cur.close()
