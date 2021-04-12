from django.urls import path

from . import views
#all the urls of the website are stored here

urlpatterns=[
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout, name="logout"),

    path('student_list/', views.student_list, name="student_list"),
    path('student_form/', views.student_form, name="student_form"),
    path('<int:id>',views.student_form, name="student_update"),
    path('delete/<int:id>',views.student_delete, name="student_delete"),
    
    path('task_form/', views.task_form, name="task_form"),
    path('task_list/', views.task_list, name='task_list'),
    path('<int:id>/', views.task_form,name='task_update'),
    path('delete_task/<int:id>', views.task_delete, name='task_delete'),

    path('studentgrades_list/',views.studentgrades_list, name="studentgrades_list"),
    path('studentgrades_form/',views.studentgrades_form, name="studentgrades_form"),
    path('delete_studentgrades/<int:id>', views.studentgrades_delete, name='studentgrades_delete'),

    path('gradebook/<str:pk_test>/', views.gradebook, name="gradebook"),
    path('evi_form/<str:pk>/', views.create_evidencerecord, name='evi_form'), 
    path('evi_update/<str:pk>/', views.update_evidencerecord,name='evi_update'),
    path('delete_evi/<str:pk>/', views.delete_evidencerecord, name='evi_delete'),

    path('category_form/<str:pk>/', views.create_category, name='category_form'),
    path('category_delete/<str:pk>/', views.delete_category, name='category_delete'),

    path('additional_form/<str:pk>/', views.create_additional, name='additional_form'),
    path('additional_delete/<str:pk>/', views.delete_additional, name='additional_delete'),

]
