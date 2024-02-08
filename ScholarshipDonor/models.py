from django.db import models

# Create your models here.
class Scholarship:

    def __init__(self, name, maxAward, totalAvail, dateCreated, applicants, awarded):
        self.name = name
        self.maxAward = maxAward        #max amount of money awarded to one candidate
        self.totalAvail = totalAvail    #total money to give out 
        self.dateCreated = dateCreated  
        self.applicants = applicants    #list of type application
        self.awarded = awarded          #list of type application?

    