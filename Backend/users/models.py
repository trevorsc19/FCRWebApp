from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import CustomUserManager

# AbstractUserModel provides the core implementation of a user model, including hashed passwords and tokenized password resets
class CustomUser(AbstractBaseUser):

    #username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150, 
        unique=True,
        help_text=('Required. 150 Characters or fewer'),
        #validators=[username_validator],
        error_messages={
            'unique': 'A user with that username already exists'
        }
    )

    email = models.EmailField('email address', blank=False)

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site'
    )

    is_superuser = models.BooleanField(
        'Superuser status',
        default = False, 
        help_text='Whether the user is a superuser'
    )

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = CustomUserManager()

    # field name on the User that will be used as the email field
    EMAIL_FIELD = 'email'
    # field name on the user model that is used as the unique identifier
    USERNAME_FIELD = 'username'
    # A list of the field names that will be prompted for when creating a user via the createsuperuser command
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'auth_user'