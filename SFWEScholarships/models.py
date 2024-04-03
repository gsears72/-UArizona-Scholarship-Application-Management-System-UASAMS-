from Student.models import Student

# Create your models here.
class Application(models.Model):
    STATUS = (
        ('Submitted', 'Submitted'), 
        ('In Reivew', 'In Review'), 
        ('Approved', 'Approved'), 
        ('Rejected', 'Rejected')
    )
    
    SR_STATUS = (
        ('In Reivew', 'In Review'),
        ('Approved', 'Approved'), 
        ('Rejected', 'Rejected')
    )
    
    
    

    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stauts = models.CharField(max_length = 20, choices = STATUS, default = 'Submitted')
<<<<<<< HEAD

    def __str__(self):
        return f"Application for {self.scholarship.scholarship_name} by {self.student.username}"
=======
    personal_statement = models.TextField()
    sr_status = models.CharField(max_length = 20, choices = SR_STATUS, default = 'In Review')
    score = models.IntegerField(max_length = 3, default = 0)
    
>>>>>>> 40afdef28ebf60d831914b7e3f985d9233fa0007
