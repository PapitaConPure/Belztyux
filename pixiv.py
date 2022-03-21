from pixivpy3 import *
import imgur
import os

#Autorizar API de pixiv
pixiv_api = AppPixivAPI()
token = os.getenv('PIXIV_REFRESH_TOKEN')
pixiv_api.auth(refresh_token=token)

def get_illust(page_id):
    '''Conseguir objeto Illust desde una ID de ilustración'''
    response = pixiv_api.illust_detail(page_id)
    return response.illust

def upload_image_to_imgur(url, image_filename='pixiv-temp'):
    '''Subir imagen de pixiv a Imgur y retornar el enlace de Imgur'''
    try:
        pixiv_api.download(url, path='pix', name=image_filename)
        image = imgur.upload_image(os.path.join('pix', image_filename))
        os.remove(os.path.join('pix', image_filename))
        return image
    except Exception:
        print('Error al descargar imagen desde pixiv o subirla a Imgur')
        return None