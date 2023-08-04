from rest_framework import serializers

from .models import Area, Region, Measurements


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        # para mostrar campos especificos de mis modelos
        # fields = ['id', 'name', 'owner', '']
        fields = '__all__'  # muestra todos los campos de mi modelo


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'
