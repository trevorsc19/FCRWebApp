from django.db import models
from users.models import CustomUser
import uuid

# Create your models here.
class Audio(models.Model):
    # By default, Django gives each model the following field
    # id = models.AutoField(primary_key=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # many to one relationship
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        null=True
    )
    # If you are using the default FileSystemStorage, the string value will be appended to your MEDIA_ROOT path to form the location on the local filesystem where uploaded files will be stored
    name = models.CharField(max_length=128)
    # audio_file = models.FileField(upload_to='audio/', blank=False, null=True)
    s3_url = models.URLField(max_length=500, default="RANDOM TEXT")

    class Meta: 
        db_table="audio_files_table"
    
class Metrics(models.Model):
    # By default, Django gives each model the following field
    # id = models.AutoField(primary_key=True)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    audio_file = models.OneToOneField(
        Audio, 
        on_delete=models.CASCADE, 
        null=True
    )

    pronunciation_posteriori_probability_score_percentage = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    syllables_count = models.IntegerField(null=True)
    pauses_count = models.IntegerField(null=True)
    rate_of_speech = models.IntegerField(null=True)
    articulation_rate = models.IntegerField(null=True)
    # speaking duration without pauses
    speaking_duration = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    # speaking duration with pauses
    original_duration = models.DecimalField(null=True, decimal_places=2, max_digits=4)



    
    class Meta:
        db_table="metrics_table"