from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http.response import JsonResponse
from django.conf import settings
from datetime import datetime
import qrcode 
import os

class IndexView(View):
    template_name = 'index.html'

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,context={'media':settings.MEDIA_URL})

    def post(self,request,*args, **kwargs):
        action = request.POST.get('action','')
        if action:
            data = request.POST.get('json_data')
            img = qrcode.make(data=data)
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)
            current_time = datetime.now()
            file_name = f"{current_time}.jpg"
            file_path = f"{settings.MEDIA_ROOT}/{current_time}.jpg"
            img.save(file_path)
            return JsonResponse({'file_name':file_name})
        else:
            return JsonResponse({'file_name':'No Data uploaded'})
        
        