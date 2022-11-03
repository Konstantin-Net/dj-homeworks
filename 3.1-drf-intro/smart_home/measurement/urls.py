from django.urls import path

from measurement.views import ListSensors, OneSensor, CreateMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListSensors.as_view()),
    path('sensors/<pk>', OneSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view())
]
