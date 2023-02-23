from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from measurements.models import Sensor, Measurement
from measurements.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorViewSet(APIView):
    def post(self, request):
        name = self.request.query_params.get('name')
        value = self.request.query_params.get('value')
        n = Sensor(name=name, value=value)
        n.save()

    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def put(self, request):
        id = self.request.query_params.get('id')
        name = self.request.query_params.get('name')
        value = self.request.query_params.get('value')
        n = Sensor(id=id, name=name, value=value)
        n.save()


class MeasurementViewSet(APIView):
    def post(self, request):
        id = self.request.query_params.get('id')
        value = self.request.query_params.get('value')
        n = Measurement(sensor_id=id, value=value)
        n.save()

    def get(self, request):
        id = self.request.query_params.get('id', 1)
        sensors = Sensor.objects.filter(id=id)
        print(sensors.query)
        ser = SensorDetailSerializer(sensors, many=True)
        return Response(ser.data)

