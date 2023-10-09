from django.urls import path
from teachers.views import TeachersListView

urlpatterns = [
    path('', TeachersListView.as_view() , name='teachers'),

]