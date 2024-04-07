from django.db import models

# Create your models here.
class Feedback (models.Model):
    feedback_id = models.IntegerField()
    team_id = models.IntegerField()
    review_comment = models.TextField(max_length=800)
    team_member_id = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    good_feedback = models.TextField(max_length=800, default=None)
    bad_feedback = models.TextField(max_length=800, default=None)
    other_feedback = models.TextField(max_length=800, default=None)
    is_open = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TeamMember (models.Model):
    team_member_name = models.CharField(max_length=200)
    team_id = models.IntegerField()
    team_member_id = models.IntegerField()
    feedback = models.ForeignKey(
        'Feedback', 
        on_delete=models.CASCADE,
        related_name='team_member'
        )

    def __str__(self):
        return self.name
    
    # supporter = models.CharField(max_length=200)