from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    )


def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)



# Job table/Entity
class Job(models.Model):
    tittle = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to= image_upload)
    
    # https://docs.djangoproject.com/en/4.1/ref/forms/fields/
    # Short label for something, containing only letters, numbers, 
    # underscores or hyphens. They’re generally used in URLs.
    slug = models.SlugField(blank=True, null=True) # https://www.jobboard.      
    # com/add-the-slug-field-inside-django-model/
    
    # Relations
    category = models.ForeignKey('Category', on_delete=models.CASCADE, 
    default=1) # one to many relationship
    owner = models.ForeignKey(User, related_name='job_owner',
    on_delete=models.CASCADE)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.tittle) # slugify will take the title and replace the space with underscore (job-board-software-engineer)
        super(Job,self).save(*args, **kwargs)
       
       
    def __str__(self):
        return self.tittle
    
    class Meta:
        ordering = ['-published_at']
        db_table = 'jobs_table'

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category_table'

# Apply form  
class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=100000)
    created_at = models.DateTimeField(auto_now=True)


    # Relations
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
   
   
    def __str__(self):
        return self.name

    class Meta:
        db_table = "application_table"


                                                       