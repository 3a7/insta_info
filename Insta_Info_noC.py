try:
    import requests,re,time,os,pyfiglet
except ModuleNotFoundError as m:
    os.system('pip install '+m.name)
from os import system
cyan = '\033[1;36m'
green="\033[4;32m"
red="\033[4;31m"
BPurple="\033[1;35m"
# cookie: ig_cb=2; ig_did=3255D07E-AE1F-435D-AE4D-6DD9143A31DD; mid=YCw4nQALAAGi2-XgPn3SB4vbITaz; shbid=7532; shbts=1614372903.1103077; csrftoken=vSzvnZY2dy6lE7WAv4K9RFHINu6FN9dO; ds_user_id=379234200
def check_username(username):
    datas = 0
    h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36','cookie':'ig_cb=2; ig_did=3255D07E-AE1F-435D-AE4D-6DD9143A31DD; mid=YCw4nQALAAGi2-XgPn3SB4vbITaz; shbid=7532; shbts=1614372903.1103077; csrftoken=4pknjFO5a97KUJ04BoSasuUSHCjp9eBw; rur=PRN; ds_user_id=276972397; sessionid=276972397%3AwxnDCAsRi05tns%3A3'}
    while True:
        try:
            i = requests.get(f'https://www.instagram.com/{username}/',headers=h,timeout=5)
            break
        except:
            try:
                i = requests.get(f'https://www.instagram.com/{username}/',headers=h,timeout=5)
                break
            except:
                print('[!] Error while logging in! Try different cookies.')
    
    word = re.findall('HttpErrorPage.css',i.text)
    if len(word) == 1:
        try:
            datas = re.findall('content=".*?Posts',i.text)[0]
            try:
                fullname = re.findall('("og:title" content=")(.*?)(\(@)',i.text)[0][1]
            except:
                fullname = None
            try:
                bio = re.findall('("description":")(.*?)(\",")',i.text)[0][1]
            except:
                bio = None
            try:
                mails = re.findall("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",i.text)
            except:
                mails = None
            try:
                is_private = re.findall('("is_private":)(\S{1,5})(,"is_verified":)',i.text)[0][1]
            except:
                is_private = None
        except Exception as e:
            return str(e)
    else:
        if i.status_code == 404:
            return '[!] The username does NOT EXIST!\n'
        print('Something went wrong! Try again later.')

    if datas != 0:
        head1 = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '68','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_cb=1; ig_did=131F2FE5-1BB1-4652-9E16-5AFF47A7CC36; mid=XzlsVQALAAFETmXB79LUzyCE348k; shbid=6664; shbts=1597861147.1435034; rur=FTW; csrftoken=Ow0d1NTJuy6sEvaH3c5irri2zk1ExJe2; urlgen="{\"185.113.96.223\": 29518}:1k8SgR:LaXQkBLADjj_JFFC4B8PkeNDmXQ"','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/password/reset/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36','x-csrftoken': 'Ow0d1NTJuy6sEvaH3c5irri2zk1ExJe2','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR2Oj4pwhIg-NMX0JaMK9oyeAa9fEiflWvsxVaSwZhGm8l1F','x-instagram-ajax': 'f6699f3befc8','x-requested-with': 'XMLHttpRequest'}
        dat = {
        'email_or_username': f'{username}',
        'recaptcha_challenge_field':''
        }
        url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
        try:
            res = requests.post(url,headers=head1,data=dat,timeout=5).text
            try:
                maily = re.search('[A-z0-9]{1}\*{1,}[A-z0-9]\@\S{1,}\.[A-z0-9]{1,}',res).group()
            except:
                try:
                    maily = re.search('[A-z0-9]{1}\*{1,}\@\S{1,}\.[A-z0-9]{1,}',res).group()
                except:
                    if 'Please wait a few minutes before you try again' in res:
                        maily = 'Please wait a few minutes before you try again'
                    else:
                        maily = None

            try:
                numb = re.findall('\+\d{1,3}\s{1}\*{3}\-{1}\*{4}\-{1}\*{2}\d{2}',res)[0]
            except:
                numb = None
            
            cv = datas[datas.index('"'):][1:].split(', ')
            #print(cv)
            if len(mails) > 1:
                mails = ' - '.join(mails)
            elif len(mails) == 1:
                mails = mails[0]
            else:
                mails = None
            date = None
            if cv[2].split(' ')[0] != 0 and is_private != 'true':
                try:
                    last_post_url = re.findall('("shortcode":")(\S{1,})(","dimensions":)',i.text)[0][1]
                    post = requests.get('https://www.instagram.com/p/'+last_post_url+'/',headers=h,timeout=5).text
                    date = re.search('( on )(.*?)(\.)(.*?)(","is_video":)',post).group(2)
                except:
                    date = 'Error'
            
            combo = f'''
----- Info -----
{'Email'}: {maily}
{'Number'}: {numb}
{'Username'}: {'@'+username}
{'Full Name'}: {fullname}
{'Is Private'}: {is_private}
{'Bio'}: {bio}
{'Other Mails In The Page'}: {mails}
{'Last Post Date'}: {date}
{'Followers'}: {cv[0].split(' ')[0]}
{'Following'}: {cv[1].split(' ')[0]}
{'Posts'}: {cv[2].split(' ')[0]}
{'Time'}: {time.asctime()}
----------------
'''         
            return combo
            #return i.text
        except Exception as ea:
            return str(ea)
    else:
        return 'Uknown Error'
clear = lambda: system("cls")
clear()




print(pyfiglet.figlet_format(' Insta Info v1'))
print('                       CopyRight >> instagram.com/a7.cc')


print()
print('[*] Welcome to Insta Info v1 !')
print("[*] This program gives you information about a certain Instagram account just by typing the account's username.")
print()

while True:
    def do():
        user = input('Enter Username >> ')
        if user[0] == '@':
            user = user[1:]
        info = check_username(user)
        print(info)
    do()
    print('(1) Check another username.')
    print('(2) Exit')
    ans = input()
    if ans == str('2'):
        break