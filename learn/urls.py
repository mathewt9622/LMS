

from django.urls import path




from . import views


urlpatterns = [
    path('', views.home ,name="home"),
    
    path('my/', views.myCourses, name='myCourses'),
    path('facultyCourses/', views.facultyCourses, name='facultyCourses'),
    path('register/', views.std_register, name='std_register'),
    path('login/', views.std_login, name='std_login'),
    path('logout/', views.std_logout, name='std_logout'),
    path('student/', views.guestStudent, name='guestStudent'),
    path('teacher/', views.guestFaculty, name='guestFaculty'),
    path('courses/', views.courses, name='courses'),
    path('my/<int:code>/', views.course_page, name='course'),
    path('faculty/<int:code>/', views.course_page_faculty, name='faculty'),
    path('addannouncement/<int:code>/', views.addAnnouncement, name='addAnnouncement'),
    path('delannounecement/<int:code>/<int:id>/', views.deleteAnnouncement, name='deleteAnnouncement'),
    path('editannounecement/<int:code>/<int:id>/', views.editAnnouncement, name='editAnnouncement'),
    path('update/<int:code>/<int:id>/', views.updateAnnouncement, name='updateAnnouncement'),
    path('course-material/<int:code>/', views.addCourseMaterial, name='addCourseMaterial'),
    path('course-material/<int:code>/<int:id>/', views.deleteCourseMaterial, name='deleteCourseMaterial'),
    path('profile/<str:id>/', views.profile, name='profile'),
    path('changePasswordPrompt/', views.changePasswordPrompt,name='changePasswordPrompt'),
    path('changePhotoPrompt/', views.changePhotoPrompt, name='changePhotoPrompt'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('changePasswordFaculty/', views.changePasswordFaculty,name='changePasswordFaculty'),
    path('changePhoto/', views.changePhoto, name='changePhoto'),
    path('changePhotoFaculty/', views.changePhotoFaculty,name='changePhotoFaculty'),
    path('facultyProfile/<str:id>/', views.profile, name='profile_faculty'),
    path('search/', views.search, name='search'),
    
] 