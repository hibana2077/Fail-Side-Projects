#匯入
from web3 import Web3
import json
from timeit import default_timer as timer

#連線
w3=Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/r5LWV9YohEw08-xtCrMjWcWy0q64_KJq'))
if w3.isConnected():print("Connected !")
else :print("Error !")

#constant
FILE='ETH_active_address.json'
START=1000007

#資料寫入
datatojson=json.load(open('python\ETH\ETH_active_address.json','r'))


#每次啟動就更新
nownum=w3.eth.get_block_number()
startt=timer()
#讀取資料
for a in range(START,nownum):
    
    print(f"目前進度:{((a-START)/(nownum-START))*10000:.4f} % 使用時間:{timer()-startt:.2f}s")
    startt=timer()
    for b in range(w3.eth.get_block_transaction_count(START)):
        tempdata=dict(w3.eth.get_transaction_by_block(START,b))
        if tempdata['from'] in datatojson:pass
        else:datatojson.append(tempdata['from'])
        if tempdata['to'] in datatojson:pass
        else:datatojson.append(tempdata['to'])
#寫入
file = open('python\ETH\ETH_active_address.json','w')
json.dump(datatojson,file)
file.close()