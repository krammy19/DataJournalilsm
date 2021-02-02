'''I wrote this script to grab all public notices published in an obscure newspaper
designed to skirt public noticing laws. This helped for research for this news article: 
https://www.mv-voice.com/news/2019/10/04/for-public-notices-mountain-view-turns-to-obscure-newspaper
'''


import requests

r = requests.get('''https://www.legaladstore.com/frmMain.cfm#section=home.cfm%3Fpage%3DAdSearchMain%26StateId%3D6''')

print(len(r.json()['QUERY']['DATA']))

ad_id = []
for x in r.json()['QUERY']['DATA']:
    print(x[4])
    ad_id.append(x[4])

print(ad_id)
i = 0
f = open("{path}", "a+")
for num in ad_id:
    ad_download = requests.get(
     "https://www.legaladstore.com/ViewAd.cfm",
     params={
             'Productid': num,
             'Producer': 1,
             '_cf_containerId': 'WinVAD-body',
             '_cf_nodebug': True,
             '_cf_nocache': True,
             '_cf_clientid': 'CA3BC1C0EA1CB1D201C748495494BB0',
     })
    f.write(ad_download.text)
    i += 1
    print(i)
