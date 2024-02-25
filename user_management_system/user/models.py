from django.db import models

class Organization(models.Model):
    org_id = models.BigAutoField(primary_key=True, unique=True)
    org_name = models.CharField(max_length=255, blank=False, default='')
    billing = models.CharField(max_length=255, blank=False, default='')
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = True
        db_table = 'organization'

class Role(models.Model):
    role_id = models.BigAutoField(primary_key=True, unique=True)
    role_name = models.CharField(max_length=255, blank=False, default='')
    org_id = models.ForeignKey(Organization, related_name="organization", on_delete=models.CASCADE, null=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = True
        db_table = 'role'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=False,null=True)
    password = models.CharField(max_length=50)
    status = models.SmallIntegerField(default=0)
    role_id = models.ForeignKey(Role, related_name="role", on_delete=models.CASCADE,null=True, default=None)
    org_id = models.ForeignKey(Organization, related_name="organization2", on_delete=models.CASCADE, null=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = True
        db_table = 'user'
