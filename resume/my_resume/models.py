from django.db import models

# Create your models here.

class About(models.Model):
    body = models.TextField()

    def __str__(self):
        return f'{self.body}'

class Experience(models.Model):
    compro = models.CharField(max_length=20, null=True, blank=True)
    date_start = models.DateField()
    date_stop = models.DateField()
    comp = models.BooleanField(default=False)
    position = models.CharField(max_length=30, null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.compro}'


class ExperienceJobs(models.Model):
    exp = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name="exp")
    jobs_done = models.TextField()


    def __str__(self) -> str:
        return f'{self.jobs_done}'


class Education(models.Model):
    school = models.CharField(max_length=30)
    course = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.school}'


class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class SkillSet(models.Model):
    skill_set = models.ForeignKey(Skill, related_name="skill_set", on_delete=models.CASCADE)
    skill = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.skill}'
