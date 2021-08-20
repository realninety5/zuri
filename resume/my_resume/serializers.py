from my_resume.models import Education, Experience, Skill, About
from rest_framework import serializers

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['body']


class ExperienceSerializer(serializers.ModelSerializer):
    exp = serializers.SlugRelatedField(many=True, 
                read_only=True, slug_field='jobs_done')

    class Meta:
        model = Experience
        fields = ['compro', 'date_start', 'date_stop', 'comp', 'position', 'location', 'exp']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['school', 'course']

class SkillSerializer(serializers.ModelSerializer):
    skill_set = serializers.SlugRelatedField(many=True, 
                read_only=True, slug_field='skill')

    class Meta:
        model = Skill
        fields = ['name', 'skill_set']