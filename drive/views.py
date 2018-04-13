from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import File
from .forms import FileForm
import time
# Create your views here.


class FileUploadView(View):
    def get(self, request):
        file_list = File.objects.all()
        form = FileForm()
        return render(self.request, 'index.html', {'file_list': file_list, 'form': form})

    def post(self, request):
        time.sleep(1)  # We don't need this line. This is just to delay the process to see the progress bar testing locally.
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

class DeleteFilesView(View):

    def post(self, request):
        try:
            data = request.POST
            ids = data['ids']
        except KeyError:
            return HttpResponse(303)
        try:
            ids = [int(x) for x in ids.split(',')]
            File.objects.filter(id__in=ids).delete()
        except ValueError:
            return HttpResponse(303)
        return HttpResponse(200)
