class UserDetails:
    def __init__(self, loginId, name, userName, password, email, gender, dateOfBirth, phoneNumber, grievances):
        self.loginId = loginId
        self.name = name
        self.userName = userName
        self.password = password
        self.email = email
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.phoneNumber = phoneNumber
        self.grievances = grievances

    def getLoginId(self):
        return self.loginId

    def getName(self):
        return self.name

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    def getGender(self):
        return self.gender

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getPhoneNumber(self):
        return self.phoneNumber

    def getGrievances(self):
        return self.grievances

    def setGrievances(self, x):
        self.grievances = x
