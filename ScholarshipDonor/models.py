from django.db import models

# Create your models here.
class Scholarship:

    def __init__(self, name, amount, donor, totalAvail, minGPA, major, dateCreated, applicants, awarded, description):
        self.name = name
        self.amount = amount            #max amount of money awarded to one candidate
        self.donor = donor
        self.totalAvail = totalAvail    #total money to give out 
        self.minGPA = minGPA            #min gpa
        self.major = major
        self.dateCreated = dateCreated  
        self.applicants = applicants    #list of type application
        self.awarded = awarded          #list of type application?
        self.description = description
        
class Donor:

    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
    