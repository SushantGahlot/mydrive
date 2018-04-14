from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import File
from .forms import FileForm
import time, os
from .tasks import delete_files
from django.template import Template, Context
from django.template.loader import get_template
import json


# Create your views here.


class FileUploadView(View):
    def get(self, request):
        file_list = File.objects.all()
        form = FileForm()
        return render(self.request, 'upload_file.html', {'file_list': file_list, 'form': form})

    def post(self, request):
        time.sleep(1)  # We don't need this line. This is just to delay the process to see the progress bar testing locally.
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            file = form.save()
            category = file.category
            if category == 'Financial Document':
                category = 'financial'
            elif category == 'Marketing Document':
                category = 'marketing'
            elif category == 'Technical Document':
                category = 'technical'
            template = get_template('partials/category_table.html')
            html = template.render({'file_list': [file]})
            data = {'status': 'success', 'row': html, 'category': category}
        else:
            data = {'status': 'fail'}
        return JsonResponse(data)


class DeleteFilesView(View):
    def post(self, request):
        try:
            data = request.POST
            ids = data['ids']
            ids = str(ids)
        except KeyError:
            return HttpResponse(303)
        try:
            ids = [int(x) for x in ids.split(',')]
            files = [x.file.path for x in File.objects.filter(id__in=ids)]
            delete_files.delay(files)  # Call celery task to delete files in the background
            File.objects.filter(id__in=ids).delete()
        except ValueError:
            return HttpResponse(303)
        return HttpResponse(200)


def search_files(request):
    if request.method == "GET":
        searched_term = request.GET.get('query')
        results = [{'value': k, 'data': v} for k, v in
                   list(File.objects.filter(filename__icontains=searched_term).values_list('filename', 'id'))]
        results = {"suggestions": results}
        return HttpResponse(json.dumps(results), content_type="application/json")


class SingleFileView(View):
    def get(self, request, *args, **kwargs):
        file_id = kwargs['file']
        try:
            file_ob = File.objects.get(id=file_id)
            return render(self.request, 'single_file.html', {'file': file_ob})
        except ObjectDoesNotExist:
            return HttpResponse(404)

    def post(self, request, *args, **kwargs):
        file_id = kwargs['file']
        try:
            data = request.POST
            category = data['category']
            category = str(category)
        except KeyError:
            return HttpResponse(303)
        try:
            file_ob = File.objects.get(id=file_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'fail'})
        file_ob.category = category
        file_ob.save()
        return JsonResponse({'status': 'success'})
