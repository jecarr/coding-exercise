from django.urls import path

from exercise import views

urlpatterns = [
    # REST endpoint to return 'Hello World'
    path("hello/", views.hello_world, name="hello"),
    # REST endpoints to return combination of arguments
    path("add-numbers/<num1>/<num2>/", views.add_numbers, name="add_numbers"),
    path("join-strings/<s1>/<s2>/", views.join_words, name="join_words"),
]
