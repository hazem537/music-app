from django.shortcuts import render ,redirect
from music.models import Song
from music.forms import SongForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import SongFilter
# from django.conf import settings

# Create your views here.
# from background_task import background
@login_required
def index(request):

   
    # songs =Song.objects.filter(user = request.user)
    query_set =Song.objects.filter(public = True)
    public_songs = SongFilter(request.GET, queryset=query_set)
    return render(request,"music/index.html",{"public_songs":public_songs})

@login_required
def get_my_songs(request):
    try:
        query_set= Song.objects.filter(user =request.user)
        song =SongFilter(request.GET,queryset=query_set)
    except Exception as e :
        print(e)
    return render(request,"music/profile.html",{"songs":song})

@login_required
def add_song (request):
    if request.method == "POST":

        song_form = SongForm(request.POST,request.FILES)
        if song_form.is_valid():
            # CreateSongThread(form=song_form).start()
            song =song_form.save(commit=False)
            song.user = request.user
            song.save()
            return redirect ("index")
        else:
            return render(request ,"music/add_song.html",{"form":song_form})
    song_form = SongForm()
    return render(request ,"music/add_song.html",{"form":song_form})

@login_required
def del_song(request ,id):
    try:
        song = Song.objects.get(id = id)
        song.delete()
    except Exception as e:
        print(e)
    
    return redirect("index")