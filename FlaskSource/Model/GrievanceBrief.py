class GrievanceBrief:
    def __init__(self, id, category, status, description, raisedUser, reply):
        self.id = id
        self.category = category
        self.status = status
        self.description = description
        self.raisedUser = raisedUser
        self.reply = reply

    def getGrievanceId(self):
        return self.id
    
    def getCategory(self):
        return self.category

    def getStatus(self):
        return self.status

    def getDescription(self):
        return self.description

    def getraisedUser(self):
        return self.raisedUser

    def getreply(self):
        return self.reply

