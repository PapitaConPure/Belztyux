import shutil
import tempfile
from pixivpy3 import *
import imgur
import os

#Trabajar con directorio relativo
dirname = os.path.dirname(__file__)

#Autorizar API de pixiv
pixiv_api = AppPixivAPI()
token = os.getenv('PIXIV_REFRESH_TOKEN')
pixiv_api.auth(refresh_token=token)

def get_illust(page_id):
    '''Conseguir objeto Illust desde una ID de ilustración'''
    response = pixiv_api.illust_detail(page_id)
    return response.illust

#def upload_image_to_imgur(url, image_filename='pixiv-temp'):
#    '''Subir imagen de pixiv a Imgur y retornar el enlace de Imgur'''
#    try:
#        file_path = os.path.join(dirname, 'pix')
#        pixiv_api.download(url, path=file_path, name=image_filename)
#        image = imgur.upload_image(os.path.join(file_path, image_filename))
#        os.remove(os.path.join(file_path, image_filename))
#        return image
#    except Exception:
#        print('Error al descargar imagen desde pixiv o subirla a Imgur')
#        return None

def upload_image_to_imgur(url):
    '''Subir imagen de pixiv a Imgur y retornar el enlace de Imgur'''
    image = None

    try:
        fd, path = tempfile.mkstemp()
        with pixiv_api.requests_call('GET', url, headers={'Referer': 'https://app-api.pixiv.net/'}, stream=True) as response:
            with os.fdopen(fd, 'wb') as tmp:
                shutil.copyfileobj(response.raw, tmp)
                image = imgur.upload_image(path)
        os.remove(path)
    except Exception as e:
        print(f'Error al descargar imagen desde pixiv o subirla a Imgur: {e}')
        return None

    return image