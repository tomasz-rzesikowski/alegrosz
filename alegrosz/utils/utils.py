import os
from datetime import datetime
from secrets import token_hex

from werkzeug.utils import secure_filename

path = os.path.abspath(os.path.dirname(__file__))
uploads_path = os.path.join(path, '..', 'uploads')


def save_image_uploads(img):
    date_format = '%Y%m%dT%H%M%S'
    now = datetime.utcnow().strftime(date_format)
    random_string = token_hex(2)  # how many bytes
    file_name = random_string + '_' + now + '_' + img.data.filename
    file_name = secure_filename(file_name)
    img.data.save(os.path.join(uploads_path, file_name))
    return file_name
