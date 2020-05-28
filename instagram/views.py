from django.shortcuts import render
from django.http import HttpResponse

posts =[
    {
       'author':'Alex',
       'image':'Blog Post 1' ,
       'caption':'As long as you qre who you are. Be who you are',
       'date_posted': 'August 27, 2018',

    },
    {
    'author':'Alex',
    'image':'Blog Post 1' ,
    'caption':'As long as you qre who you are. Be who you are',
    'date_posted': 'August 27, 2018',

}
]


def main(request):
    context = {
        'posts': posts
    }
    return render(request, 'instagram/main.html', context)
