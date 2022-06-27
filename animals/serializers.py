from rest_framework import serializers

from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer

from groups.models import Group
from characteristics.models import Characteristic
from animals.models import Animal

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)



    def create(self, validated_data:dict):
        group_data = validated_data.pop('group')
        characteristics_data = validated_data.pop('characteristics')

        group, created = Group.objects.get_or_create(**group_data)
        animal = Animal.objects.create(**validated_data, group = group)

        for characteristic in characteristics_data:
            c, created = Characteristic.objects.get_or_create(**characteristic)
            animal.characteristics.add(c)
        return animal
