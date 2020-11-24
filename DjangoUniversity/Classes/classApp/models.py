from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    title = models.CharField(max_length=100, default='')
    course_number = models.IntegerField(default='')
    instructor_name = models.CharField(max_length=50, default='')
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title


djangoClasses.objects.create(title="American History Through the Civil War", course_number=1,
                             instructor_name="Barry Weinstein", duration=2.15)
djangoClasses.objects.create(title="Introduction to Python", course_number=2, instructor_name="Lucie Marie",
                             duration=1.0)
djangoClasses.objects.create(title="Black and White Photography", course_number=3, instructor_name="Zack Pont",
                             duration=1.5)


