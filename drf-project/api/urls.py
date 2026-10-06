from django.urls import include, path
from rest_framework.routers import DefaultRouter

from students.urls import urlpatterns

from . import views

router = DefaultRouter()
router.register("employees", views.EmployeeViewSet, basename="employee")

urlpatterns = [
    path("students/", views.studentView),
    path("student/<int:pk>", views.studentDetailView),
    # path('employees/', views.Employees.as_view()),
    # path('employee/<int:pk>', views.EmployeeDetail.as_view())
    path("", include(router.urls)),
    path("blogs/", views.BlogsView.as_view()),
    path("comments/", views.CommentsView.as_view()),
    path("blogs/<int:pk>", views.BlogDetailedView.as_view()),
    path("comments/<int:pk>", views.CommentDetailedView.as_view()),
]
