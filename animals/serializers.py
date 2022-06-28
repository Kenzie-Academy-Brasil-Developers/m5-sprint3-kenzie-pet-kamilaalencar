from rest_framework import serializers

from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer

from groups.models import Group
from characteristics.models import Characteristic
from animals.models import Animal

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
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

    def update(self, instance:Animal, validated_data:dict):
        no_editable_keys = ('sex','group',)
        for key, value in validated_data.items():
            if key in no_editable_keys:
                raise KeyError(key)

            if key == 'characteristics' and type(value) == list:
                for characteristic in value:
                    characteristics_characteristic, created = Characteristic.objects.get_or_create(**characteristic)
                    instance.characteristics.add(characteristics_characteristic)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
        