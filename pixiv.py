from pixivpy3 import *
import imgur
import os

#Trabajar con directorio relativo
dirname = os.path.dirname(__file__)
print(os.getcwd())
print(__file__)
print(dirname)

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
    print(token)
    #try:
    file_path = os.path.join(dirname, 'pix')
    print(file_path)
    pixiv_api.download(url, path=file_path, name=image_filename)
    image = imgur.upload_image(os.path.join(file_path, image_filename))
    os.remove(os.path.join(file_path, image_filename))
    return image
    #except Exception:
    #    print('Error al descargar imagen desde pixiv o subirla a Imgur')
    #    return None