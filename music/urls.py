from django.urls import path
from music import views


urlpatterns = [
path("",views.index ,name="index"),
# path("song/<slug:slug>",views.get_song,name="get-song"),
path("profile/",views.get_my_songs,name="mysongs"),
path("add-song/",views.add_song,name="add-song"),
path("del-song/<int:id>",views.del_song,name="del-song")
]

