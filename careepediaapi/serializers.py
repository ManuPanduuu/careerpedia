from rest_framework import serializers
from .models import Bachelor, Intermediate


class BachelorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bachelor
        fields = ('id', 'serial', 'stream', 'course', 'description', 'eligibility', 'education_level', 'serial', 'government_recognition',
                  'career_opportunities_one', 'career_opportunities_two', 'career_opportunities_three', 'career_opportunities_four',
                  'career_opportunities_five', 'career_opportunities_six', 'subject_one', 'subject_two','subject_three','subject_four','subject_five',
                  'subject_six','subject_seven','subject_eight','subject_nine','subject_ten','subject_eleven','subject_twelve','subject_thirteen',
                  'subject_fourteen','subject_fifteen','subject_sixteen','subject_seventeen')


class IntermediateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Intermediate
        fields = ('id', 'serial', 'stream', 'course', 'description', 'eligibility', 'education_level', 'serial', 'government_recognition',
                  'career_opportunities_one', 'career_opportunities_two', 'career_opportunities_three', 'career_opportunities_four',
                  'career_opportunities_five', 'career_opportunities_six', 'subject_one', 'subject_two','subject_three','subject_four','subject_five',
                  'subject_six','subject_seven','subject_eight','subject_nine','subject_ten','subject_eleven','subject_twelve','subject_thirteen',
                  'subject_fourteen','subject_fifteen','subject_sixteen','subject_seventeen')
