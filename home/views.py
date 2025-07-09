from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # peoples = [
    #     {'name':'sudip','age':21},
    #     {'name':'shivam','age':20},
    #     {'name':'rohan','age':22},
    #     {'name':'ranveer','age':15},
    #     {'name':'supratim','age':21},
    #     {'name':'abdul','age':23},
    #     {'name':'debu','age':18},
    # ]
    # vegetables=['pumpkin','Tomato','Potato']
    #text="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum nesciunt sed reprehenderit eligendi, mollitia perferendis animi cupiditate fugit, officia quis veritatis hic accusantium culpa? Suscipit cum eius, illo eos vero officia nulla aut architecto praesentium, obcaecati quos voluptatem laboriosam animi voluptatibus tempore minus voluptatum? Veritatis, rerum quaerat quod magnam aliquid quae odio et sint consequuntur impedit cum quo soluta suscipit, officiis expedita. Repellat magnam commodi error vitae, omnis officia optio earum vero molestias ratione repellendus, doloremque minus amet illo laudantium molestiae exercitationem illum saepe iure a libero! Atque voluptate dolor consectetur voluptatem amet exercitationem quaerat, iure numquam dignissimos aut iusto!"""
       
    return render(request , "receipes.html")#,'text':text,'vegetables':vegetables
# def home(request):
#     return render(request,"html/index.html")
def contact(request):
    return render(request , "html/contact.html")

def about(request):
    return render(request , "D:/All Projects/DJANGO-YOUTUBE/jangoproject/home/templates/html/about.html")

def success_page(request):
     return HttpResponse("Hey this is a success page")