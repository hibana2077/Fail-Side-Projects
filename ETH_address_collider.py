#匯入函數庫
from time import sleep
from eth_account import Account
from timeit import default_timer as timer
import requests,json,secrets

#函數
def createAddress():
  priv = secrets.token_hex(32)
  private_key = "0x" + priv
  acct = Account.from_key(private_key)
  return private_key, acct.address

#常數
API_TOKEN=''#your ETH explore API_TOKEN
failcounter=0
start=timer()
while True:
    pk,ad=createAddress()

    url='https://api.etherscan.io/api?module=account&action=balance&address='+str(ad)+'&tag=latest&apikey='+str(API_TOKEN)
    if int(json.loads(requests.get(url).text)['result'])/(10**18)>0:
        print(f"private_key:{pk}\n address:{ad} \n time using:{timer()-start} s")
        break
    else:
        failcounter+=1
        print(f"no money! this addres balance:{int(json.loads(requests.get(url).text)['result'])/(10**18)} timeusing:{timer()-start} fail counter:{failcounter}")
        sleep(1.1)
        start=timer()
'''
理論上可行，但是機率很低，猜對的機率是10的負72次方，運氣好就會有，不好的話一輩子也看不到他成功。
'''
