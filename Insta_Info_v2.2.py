
import requests
from colored import fg,attr

green = lambda x : fg('green')+x+attr('reset')
red = lambda x : fg('red')+x+attr('reset')
blue = lambda x : fg('blue')+x+attr('reset')
yellow = lambda x : fg('yellow')+x+attr('reset')
cyan = lambda x : fg('cyan')+x+attr('reset')
magenta = lambda x : fg('magenta')+x+attr('reset')

# Sends instagram reset
def reset(user):

    headers = {
        'x-ig-app-locale': 'en_US',
        'x-ig-device-locale': 'en_US',
        'x-ig-mapped-locale': 'en_US',
        'x-pigeon-session-id': 'UFS-88bf7364-c6e0-4576-b65a-74d86b161f4c-1',
        'x-pigeon-rawclienttime': '1682115374.546',
        'x-ig-bandwidth-speed-kbps': '5897.000',
        'x-ig-bandwidth-totalbytes-b': '1666809',
        'x-ig-bandwidth-totaltime-ms': '384',
        'x-ig-app-startup-country': 'IQ',
        'x-bloks-version-id': '8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07',
        'x-ig-www-claim': '0',
        'x-bloks-is-layout-rtl': 'false',
        'x-ig-device-id': '8136b78d-1663-48bb-91ce-d647ee6fa21a',
        'x-ig-family-device-id': 'ee85c5e4-9543-4985-989e-8de1dc882ecb',
        'x-ig-android-id': 'android-08a47fd1c43d35c4',
        'x-ig-timezone-offset': '-18000',
        'x-ig-nav-chain': 'SelfFragment:self_profile:2:main_profile::,ProfileMediaTabFragment:self_profile:3:button::,AccountSwitchFragment:account_switch_fragment:4:button::,AddAccountBottomSheetFragment:add_account_bottom_sheet:5:button::,AD1:login_landing:6:button::,AD2:password_lookup:7:button::,9jv:user_password_recovery:8:button::',
        'x-fb-connection-type': 'WIFI',
        'x-ig-connection-type': 'WIFI',
        'x-ig-capabilities': '3brTv10=',
        'x-ig-app-id': '567067343352427',
        'priority': 'u=3',
        'user-agent': 'Instagram 237.0.0.14.102 Android (25/7.1.2; 239dpi; 720x1280; Asus; ASUS_Z01QD; ASUS_Z01QD; intel; en_US; 373310563)',
        'accept-language': 'en-US',
        'x-mid': 'ZDhYBAABAAGVFpl3Cy9e5IBEttUa',
        'ig-intended-user-id': '0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'content-length': '290',
        'accept-encoding': 'gzip, deflate',
        'x-fb-http-engine': 'Liger',
        'x-fb-client-ip': 'True',
        'x-fb-server-cluster': 'True',}

    data = {
        'adid':'9da1c7ad-59a1-4d9c-95d6-4dcef4a136e0',
        'guid':'8136b78d-1663-48bb-91ce-d647ee6fa21a',
        'device_id':'android-08a47fd1c43d35c4',
        'query':user,
        'waterfall_id':'382b2075-4df6-4573-ad9e-6ab0dc0ef38a'}
    

    try:
        sendreq = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,timeout=10)
    except:
        return 'ERROR'
    
    if 'sent' in sendreq.text:
        email = sendreq.json()['email']
        return email
    
    else:
        return 'ERROR'

def get_instagram_info(user):

    if user.startswith('@'):
        user = user[1:]

    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar',
    'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    }
    try:
        r = requests.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}',headers=headers).json()
    except Exception as exe:
        return f'[{red("!")}] Error retrieving the data >> '+str(exe)
   
    if "</a></li>" not in r:
        if r["data"]["user"] == None:
            print(f"[{red("!")}] This user doesn't exist!")
        try:
            bio = r["data"]["user"]["biography"]
        except:
            bio = 'Error'
        try:
            followers = r["data"]["user"]["edge_followed_by"]["count"]
        except:
            followers = 'Error'
        try:
            following = r["data"]["user"]["edge_follow"]["count"]
        except:
            following = 'Error'
        try:
            highlight_reel_count = r["data"]["user"]["highlight_reel_count"]
        except:
            highlight_reel_count = 'Error'
        try:
            is_business_account = r["data"]["user"]["is_business_account"]
        except:
            is_business_account = 'Error'
        try:
            is_professional_account = r["data"]["user"]["is_professional_account"]
        except:
            is_professional_account = 'Error'
        try:
            profile_pic = r["data"]["user"]["profile_pic_url"]
        except:
            profile_pic = 'Error'
        try:
            business_email = r["data"]["user"]["business_email"]
        except:
            business_email = 'Error'
        try:
            business_phone_number = r["data"]["user"]["business_phone_number"]
        except:
            business_phone_number = 'Error'
        linked_email = reset(user)
        try:
            is_private = r["data"]["user"]["is_private"]
        except:
            is_private = 'Error'
        try:
            is_verified = r["data"]["user"]["is_verified"]
        except:
            is_verified = 'Error'
        try:
            url = r["data"]["user"]["bio_links"][0]["url"]
        except:
            url = 'None'
        try:
            location = r["data"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["location"]["name"]
        except:
            location="None"
        try:
            last_post = r["data"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["accessibility_caption"]
        except:
            last_post = 'Error'
        try:
            name = r["data"]["user"]["full_name"]
        except:
            name = 'Error'
        try:
            id = r["data"]["user"]["id"]
        except:
            id = 'Error'
        try:
            posts = r["data"]["user"]["edge_owner_to_timeline_media"]["count"]
        except:
            posts = 'Error'
        try:
            date = int(requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"])-1
        except:
            date = 'None'
        
        data =(f"""
[ Get Info For {green('@'+user)} ] ..
[ + ] {cyan('UserID')} : {id}
[ + ] {cyan('Profile Picture')} : {profile_pic}
[ + ] {cyan('Name')} : {name}
[ + ] {cyan('User')} : {user}
[ + ] {cyan('Followers')} : {followers}
[ + ] {cyan('Following')} : {following}
[ + ] {cyan('Posts')} : {posts}
[ + ] {cyan('Last Post')} : {last_post}
[ + ] {cyan('Bio URL')} : {url}
[ + ] {cyan('Is private')} : {is_private}
[ + ] {cyan('Is verified')} : {is_verified}
[ + ] {cyan('Highlight reel count')} : {highlight_reel_count}
[ + ] {cyan('Is professional account')} : {is_professional_account}
[ + ] {cyan('Is business account')} : {is_business_account}
[ + ] {cyan('Linked Email')} : {linked_email}
[ + ] {cyan('Business email')} : {business_email}
[ + ] {cyan('Business phone number')} : {business_phone_number}
[ + ] {cyan('User Create Time')} : {date}
[ + ] {cyan('Account Region')} : {location}
[ + ] {cyan('Bio')} : {bio}
[ + ] Bot made by {red('@A7_acc')}
        """)
        return data
    else:
        return f'[{red("!")}] Unknown Error when parsing the data!! Contact @A7_acc'

print('''
  _____           _          _____        __             ___  
 |_   _|         | |        |_   _|      / _|           |__ \\ 
   | |  _ __  ___| |_ __ _    | |  _ __ | |_ ___   __   __ ) |
   | | | '_ \\/ __| __/ _` |   | | | '_ \\|  _/ _ \\  \\ \\ / // / 
  _| |_| | | \\__ \\ || (_| |  _| |_| | | | || (_) |  \\ V // /_ 
 |_____|_| |_|___/\\__\\__,_| |_____|_| |_|_| \\___/    \\_/|____|
''')
print(f'                             CopyRight >> {cyan("instagram.com/a7.cc")}')


print()
print(f'Welcome to Insta Info v2 ~ {magenta("10/2024")}')
print(" --- This program gives you public information about a certain Instagram account just by typing the account's username --- ")
print(f" --- Try out the telegram bot version! --> {cyan('@insta_user_info_bot')} --- ")
print()

while True:
    def do():
        user = input(f'[{magenta("?")}] Enter Username >> ')
        info = get_instagram_info(user)
        print(info)
    do()
    print(f'({cyan("1")}) Check another username.')
    print(f'({cyan("2")}) Exit')
    ans = input()
    if ans == str('2'):
        break