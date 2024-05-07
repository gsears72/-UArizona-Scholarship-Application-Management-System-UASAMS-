from django.shortcuts import render
from NotificationSystem.models import Notification
from Login.models import User

# Create your views here.

def send_notification_S_INREVIEW( recipient, scholarship_name):
    title = "Application in Review"
    message = "Your application for "+ scholarship_name +" is currently in review. You will be notified of the decision soon."
    sender ="SFWEAutoNotify"

    Notification.objects.create(title=title, message=message, sender=sender, recipient=recipient)   
    pass

def send_notification_SA_REVIWFINISHED( recipient, scholarship_name):
    title = "Application Review Finished"
    message = "An application for "+scholarship_name+ " review has been completed. Please review the decision."
    sender ="SFWEAutoNotify"

    Notification.objects.create(title=title, message=message, sender=sender, recipient=recipient) 
    pass

def send_notification_S_DECISION( recipient, decision,scholarship_name):
    
    if (decision == "ACCEPTED"):
        title = "Application Accepted"
        message = "Congratulations! Your application for "+  scholarship_name +  " has been accepted."
    elif (decision == "REJECTED"):
        title = "Application Rejected"
        message = "We regret to inform you that your application for " +scholarship_name +  " has been rejected."

    sender ="SFWEAutoNotify"

    Notification.objects.create(title=title, message=message, sender=sender, recipient=recipient) 


    pass


def send_notification_SD_AWARDER( recipient, scholarship_name,winner):
    title = "Scholarship Awarded"
    message = "Congratulations! The scholarship for "+ scholarship_name + " has been awarded to " + winner
    sender ="SFWEAutoNotify"

    Notification.objects.create(title=title, message=message, sender=sender, recipient=recipient)

    pass

def send_notification_S_CLARIFICATION( recipient,scholarship_name):
    title = "Clarification Required"
    message = "Your application for "+ scholarship_name + " requires clarification. Please contact the scholarship reviwer at (email)."

    sender ="SFWEAutoNotify"

    Notification.objects.create(title=title, message=message, sender=sender, recipient=recipient)

    pass


