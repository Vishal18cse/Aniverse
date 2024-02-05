from django.shortcuts import render ,redirect ,get_object_or_404
from django.contrib.auth import login ,authenticate ,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Anime.models import a_anime , b_anime , c_anime
from trending.models import trending_anime
from recent.models import recently_updated
from top.models import top_airing
from movies.models import anime_movies
from store.models import storage,Wishlist,Favorites
from django.core.paginator import Paginator
from django.http import JsonResponse
from contact.models import Contact
from comment.models import Comment


def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirmpass')
        
        if password != confirm_pass:
            return render(request , 'signup.html' ,{'error' :'Password not matched'})
        
        user = User.objects.create_user(name , email ,password)
        return redirect('login')
    else :
        return render(request , 'signup.html')

def main_login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username = name , password = password)

        if user:
            login(request , user)
            return redirect('index')
        else :
            return render(request , 'login.html' , {'error' : 'Invalid Username or password'})
    else :
        return render(request , 'login.html')

def index(request):
    anime_store = storage.objects.all()
    login = request.user.is_authenticated
    trend = trending_anime.objects.all()
    recent = recently_updated.objects.all()
    top = top_airing.objects.all()
    movies = anime_movies.objects.all()
    one = a_anime.objects.all()
    two = b_anime.objects.all()
    three = c_anime.objects.all()


    if request.method == 'GET':
        search = request.GET.get('search_anime')
        if search !=None :
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            paginator = Paginator(anime_store , 5)
            page_no = request.GET.get("page" , 1)
            result = paginator.get_page(page_no)
            total = result.paginator.num_pages
            context = {
                'data' : result ,
                'login' : login ,
                'page_list' : [n+1 for n in range(total)],
                'one' : one,
                'two' : two,
                'three' : three,

            }
            return render(request , 'search.html' , context)
  
    dic = {
        'trend' : trend,
        'recent' : recent,
        'top' : top,
        'movies':movies,
        'login' : login,
        'one' : one,
        'two' : two,
        'three' : three,
    }    
    return render(request , 'index.html' , dic)

def search(request):
    anime_store = storage.objects.all()
    login = request.user.is_authenticated
    one = a_anime.objects.all()
    two = b_anime.objects.all()
    three = c_anime.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search_anime' , '')
        if search !=None :
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            paginator = Paginator(anime_store , 5)
            page_no = request.GET.get("page" , 1)
            result = paginator.get_page(page_no)
            total = result.paginator.num_pages
            context = {
                    'store' : anime_store , 
                    'login' : login ,
                    'data' : result , 
                    'page_list' : [n+1 for n in range(total)],
                    'one' : one,
                    'two' : two,
                    'three' : three,
                }
            return render(request , 'search.html' , context)
   
    return render(request , 'search.html')    

def logout_view(request):
    logout(request)
    return redirect('index')
 
def anime(request):
    anime_store = storage.objects.all().order_by('name')
    login = request.user.is_authenticated
    one = a_anime.objects.all()
    two = b_anime.objects.all()
    three = c_anime.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search_anime', '')
        if search:
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            paginator = Paginator(anime_store , 5)
            page_no = request.GET.get("page" , 1)
            result = paginator.get_page(page_no)
            total = result.paginator.num_pages
            context = {
                    'store' : anime_store , 
                    'login' : login ,
                    'data' : result , 
                    'page_list' : [n+1 for n in range(total)],
                    'one' : one,
                    'two' : two,
                    'three' : three,
                }
            return render(request , 'search.html' , context)

    paginator = Paginator(anime_store, 10)
    page_no = request.GET.get("page", 1)
    result = paginator.get_page(page_no)
    total = paginator.num_pages
    context = {
        'store': anime_store,
        'data': result,
        'login': login,
        'page_list': [n + 1 for n in range(total)],
        'one' : one,
        'two' : two,
        'three' : three,
    }
    return render(request, 'anime.html', context)
        
def add_to_watchlist(request):
    try:
        product_id = request.POST.get('productId')
        product = get_object_or_404(storage, id=product_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)

        if product not in wishlist.products.all():
            wishlist.products.add(product)
            return JsonResponse({'success': True, 'message': 'Added to Watchlist'}, status=200)
        else:
            return JsonResponse({'success': False, 'message': 'This item is already in Watchlist'}, status=200)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

def add_to_favourite(request):
    try:
        product_id = request.POST.get('productId')
        product = get_object_or_404(storage, id=product_id)
        favorites, created = Favorites.objects.get_or_create(user=request.user)

        if product not in favorites.products.all():
            favorites.products.add(product)
            return JsonResponse({'success': True, 'message': 'Added to Favorites'}, status=200)
        else:
            return JsonResponse({'success': False, 'message': 'This item is already in Favorites'}, status=200)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

def comment(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        user = request.user
        id = request.POST.get('anime_id')
        anime = storage.objects.get(id=id)
        reply = request.POST.get('reply_id')

        if reply == "":
            enq = Comment(message=message , user=user , anime=anime)
        else :
            parent = Comment.objects.get(id=reply) 
            enq = Comment(message=message , user=user , anime=anime , parent=parent)  
        enq.save()     
        return redirect('slug', slug=anime.slug)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def slug(request, slug):
    login = request.user.is_authenticated
    anime_store = storage.objects.all()
   
    if request.method == 'GET':
        search = request.GET.get('search_anime')
        if search is not None:
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            items_per_page = 5
            paginator = Paginator(anime_store, items_per_page)
            page_no = request.GET.get("page", 1)
            result = paginator.get_page(page_no)
            total_pages = result.paginator.num_pages
            context = {
                'data': result,
                'login': login,
                'page_list': [n + 1 for n in range(total_pages)]
            }
            return render(request, 'search.html', context)
    elif request.method == 'POST':
        action_type = request.POST.get('action_type')
        if action_type == 'wishlist':
            return add_to_watchlist(request)
        elif action_type == 'favorites':
            return add_to_favourite(request)
        elif action_type == 'submit':
            return comment(request)
        else:
            return JsonResponse({'error': 'Invalid action type'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)    

    slug_object = get_object_or_404(storage, slug=slug)
    comments = Comment.objects.filter(anime = slug_object ,parent = None).order_by('-created_at')
    replies =  Comment.objects.filter(anime = slug_object).exclude(parent=None).order_by('-created_at')
    dic = {}
    for reply in replies:
        if reply.parent.id not in dic.keys():
            dic[reply.parent.id] = [reply]
        else:
            dic[reply.parent.id].append(reply) 

    context = {'a_slug': slug_object, 
               'login': login , 
               'comments' : comments ,
               'reply' : replies,
               'dic' : dic,
            }           

    return render(request, 'store.html', context)

def t_slug(request, slug):
    login = request.user.is_authenticated
    anime_store = storage.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search_anime')
        if search is not None:
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            paginator = Paginator(anime_store, 5)
            page_no = request.GET.get("page", 1)
            result = paginator.get_page(page_no)
            total = result.paginator.num_pages
            context = {
                'data': result,
                'login': login,
                'page_list': [n + 1 for n in range(total)]
            }
            return render(request, 'search.html', context)

    elif request.method == 'POST':
        action_type = request.POST.get('action_type')
        if action_type == 'wishlist':
            return add_to_watchlist(request)
        elif action_type == 'favorites':
            return add_to_favourite(request)
        else:
            return JsonResponse({'error': 'Invalid action type'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    slug_object = get_object_or_404(storage, slug=slug)
    comments = Comment.objects.filter(anime = slug_object ,parent = None)
    replies =  Comment.objects.filter(anime = slug_object).exclude(parent=None)
    dic = {}
    for reply in replies:
        if reply.parent.id not in dic.keys():
            dic[reply.parent.id] = [reply]
        else:
            dic[reply.parent.id].append(reply) 

    context = {'a_slug': slug_object, 
               'login': login , 
               'comments' : comments ,
               'reply' : replies,
               'dic' : dic,
            }           
    return render(request, 'store.html', context)

def r_slug(request,slug):
    login = request.user.is_authenticated
    anime_store = storage.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search_anime')
        if search is not None:
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            items_per_page = 5
            paginator = Paginator(anime_store, items_per_page)
            page_no = request.GET.get("page", 1)
            result = paginator.get_page(page_no)
            total_pages = result.paginator.num_pages
            context = {
                'data': result,
                'login': login,
                'page_list': [n + 1 for n in range(total_pages)]
            }
            return render(request, 'search.html', context)
    elif request.method == 'POST':
        action_type = request.POST.get('action_type')
        if action_type == 'wishlist':
            return add_to_watchlist(request)
        elif action_type == 'favorites':
            return add_to_favourite(request)
        else:
            return JsonResponse({'error': 'Invalid action type'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)    

    slug_object = get_object_or_404(storage, slug=slug)
    comments = Comment.objects.filter(anime = slug_object ,parent = None)
    replies =  Comment.objects.filter(anime = slug_object).exclude(parent=None)
    dic = {}
    for reply in replies:
        if reply.parent.id not in dic.keys():
            dic[reply.parent.id] = [reply]
        else:
            dic[reply.parent.id].append(reply) 

    context = {'a_slug': slug_object, 
               'login': login , 
               'comments' : comments ,
               'reply' : replies,
               'dic' : dic,
            }           
    return render(request, 'store.html', context)

def top_slug(request,slug):
    login = request.user.is_authenticated
    anime_store = storage.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search_anime')
        if search is not None:
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            items_per_page = 5
            paginator = Paginator(anime_store, items_per_page)
            page_no = request.GET.get("page", 1)
            result = paginator.get_page(page_no)
            total_pages = result.paginator.num_pages
            context = {
                'data': result,
                'login': login,
                'page_list': [n + 1 for n in range(total_pages)]
            }
            return render(request, 'search.html', context)
        
    elif request.method == 'POST':
        action_type = request.POST.get('action_type')
        if action_type == 'wishlist':
            return add_to_watchlist(request)
        elif action_type == 'favorites':
            return add_to_favourite(request)
        else:
            return JsonResponse({'error': 'Invalid action type'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)    

    slug_object = get_object_or_404(storage, slug=slug)
    comments = Comment.objects.filter(anime = slug_object ,parent = None)
    replies =  Comment.objects.filter(anime = slug_object).exclude(parent=None)
    dic = {}
    for reply in replies:
        if reply.parent.id not in dic.keys():
            dic[reply.parent.id] = [reply]
        else:
            dic[reply.parent.id].append(reply) 

    context = {'a_slug': slug_object, 
               'login': login , 
               'comments' : comments ,
               'reply' : replies,
               'dic' : dic,
            }           
    return render(request, 'store.html', context)   

def m_slug(request,slug):
    login = request.user.is_authenticated
    anime_store = storage.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search_anime')
        if search is not None:
            anime_store = storage.objects.filter(name__icontains=search).order_by('name')
            items_per_page = 5
            paginator = Paginator(anime_store, items_per_page)
            page_no = request.GET.get("page", 1)
            result = paginator.get_page(page_no)
            total_pages = result.paginator.num_pages
            context = {
                'data': result,
                'login': login,
                'page_list': [n + 1 for n in range(total_pages)]
            }
            return render(request, 'search.html', context)
    elif request.method == 'POST':
        action_type = request.POST.get('action_type')
        if action_type == 'wishlist':
            return add_to_watchlist(request)
        elif action_type == 'favorites':
            return add_to_favourite(request)
        else:
            return JsonResponse({'error': 'Invalid action type'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)    

    slug_object = get_object_or_404(storage, slug=slug)
    comments = Comment.objects.filter(anime = slug_object ,parent = None)
    replies =  Comment.objects.filter(anime = slug_object).exclude(parent=None)
    dic = {}
    for reply in replies:
        if reply.parent.id not in dic.keys():
            dic[reply.parent.id] = [reply]
        else:
            dic[reply.parent.id].append(reply) 

    context = {'a_slug': slug_object, 
               'login': login , 
               'comments' : comments ,
               'reply' : replies,
               'dic' : dic,
            }           
    return render(request, 'store.html', context)

@login_required(login_url="/login/")
def watchlist(request):
    login = request.user.is_authenticated
    one = a_anime.objects.all()
    two = b_anime.objects.all()
    three = c_anime.objects.all()
    if request.user.is_authenticated:
        # Get or create the user's wishlist
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        anime_store = storage.objects.all()
        if request.method == 'GET':
            search = request.GET.get('search_anime')
            if search is not None:
                anime_store = storage.objects.filter(name__icontains=search).order_by('name')
                items_per_page = 5
                paginator = Paginator(anime_store, items_per_page)
                page_no = request.GET.get("page", 1)
                result = paginator.get_page(page_no)
                total_pages = result.paginator.num_pages
                context = {
                'data': result,
                'login': login,
                'page_list': [n + 1 for n in range(total_pages)],
                'one' : one,
                'two' : two,
                'three' : three,
                }
                return render(request, 'search.html', context)

        # Pass the wishlist data to the template
        context = {
            'wishlist': wishlist.products.all(),
            'login': login,
        }

        return render(request, 'watchlist.html', context)
    else:
        # Handle the case when the user is not authenticated
        return render(request, 'watchlist.html', {})

@login_required(login_url="/login/")
def favourite(request):
    one = a_anime.objects.all()
    two = b_anime.objects.all()
    three = c_anime.objects.all()
    login = request.user.is_authenticated
    if request.user.is_authenticated:
        # Get or create the user's favorites
        favorites, created = Favorites.objects.get_or_create(user=request.user)
        anime_store = storage.objects.all()
        if request.method == 'GET':
            search = request.GET.get('search_anime')
            if search is not None:
                anime_store = storage.objects.filter(name__icontains=search).order_by('name')
                items_per_page = 5
                paginator = Paginator(anime_store, items_per_page)
                page_no = request.GET.get("page", 1)
                result = paginator.get_page(page_no)
                total_pages = result.paginator.num_pages
                context = {
                'data': result,
                'login': login,
                'page_list': [n + 1 for n in range(total_pages)],
                'one' : one,
                'two' : two,
                'three' : three,
                }
                return render(request, 'search.html', context)

        context = {
            'favorites': favorites.products.all(),
            'login': login,
        }

        return render(request, 'favourite.html', context)
    else:
        # Handle the case when the user is not authenticated
        return render(request, 'favourite.html', {})

def delete_from_watchlist(request, product_id):
    if request.method == 'POST':
        # Assuming the product_id is sent in the request
        product = get_object_or_404(storage, id=product_id)
        
        # Get the user's wishlist
        wishlist = Wishlist.objects.get(user=request.user)
        
        # Remove the product from the wishlist
        wishlist.products.remove(product)
        
        return JsonResponse({'success': True, 'message': 'Removed from Watchlist'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    
def delete_from_favourite(request, product_id):
    if request.method == 'POST':
    
        # Assuming the anime_id is sent in the request
        product = get_object_or_404(storage, id=product_id)
        
        # Get the user's favorites
        favorites = Favorites.objects.get(user=request.user)
        
        # Remove the anime from the user's favorites
        favorites.products.remove(product)
        
        return JsonResponse({'success': True, 'message': 'Removed from Favorites'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        btn = Contact(name = name , email = email , message = message)
        btn.save()
    return render(request , 'contact.html')


