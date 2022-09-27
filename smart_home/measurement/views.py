# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from functools import partial
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.serializers import DetailedSensorSerializer, MeasurementSerializer, SensorSerializer
from rest_framework.response import Response
from measurement.models import Sensor

class CreateSensor(CreateAPIView):
    
    def post(self, request):
        sensor = request.data
        serializer = SensorSerializer(data=sensor)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('ok')

class ChangeSensor(RetrieveUpdateAPIView):

    def patch(self, request, pk):
        updated_object = Sensor.objects.filter(pk=pk).first()
        sensor = request.data
        serializer = SensorSerializer(updated_object, data=sensor, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('ok')

class CreateMeasurement(CreateAPIView):

    def post(self, request):
        measurement = request.data
        serializer = MeasurementSerializer(data=measurement)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('ok')

class AllSensors(ListCreateAPIView):
    
    def get(self, request):
        queryset = Sensor.objects.all()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

class DetailedSensors(ListCreateAPIView):

    def get(self, request, pk):
        queryset = Sensor.objects.filter(pk=pk)
        serializer = DetailedSensorSerializer(queryset, many=True)
        return Response(serializer.data)
