import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/raw/mJRKwd3j')

try:
    if hwid in r.text:
        pass
    else:
        print('[AUTH] HWID Not in database')
        print(f'HWID: {hwid}') 
        time.sleep(5)
        os._exit()
except:
    print(f'[AUTH] Failed to connect to database')
    time.sleep(5) 
    os._exit() 

print('[AUTH] Found HWID in database')
input()
