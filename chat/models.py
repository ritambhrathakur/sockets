from django.db import models

# Create your models here.


class ChatMessages(models.Model):
    """
    class ChatMessages is created to add the email templates with template fields
    """
    id = models.AutoField(primary_key=True)
    text_name = models.CharField(max_length=30, null=True, blank=True)
    message = models.CharField(max_length=200,null=True, blank=True)
    
    is_active = models.BooleanField(default=True, help_text="user is active")
    is_deleted = models.BooleanField(default=False, help_text="to delete the user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
