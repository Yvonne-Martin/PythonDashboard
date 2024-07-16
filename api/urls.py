from django.urls import path
from .views import StudentListView
from .views import ClassroomListView
from .views import TeachersListView
from .views import ClassPeriodListView
from .views import CoursesListView





urlpatterns = [ 
    path ("student/",StudentListView.as_view(),name="student_list_view"),
    path ("class/",ClassPeriodListView.as_view(),name="class_list_view"),
    path ("teacher/", TeachersListView.as_view(),name="teacher_list_view"),
    path ("classroom/",ClassroomListView.as_view(),name="classroom_list_view"),
    path ("course/",CoursesListView.as_view(),name="courses_list_view"),



]

