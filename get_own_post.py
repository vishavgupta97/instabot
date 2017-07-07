from constants import  BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib
def get_own_post() :
    requests_url=(BASE_URL)+"users/self/media/recent/?access_token=%s"%(APP_ACCESS_TOKEN)
    print "Get Request URL:%s"%(requests_url)
    own_media=requets.get(requests_url).json()
    if own_media['meta']['code']==200 :
        if len(own_media['data']) :
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
            #return own_media['data'][0]['id']
        else :
            print "!!!Post Doesn't exists!!!"
    else :
        print "STATUS CODE OTHER THAN 200 IS FOUND!"
    #return None

