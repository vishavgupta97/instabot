from constants import  BASE_URL,APP_ACCESS_TOKEN
import requests
def get_own_post() :
    requests_url=(BASE_URL)+"users/self/media/recent/?access_token=%s"%(APP_ACCESS_TOKEN)
    print "Get URL is:%s"%(requests_url)
    own_media=requets.get(requests_url).json()

