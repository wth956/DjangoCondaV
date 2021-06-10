from django.shortcuts import render
from .models import Movie, Rating #high_rate, top_rate
from operator import itemgetter #high_rate, top_rate
from .WebView import WebView #high_rate, top_rate
from .movie_forms import MovieSelectForm    #movie_also_like
from .movie_forms import MovieUserInputForm #movie_also_dislike
from .movie_forms import MovieUserNameForm  #movie_rcmd_exist_user
from .recommender import Recommender        #movie_rcmd_exist_user
from django.shortcuts import get_object_or_404 #movie_detail
from .movie_forms import RatingForm #add_rating
from datetime import datetime #add_rating
from django.contrib.auth.decorators import login_required #add_rating
from django.contrib.auth.models import User  #add_rating
from django.http import HttpResponseRedirect #add_rating
from django.core.urlresolvers import reverse #add_rating
import collections #OrderedDict
import json #movie_detail 

## 產生一個物件 相似度公式:cosine 最近鄰居數:3  推薦項目數:5
r = Recommender(3,'cosine',5) # r is a class public variable
v = WebView() # v is a class public variable
movie_list_Box2 = ['a0101.jpg', 'a0102.jpg', 'a0103.jpg', 'a0104.jpg', 'a0105.jpg', 'a0106.jpg', 'a0107.jpg', 'a0108.jpg', 'a0109.jpg', 'a0110.jpg',
                       'a0111.jpg', 'a0112.jpg', 'a0113.jpg', 'a0114.jpg', 'a0115.jpg', 'a0116.jpg', 'a0117.jpg', 'a0118.jpg', 'a0119.jpg', 'a0120.jpg',
                       'a0121.jpg', 'a0122.jpg', 'a0123.jpg', 'a0124.jpg', 'a0125.jpg', ]

# from django.contrib.auth.models import User
def base(request):
    movie_list = Movie.objects.order_by('name')
    movie_list_Box = []
    
    for item in movie_list:
        movie_list_Box.append( (item.name))
    # print (movie_list_Box2)
    list_combine = zip(movie_list, movie_list_Box2)
    # movie_list_test = Movie.objects.order_by('name')
    # print( zip(movie_list, movie_list_Box2) )
    return render(request, 'home.html', {'moviedata': list_combine})

def high_rate(request):
    movie_list = Movie.objects.all()
    high_rate_movie = []
    for b in movie_list:
        # print(b.id, b.name, b.average_rating()) # 101 Alien 3.4545454545454546 
        high_rate_movie.append(  (b.id, b.name, b.average_rating())  )
    sorted_top_movie = sorted(high_rate_movie, key=itemgetter(2),  reverse=True)
    temp_context = {'result': sorted_top_movie[:5]} 

    answer = v.add_Index( temp_context )
    context = {
        'result': answer
    } 
    print(answer)
    return render(request, 'show_message_high_rate.html', context)
    
def top_rate(request):
    movie_list = Movie.objects.all()
    top_movie = []
    for b in movie_list:
        print(b.name,b.rating_set.count())
        top_movie.append(  (b.id, b.name, b.rating_set.count(), b.average_rating())  )
    sorted_top_movie = sorted(top_movie, key=itemgetter(2),  reverse=True)
    temp_context = {'result': sorted_top_movie[:5]} 
    answer = v.add_Index( temp_context )
    context = {
        'result': answer
    }
    return render(request, 'show_message_top_rate.html', context)

def movie_also_like(request):
    answer=''
    if request.method =='POST':
        myform = MovieSelectForm(request.POST)
        if myform.is_valid():
            movie_name = myform.cleaned_data['movie_name']
            answer = r.also_like(movie_name)
    else:
        myform = MovieSelectForm()
    return render(request, 'movie_also_like.html', {'form':myform, 'answer':answer})

def movie_also_dislike(request):
    answer=''
    if request.method =='POST':
        myform = MovieSelectForm(request.POST)
        if myform.is_valid():
            movie_name = myform.cleaned_data['movie_name']
            answer = r.also_dislike(movie_name)
    else:
        myform = MovieSelectForm()

    return render(request, 'movie_also_dislike.html',
        {'form':myform, 'answer':answer})

def movie_rcmd_temporary_user(request):
    neighbors=''
    answer=''
    if request.method == 'POST':
        form = MovieUserInputForm(request.POST)
               
        if form.is_valid():
            ratings={}            
            movie1 = form.cleaned_data['movie1']
            movie2 = form.cleaned_data['movie2']           
            movie3 = form.cleaned_data['movie3']
            movie4 = form.cleaned_data['movie4']
            movie5 = form.cleaned_data['movie5']
            movie6 = form.cleaned_data['movie6']
            movie7 = form.cleaned_data['movie7']
            movie8 = form.cleaned_data['movie8']
            movie9 = form.cleaned_data['movie9']
            movie10 = form.cleaned_data['movie10']
            movie11 = form.cleaned_data['movie11']
            movie12 = form.cleaned_data['movie12']
            movie13 = form.cleaned_data['movie13']
            movie14 = form.cleaned_data['movie14']
            movie15 = form.cleaned_data['movie15']
            movie16 = form.cleaned_data['movie16']
            movie17 = form.cleaned_data['movie17']
            movie18 = form.cleaned_data['movie18']
            movie19 = form.cleaned_data['movie19']
            movie20 = form.cleaned_data['movie20']
            movie21 = form.cleaned_data['movie21']
            movie22 = form.cleaned_data['movie22']
            movie23 = form.cleaned_data['movie23']
            movie24 = form.cleaned_data['movie24']
            movie25 = form.cleaned_data['movie25']

            if movie1 != '-1':
                ratings['Alien']= float(movie1)
            if movie2 != '-1':
                ratings['Avatar']= float(movie2)
            if movie3 != '-1':
                ratings['Blade Runner']= float(movie3)
            if movie4 != '-1':
                ratings['Braveheart']= float(movie4)
            if movie5 != '-1':
                ratings['Dodgeball']= float(movie5)
            if movie6 != '-1':
                ratings['Forest Gump']= float(movie6)
            if movie7 != '-1':
                ratings['Gladiator']= float(movie7)
            if movie8 != '-1':
                ratings['Jaws']= float(movie8)
            if movie9 != '-1':
                ratings['Kazaam']= float(movie9)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)
            if movie10 != '-1':
                ratings['Lord of the Rings']= float(movie10)


            #ratings={'蘇打綠':float(movie1),'五月天':float(movie2)}
            if ratings:
                user_name = 'unknown'
                r.adduser(user_name, ratings)
                answer = r.recommend(user_name)
                neighbors= r.getNearestNeighbor(user_name) 
            else:
                answer=['沒有資料！']
                neighbors=['沒有資料！']
            
                   
    else:
        form = MovieUserInputForm()
    return render(request, 'movie_rcmd_temporary_user.html', 
        {'form':form, 'answer':answer, 'neighbors': neighbors})

def movie_rcmd_exist_user( request ):
    ans = ''
    neighbor = ''

    if request.method == 'POST':
        myform = MovieUserNameForm( request.POST )
        print(MovieUserNameForm( request.POST ))
        if myform.is_valid():
            name = myform.cleaned_data['user_name']
            ans =  r.recommend( name )
            neighbor = r.getNearestNeighbor( name )
    else:
        myform = MovieUserNameForm()
    return render(request, 'movie_rcmd_exist_user.html', {'form': myform, 'answer': ans , 'neighbor' : neighbor})

def movie_rcmd_to_user(request):
    r.loadMovieFromDB() 
    answer=''
    neighbors=''
    user_name = request.user.username
    answer = r.recommend(user_name)
    neighbors= r.getNearestNeighbor(user_name)
    return render(request, 'movie_rcmd_to_user.html', {'answer':answer, 'neighbors': neighbors})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = RatingForm()

    movieVIS = movie.ratingstar_counter() # Counter({4.0: 4, 2.0: 3, 3.0: 2, 5.0: 2})
    movieVISdict = dict(movieVIS)  # {2.0: 3, 3.0: 2, 4.0: 4, 5.0: 2}
    movieVISOD = collections.OrderedDict(sorted(movieVISdict.items())) # ([(2.0, 3), (3.0, 2), (4.0, 4), (5.0, 2)])
    movieVISlst = list(movieVISOD.items())  # [(2.0, 3), (3.0, 2), (4.0, 4), (5.0, 2)]
    resultlst = []
    # iterating over the tuples lists
    for (key, value) in movieVISlst:
        tmpdict ={}
        tmpdict['star'] = key
        tmpdict['counts'] = value
        resultlst.append(tmpdict)
        # print(resultlst)  # [{'counts': 3, 'star': 2.0}, {'counts': 2, 'star': 3.0}, {'counts': 4, 'star': 4.0}, {'counts': 2, 'star': 5.0}]
    return render(request, 'movie_detail.html', {'movie': movie,'form': form, 'moviename':movie_list_Box2, 'piedata':json.dumps(resultlst)})



@login_required
def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id) #取得樂團物件
    form = RatingForm(request.POST) #取得使用者填寫的表單
    myuser = User.objects.get(pk = request.user.id) #取得當前login使用者
    # myuser = User.objects.get(pk = 1) #取得當前login使用者    
    #myuser = request.user #這種寫法不可以 雖然都是user但是格式不同
    
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        
        newRate = Rating()
        newRate.movie = movie
        newRate.user = myuser
        newRate.rating = rating
        newRate.comment = comment
        newRate.pub_date = datetime.now()
        newRate.save()

        # r.loadBandFromDB() # data內容依據資料庫最新資料

        #呼叫 band_detail 程式(定義在urls.py)
        return HttpResponseRedirect(reverse('movie_detail', args = (movie_id, )))

    return render(request, 'movie_detail.html', {'movie':movie, 'form':form})

