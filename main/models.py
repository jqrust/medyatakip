from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user    

class User(AbstractBaseUser,PermissionsMixin):    
    email = models.EmailField(verbose_name=('email address'), max_length=255,unique=True)
    is_staff = models.BooleanField(('staff status'), default=False,
        help_text=('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(('active'), default=True,
        help_text=('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = ('user')
        verbose_name_plural = ('users')        
        ordering = ['email']

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fee = models.IntegerField(blank=False,null=False)

    intervals = (
        ('D' , 'Daily'),
        ('W' , 'Weekly'),
        ('M' , 'Monthly'),
        ('Y' , 'Yearly'),
    )
    report_interval = models.CharField(max_length=1,choices=intervals,default='M')
    date_last_report = models.DateTimeField(blank=True)
    class Meta:
        abstract = True
class Company(Customer):
    company_name = models.CharField(max_length=64)
    tax_no = models.IntegerField(unique=True)
   
class Person(Customer):
    first_name = models.CharField(max_length=64)
    last_name  = models.CharField(max_length=64) 
    tc_id = models.IntegerField(unique=True)
    
class Surveyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name  = models.CharField(max_length=64)

class Outlet(models.Model):
    name = models.CharField(max_length=64)    
    
class Publication(models.Model):
    source = models.ForeignKey(Outlet,on_delete=models.PROTECT)  
    date_published= models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name=('İçerik')) 
    #tags = models.ManyToManyField(Tags)

class Question(models.Model):
    name = models.CharField(max_length=255)

class Answers(models.Model):
    text = models.CharField(max_length=128)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

class Survey(models.Model):
    ask_count = models.IntegerField(default=0)
    surveyors = models.ForeignKey(Surveyer,models.DO_NOTHING)
    fee = models.IntegerField(default=5000)
    questions = models.ForeignKey(Question,models.DO_NOTHING)