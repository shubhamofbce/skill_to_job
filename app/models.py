from django.db import models
from safedelete.models import SafeDeleteModel


class Skill(SafeDeleteModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    micro_skills = models.ManyToManyField(
        'MicroSkill',
        through='SkillMicroSkills',
        through_fields=('skill', 'microskill')
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MicroSkill(SafeDeleteModel):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    pre_requisite = models.ManyToManyField('self',
                                           through='MicroSkillPrerequisite',
                                           through_fields=('microskill', 'pre_microskill'))

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SkillMicroSkills(SafeDeleteModel):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    microskill = models.ForeignKey(MicroSkill, on_delete=models.CASCADE)
    weight = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill.name + ' ' + self.microskill.name


class MicroSkillPrerequisite(SafeDeleteModel):
    microskill = models.ForeignKey(MicroSkill, on_delete=models.CASCADE)
    pre_microskill = models.ForeignKey(MicroSkill, on_delete=models.CASCADE, related_name='pre_skill')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.microskill.name


class Domain(SafeDeleteModel):
    name = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=2048, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Industry(SafeDeleteModel):
    name = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=2048, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Company(SafeDeleteModel):
    name = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=2048, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Job(SafeDeleteModel):
    title = models.CharField(max_length=256)
    domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, null=True, blank=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    annual_ctc = models.IntegerField(default=0)
    currency = models.CharField(max_length=16, default='INR')
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    relevant_experience_in_months = models.IntegerField()
    overall_experience_in_months = models.IntegerField()
    graduation = models.CharField(max_length=256)
    graduation_institute = models.CharField(max_length=1024)
    post_graduation = models.CharField(max_length=256)
    post_graduation_institute = models.CharField(max_length=256)
    skills = models.ManyToManyField(
        Skill,
        through='JobSkills',
        through_fields=('job', 'skill')
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobSkills(SafeDeleteModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=256)
    weight = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job.title + ' ' + self.skill.name
