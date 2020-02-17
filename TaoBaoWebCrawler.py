import requests
import json

class TaoBao:
    url = "https://rate.tmall.com/list_detail_rate.htm"
    header = {
        "cookie": "t=e582bfa4e4ae0a209a0eaceaf0960659; tracknick=melusines; lid=melusines; lgc=melusines; _tb_token_=e19e607bee713; cookie2=1d4479f6db80a02cc65c0c4cb73748f7; cna=u6+DFB1iKB4CAaVbDYeI6TuT; dnk=melusines; hng=CN%7Czh-CN%7CCNY%7C156; enc=L6Tc5%2BIIT3fNOa37Y4KcAPm967ebHdyjOsdJIKydJHeyWARw81zg5JvmA6wukqWjOYbzT5n6fbVCljAfxp6b7g%3D%3D; uc1=cookie21=W5iHLLyFeYZ1WM9hVnmS&pas=0&lng=zh_CN&tag=8&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=true&cookie14=UoTUO8kCKUnosA%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dBxdz1R1hwS6KAHVg%3D&id2=UNaFXFHXP7pRdQ%3D%3D&nk2=DlVlzl4TcINy; uc4=nk4=0%40DDC%2BMfwlNwiqFpPedqKGJ4GbR%2F4%3D&id4=0%40UgGMIX4tP%2BBIZIQQ4SayWxXoDK02; _l_g_=Ug%3D%3D; unb=3624038711; cookie1=AHxLi75i90WmZPQsxqvgGktWNtHhYx9zKUJm4E4idK0%3D; login=true; cookie17=UNaFXFHXP7pRdQ%3D%3D; _nk_=melusines; sg=s19; csg=b5ad221b; x5sec=7b22726174656d616e616765723b32223a226266663766623734396634393665613332626234343031363933316362306665434d5343712f4946454e447a75767a4a674f717258686f4d4d7a59794e44417a4f4463784d547378227d; l=cBag1ll7QRll5fgaBOfwKurza77tiBdfcsPzaNbMiICPOb5J0hwOWZVNsHYvCnGNL6PyJ37nEPh4BPT39y4FhZXRFJXn9MpO.; isg=BFlZf9kbY4Jm6D8WmumBidLCaEUz5k2Y9XIm3XsJUACXgn4Uwjdbae1UhE70OuXQ",
        "referer": "https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w5003-14579014167.6.44783c2fJGAm6F&id=38848279045&skuId=3513813706827&scene=taobao_shop",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
    }

    params = {
        "itemId": "38848279045",
        "sellerId": "2064892827",
        "currentPage": "1",
        "order":"1",
        "callback": "jsonp1336",
    }

    def __init__(self, id):
        self.params['itemId'] = id

    def getPageData(self,pageIndex):
        self.params["currentPage"] = str(pageIndex)
        req = requests.get(url=self.url, params=self.params, headers=self.header, timeout = 8).content.decode('utf-8');
        req = req[req.find('{'):req.rfind('}')+1]
        return json.loads(req)

searchNumber = 50
taobao = TaoBao("38848279045")
for i in range(50):
    pageJson = taobao.getPageData(i)
    for l in pageJson['rateDetail']['rateList']:
        print(l['rateContent'])

