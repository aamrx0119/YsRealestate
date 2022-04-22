from . import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('reset/', views.Password_Reset_view.as_view(),name='reset_password'),
    path('reset/done/', views.Password_Reset_Done.as_view(),name='password_reset_done'),
    path('confirm/reset/<uidb64>/<token>/', views.Password_Reset_Confirm.as_view(),name='password_reset_confirm'),
    path('confirm/done/', views.Password_Reset_Complete.as_view(),name='password_reset_complete'),
    path('signup/',views.Signup_Acc,name='signup_view'),
    path('login/',views.Login_Acc,name='login_view'),
    path('logout/',views.Logout_Acc,name='logout_view'),
    path('profile/dashboard/<int:id>/',views.Dashboard_Acc,name='dashboard_view'),
    path('profile/dashboard-form/<int:id>/',views.Form_page,name='form_page'),
    path('profile/dashboard-Change/p/<int:id>/',views.Change_profile_view,name='change_profile'),
    path('chaking/house/',views.Checking_houses,name='chacking_house'),
    path('manage/house/<int:id>/',views.Manage_house,name='manage_house'),
]
