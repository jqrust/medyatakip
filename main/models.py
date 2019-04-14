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
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    fee = models.IntegerField(blank=False,null=False)

    intervals = (
        ('D' , 'Daily'),
        ('W' , 'Weekly'),
        ('M' , 'Monthly'),
        ('Y' , 'Yearly'),
    )
    report_interval = models.CharField(max_length=1,choices=intervals,default='M')
    date_last_report = models.DateTimeField(blank=True,null=True)
    class Meta:
        abstract = True
class Company(Customer):
    company_name = models.CharField(max_length=64)
    tax_no = models.IntegerField(unique=True)
    def __str__(self):
        return self.company_name
   
class Person(Customer):
    first_name = models.CharField(max_length=64)
    last_name  = models.CharField(max_length=64) 
    tc_id = models.IntegerField(unique=True)
    def get_name(self):
        return self.first_name +' '+ self.last_name
    def __str__(self):
        return self.get_name()
    
class Surveyor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name  = models.CharField(max_length=64)
    def get_name(self):
        return self.first_name +' '+ self.last_name
    def __str__(self):
        return self.get_name()

class Outlet(models.Model): 
    name = models.CharField(max_length=64)   
    def __str__(self):
        return self.name 
    
class Publication(models.Model):
    header = models.CharField(max_length=128)
    source = models.ForeignKey(Outlet,on_delete=models.PROTECT)  
    date_published= models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name=('İçerik')) 
    releated_to = models.ManyToManyField(User,related_name='publications')
    #tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.header

class Survey(models.Model):
    name = models.CharField(max_length=128)
    ask_count = models.IntegerField(default=0)
    surveyors = models.ManyToManyField(Surveyor,related_name='surveys',blank=True)
    fee = models.IntegerField(default=5000)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=255)
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Answer(models.Model):
    text = models.CharField(max_length=128)
    question = models.ForeignKey(Question,related_name="answer_set",on_delete=models.CASCADE)
    def __str__(self):
        return self.text

