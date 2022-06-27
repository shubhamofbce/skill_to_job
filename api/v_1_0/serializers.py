from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Skill, Job, MicroSkill, MicroSkillPrerequisite
from app.models import Domain, Industry, Company, Job, JobSkills, SkillMicroSkills

# Add all fields in all serialisers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MicroSkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroSkill
        exclude = ['deleted', 'created', 'updated', 'deleted_by_cascade']


class MicroSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroSkill
        exclude = ['deleted', 'created', 'updated', 'deleted_by_cascade']


class SkillMicroSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillMicroSkills
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']


class MicroSkillPrerequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroSkillPrerequisite
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']


class JobSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkills
        exclude = ['id', 'deleted', 'created', 'updated', 'deleted_by_cascade']
