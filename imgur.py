from imgurpython import ImgurClient
import os

client_id = 'f4b441972b26281'
client_secret = os.getenv('IMGUR_SECRET')
access_token = os.getenv('IMGUR_ACCESS_TOKEN')
refresh_token = os.getenv('IMGUR_REFRESH_TOKEN')
imgur_client = ImgurClient(client_id, client_secret, access_token, refresh_token)

def upload_image(path):
    image = imgur_client.upload_from_path(path)
    return image