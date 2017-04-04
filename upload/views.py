from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import sys
sys.path.append('C:\Users\Ishan\Documents\SSMS_Menu\dailymenu')
import populate

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        # inroduce a better method to include media file path
        populate.populate('C:\Users\Ishan\Documents\SSMS_Menu\dailymenu'+uploaded_file_url)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')
