import json
import requests
from requests.auth import HTTPBasicAuth
import logging
import os


def es_connection(days, file, idx):
    requests.packages.urllib3.disable_warnings()
    headers = {"content-type": "application/json", "Accept-Charset": "UTF-8", "Access-Control-Allow-Origin": "*"}
    # os.chdir("E:\\insiredge\\json_query_files")#/home/ubuntu/tmp/json_query_files
    url = "https://3.84.166.62:9200/new*/_search"
    f = open(file, )
    data = json.load(f)
    data['queries']['query']['bool']['filter'][idx]['range']['@timestamp']['gte'] = "now-" + str(days) + 'd'
    data['queries']['query']['bool']['filter'][idx]['range']['@timestamp']['lte'] = "now"
    with open(file, 'w') as f:
        json.dump(data, f)
        # for item in data['queries']:
        #     print(item)
        query_data = json.dumps(data['queries'])
        # print('query data is {}'.format(query_data))
        try:
            response = requests.get(url, auth=HTTPBasicAuth('elastic', 'iesearch'), verify=False,
                                    data=query_data,
                                    headers=headers)
            results = json.loads(response.text)
            print(results)
            if response.status_code == 200:
                logging.info(
                    "Connection established to ES server and executed query successfully with response code as {}.".format(
                        response.status_code))
        except:
            print('there is some error')
        return results


class esConnection:
    pass
