from django.contrib import admin
from app.models import Skill, MicroSkill, SkillMicroSkills, MicroSkillPrerequisite
from app.models import Domain, Industry, Company, Job, JobSkills

admin.site.register(Skill)
admin.site.register(MicroSkill)
admin.site.register(SkillMicroSkills)
admin.site.register(MicroSkillPrerequisite)
admin.site.register(Domain)
admin.site.register(Industry)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobSkills)