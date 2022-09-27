from django.urls import path
from measurement.views import AllSensors, ChangeSensor, CreateMeasurement, CreateSensor, DetailedSensors
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateSensor.as_view(), name='create_sensor'),
    path('change_sensor/<pk>/', ChangeSensor.as_view(), name='change_sensor'),
    path('measurements/', CreateMeasurement.as_view(), name='create_measurement'),
    path('all_sensors/', AllSensors.as_view(), name='all_sensors'),
    path('detailed_sensors/<pk>/', DetailedSensors.as_view(), name='detailed_sensors')

]
