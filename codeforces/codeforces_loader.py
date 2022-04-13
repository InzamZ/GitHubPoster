import json,time,requests,os,sys,datetime
from matplotlib.font_manager import json_dump 

def main():
    acset = set()
    data = {}
    url = "https://codeforces.com/api/user.status?handle=Misaka_No.19614&from=1&count=10000"
    resp = json.loads(requests.get(url).text)
    result = resp["result"]
    for i in result:
        if i["verdict"] == "OK":
            submittime = datetime.datetime.fromtimestamp(i["creationTimeSeconds"])
            tmp = str(submittime.date())
            id = str(i["problem"]["contestId"]) + i["problem"]["index"]
            if id not in acset:
                acset.add(id) 
                if tmp not in data.keys():
                    data[tmp] = 1
                else:
                    data[tmp] += 1
    url = "https://codeforces.com/api/user.status?handle=Inzam_Z&from=1&count=10000"
    resp = json.loads(requests.get(url).text)
    result = resp["result"]
    for i in result:
        if i["verdict"] == "OK":
            submittime = datetime.datetime.fromtimestamp(i["creationTimeSeconds"])
            tmp = str(submittime.date())
            id = str(i["problem"]["contestId"]) + i["problem"]["index"]
            if id not in acset:
                acset.add(id) 
                if tmp not in data.keys():
                    data[tmp] = 1
                else:
                    data[tmp] += 1
    # print(data)
    with open("data/data.json", "w") as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    main()