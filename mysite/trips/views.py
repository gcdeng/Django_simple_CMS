from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def hello_world(request):
    # 1
    # return HttpResponse("Hello World!")

    # 2
    # output = """
    #     <!DOCTYPE html>
    #     <html>
    #     <head>
    #     </head>
    #     <body>
    #         Hello World! <em style="color: LightSeaGreen;">{current_time}</em>
    #     </body>
    #     </html>
    # """.format(current_time = datetime.now())
    # return HttpResponse(output)

    # 3
    return render(request, 'hello_world.html', {
        'current_time': datetime.now()
    })
