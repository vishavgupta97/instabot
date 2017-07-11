import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
#colorama library is imported to add color capabilities in my Application
from colorama import  *
#Mehod For Getting Own's Information
def self_info() :
    requests_url=(BASE_URL)+"users/self/?access_token=%s"%(APP_ACCESS_TOKEN)
    print "Get Request URL:%s"%(requests_url)
    user_info=requests.get(requests_url).json()#Get mehod Is Used For Getting Own Information
    if user_info['meta']['code']==200 :
        if len(user_info['data']) :
            #Here Are The Information of The User
            print Fore.GREEN+Style.BRIGHT+"USERNAME: %s"%(user_info['data']['username'])
            print "You have %s followers"%(user_info['data']['counts']['followed_by'])
            print "you are following %s people" % (user_info['data']['counts']['follows'])
            print "You Have %s No. of posts" % (user_info['data']['counts']['media'])
            Style.RESET_ALL
        else :
            #If nothing Is Recieved From Server
            print Fore.RED+Style.BRIGHT+"Sorry!!!!This User Doesn't Exists"
            Style.RESET_ALL
    else :
        print Fore.RED+Style.BRIGHT+"!!!Status Code Other Than 200 Recieved!!!"
        Style.RESET_ALL





