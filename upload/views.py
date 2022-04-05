from django.shortcuts import render
from upload.forms import UploadFileForm
from upload.utils import generate_hash_for_file
from upload.models import Property
from django.db import IntegrityError
from django.forms.models import model_to_dict
from datetime import datetime
from . import errors


def upload_file(request):
    """
    Сохранение права на файл через форму
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_hash = generate_hash_for_file(request.FILES['file'])
            try:
                timestamp = int(datetime.timestamp(datetime.now()))
                model_instance = Property.objects.create(
                    author=form.cleaned_data['author'],
                    hash_sum=file_hash,
                    timestamp=timestamp
                )
            except IntegrityError:
                new_form = UploadFileForm()
                return render(request, 'upload.html',
                              {'form': new_form, 'previous_result': errors.UPLOAD_EXISTS},
                              status=400)
            else:
                data = model_to_dict(instance=model_instance)
                new_form = UploadFileForm()
                return render(request, 'upload.html', {'form': new_form, 'created_data': data})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
