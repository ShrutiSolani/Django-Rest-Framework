from rest_framework import serializers
from .models import Student

#Validators
def start_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError('Should start with s')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators = [start_with_s])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

#create 
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
#update
    def update(self, instance, validated_data):
        #print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        #print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

#delete
# No need for delete serializer

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'ram' and ct.lower() != 'ayodhya':
            raise serializers.ValidationError('City should by Ayodhya')
        return data