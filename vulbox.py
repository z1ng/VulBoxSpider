import requests
import jsonpath
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def get_json():
    company_list = []
    url_list = []
    url = 'https://www.vulbox.com/json/getCompanyInfoByName'
    data={
            'page':'0'
        }
    for i in range(1,53):
        data['page'] = i
        res = requests.post(url=url,data=data)
        text = res.text
        #print text
        json_tmp = json.loads(text)
        company_tmp = jsonpath.jsonpath(json_tmp,'$..bus_name')
        company_list += company_tmp
        print company_tmp
        url_tmp = jsonpath.jsonpath(json_tmp,'$..bus_url')
        url_list += url_tmp

    file = open('vulbox_url.txt','a')
    for i in range(0,1039):
        b = url_list[i]
        print >> file,b

get_json()