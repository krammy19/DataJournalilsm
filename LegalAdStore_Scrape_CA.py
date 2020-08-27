#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      m_noa_000
#
# Created:     15/10/2019
# Copyright:   (c) m_noa_000 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import requests

r = requests.get('''https://www.legaladstore.com/frmMain.cfm#section=home.cfm%3Fpage%3DAdSearchMain%26StateId%3D6''')

print(len(r.json()['QUERY']['DATA']))

ad_id = []
for x in r.json()['QUERY']['DATA']:
    print(x[4])
    ad_id.append(x[4])

print(ad_id)
i = 0
f = open("C:\\Program Files\\PyScripter\\Python practice\\pagerank\\ad_list.txt", "a+")
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