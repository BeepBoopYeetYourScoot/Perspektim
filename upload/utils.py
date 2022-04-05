import hashlib

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from . import errors


def generate_hash_for_file(uploaded_file: InMemoryUploadedFile) -> str:
    """
    Генерирует хэш для загружаемого файла
    """
    h = hashlib.sha256()
    for chunk in uploaded_file.chunks(chunk_size=1024):
        h.update(chunk)
    return h.hexdigest()


def validate_size(value) -> None:
    """
    Валидатор размера файла
    """
    # 1 GB
    limit = 1 * 1024 ** 3
    if value.size > limit:
        raise ValidationError(errors.FILE_TOO_LARGE)
