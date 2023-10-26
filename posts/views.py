from django.shortcuts import render
from django.core.exceptions import BadRequest
def add_post(request):
    if request.method == "POST" : 
        pass
    
    return render(request, "add_post.html")
    

def delete_post(request):
    if request.method == "POST":
        pass
    raise BadRequest()
