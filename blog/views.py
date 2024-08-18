from django.shortcuts import render ,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.db.models import Sum
from .models import Post,Comment,Slider,Feedback,Meeting    
from .forms import CommentForm,CommentForm1
from geopy.distance import great_circle
import speech_recognition as sr 
import requests



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def index(request):
    context = {
        'posts': Post.objects.all(),
        'sliders':Slider.objects.all(),
        'meetings': Meeting.objects.all()  
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','address','date' ,'expire_time','availble_quantity_of_food','type_of_food','detail','image_of_food']

    def form_valid(self, form):
        if form.instance.detail:
            AUDIO_FILE = (form.instance.detail)
            r = sr.Recognizer() 
            with sr.AudioFile(AUDIO_FILE) as source: 
                audio = r.record(source)
            r = sr.Recognizer() 
            form.instance.details_audio =r.recognize_google(audio)
        form.instance.author = self.request.user 
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','address','date' ,'expire_time','availble_quantity_of_food','type_of_food','detail','image_of_food']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView1(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content','status']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return True


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def meetingDetail(request, slug):
    post = get_object_or_404(Post, MSlug = slug)
    users=User.objects.all()
    a=[]
    for user in users:
        dist = great_circle((user.profile.latitude,user.profile.longitude),(post.latitude,post.longitude)).miles
        if (dist<2):
            a.append(user)
            print("Distance between Donors to Hungers",dist*1000)
            # if user.profile.type_of_user is 'Volunteer' :
            #     url = "https://www.fast2sms.com/dev/bulk"
            #     payload = "sender_id=FSTSMS&message=AKSHAYA PATRA: Some Good Quality foods are available near &language=english&route=p&numbers=6392507439"
            #     headers = {
            #     'authorization': "qHiIlKbn2RuVxYjg67SA9WFTdzOJLME41wBvpP5QmUDecNskoro9N41ulrZL2GUEwD3nzpOiJFvbed58",
            #     'Content-Type': "application/x-www-form-urlencoded",
            #     'Cache-Control': "no-cache",
            #     }
            #     response = requests.request("POST", url, data=payload, headers=headers)
            # print("Message sent")
        else:
            print(dist)
    comments = post.comments.filter(Active=True, Parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        comment_form1 = CommentForm1(data=request.POST)
        if comment_form.is_valid and comment_form1.is_valid:
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
            if Parent_id:
                Parent_obj = Comment.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment1 = comment_form1.save(commit=False)
                    reply_comment.Parent = Parent_obj
                    reply_comment1.Parent = Parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment1 = comment_form1.save(commit=False)
            new_comment.Meeting_Comment = post
            new_comment.save()
            return redirect('meeting_detail', slug)
    else:
        comment_form = CommentForm()
        comment_form1 = CommentForm1()

    return render(request, 'blog/meeting_detail.html', {'title': 'Meeting Details','a':a,'users':users,'meetings':post, 'comments':comments,'comment_form':comment_form,'comment_form1':comment_form1})


# def meetingDetail(request, slug):
#     post = get_object_or_404(Post, MSlug = slug)
#     users=User.objects.all()
#     a=[]
#     b=[]
#     for user in users:
#         dist = great_circle((user.profile.latitude,user.profile.longitude),(post.lat,post.longi)).miles
#         if (dist<2):
#             a.append(user.profile.latitude)
#             b.append(user.profile.longitude)
#             print(user.profile.latitude)
#         else:
#             print(dist)
         
#     comments = post.comments.filter(Active=True, Parent__isnull=True)
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         comment_form1 = CommentForm1(data=request.POST)
#         if comment_form.is_valid:
#             Parent_obj = None
#             try:
#                 Parent_id = int(request.POST.get('Parent_id'))
#             except:
#                 Parent_id = None
#             if Parent_id:
#                 Parent_obj = Comment.objects.get(id=Parent_id)
#                 if Parent_obj:
#                     reply_comment = comment_form.save(commit=False)
#                     reply_comment1 = comment_form1.save(commit=False)
#                     reply_comment.Parent = Parent_obj
#                     reply_comment1.Parent = Parent_obj
#             new_comment = comment_form.save(commit=False)
#             new_comment = comment_form1.save(commit=False)
#             new_comment.Meeting_Comment = post
#             new_comment.save()
#             return redirect('meeting_detail', slug)
#     else:
#         comment_form = CommentForm()
#         comment_form1 = CommentForm1()

#     return render(request, 'blog/meeting_detail.html', {'title': 'Meeting Details','a':a,'b':b,'users':users,'meetings':post, 'comments':comments,'comment_form':comment_form,'comment_form1':comment_form1})

def discussions(request, slug):
    post = get_object_or_404(Post, MSlug = slug)
    comments = post.comments.filter(Active=True, Parent__isnull=True)
    post.comments.comment_act=True
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
            if Parent_id:
                Parent_obj = Comment.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.Parent = Parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.Meeting_Comment = post
            new_comment.save()
            return redirect('discussions', slug)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/discussions.html', {'title': 'Discussions','meetings':post, 'comments':comments,'comment_form':comment_form})

def feedback(request):
    context = {
        'feedback': Feedback.objects.all()  
    }
    return render(request, 'club/feedback.html', { 'title': 'Feedback' })



class PostCreateView1(CreateView):
    model = Feedback
    template_name = 'blog/feedback.html'
    success_url = '/'
    fields = ['Name','Content']
    

def meeting(request):
    context = {
        'meeting': Meeting.objects.all()  
    }
    return render(request, 'blog/meeting.html',context)


def analysis(request):
    return render(request, 'blog/analysis.html')