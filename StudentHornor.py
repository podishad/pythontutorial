class StudentHornor:

    def __init__(self, name, study, gpa):
        self.name = name
        self.study = study
        self.gpa = gpa


    def onHornorRoll(self):
        if(self.gpa > 3.5):
            return True
        else:
            return False