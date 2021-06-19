import json
import requests
from requests.auth import HTTPBasicAuth
import logging
import os
import definition
from utils import elasticconnection as ec


# pie chart
def top_ten_src_ip(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    pie = [{
        "labels": "Top 10 Source IP - Sonicwall", "pie": data}]
    #print(pie)
    return pie


# metric chart
def log_insertion_count(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = results['hits']['total']
    data.pop('relation', None)
    data['labels'] = 'Log Insertion Rate Per Day'
    data["unit"] = "Count"
    print([data])
    return [data]


# metric chart
def traffic_overview_count(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = results['aggregations']['1']
    bsize = 1024
    a = {'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6}
    r = float(data['value'])
    for i in range(a['g']):
        r = r / bsize
    data['value'] = round(r, 2)
    data['labels'] = 'Total Network Traffic'
    data["unit"] = "GB"
    # print([data])
    return [data]


# pie chart
def top_ten_destination_ip(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    pie = [{
            "labels": "Top 10 Destination IP - Sonicwall", "pie": data}]
    # print(pie)
    return pie


def threat_by_severity_count(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = results['hits']['total']
    data.pop('relation', None)
    data['labels'] = 'IPS : High or Medium Severity'
    data["unit"] = "Count"
    # print([data])
    return [data]


# table having same query executed in below function
def ips_severity_table_count(days, file, idx):
    results = ec.es_connection(days, file, idx)
    if not (len(results['aggregations']['2']['buckets']) == 0):
        data = [doc for doc in results['aggregations']['2']['buckets'][0]['3']['buckets']]
    data = [doc for doc in results['aggregations']['2']['buckets']]
    key_category = []

    for val in data:
        for key_val in val['3']['buckets']:
            final_dict_format = {}
            final_dict_format['key'] = key_val['key']
            final_dict_format['doc_count'] = key_val['doc_count']
            key_category.append(final_dict_format)
    table = [{
        "labels": "IPS: High or Medium Severity", "table": key_category}]
    print(table)
    return table


# bar having same query executed in above function
def threats_by_severity_bar(days, file, idx):
    results = ec.es_connection(days, file, idx)
    if not (len(results['aggregations']['2']['buckets']) == 0):
        data = [doc for doc in results['aggregations']['2']['buckets'][0]['3']['buckets']]
    data = [doc for doc in results['aggregations']['2']['buckets']]
    key_category = []
    for val in data:
        date_val = val['key_as_string'].split('T')[0]
        for key_val in val['3']['buckets']:
            final_dict_format = {}
            final_dict_format['date'] = date_val
            final_dict_format['key'] = key_val['key']
            final_dict_format['doc_count'] = key_val['doc_count']
            key_category.append(final_dict_format)
    # print(key_category)
    bar = [{
        "labels": "IPS: High or Medium Severity", "bar": key_category}]
    print(bar)
    return bar


# bar chart
def top_ten_category_by_severity_types(days, file, idx):
    results = ec.es_connection(days, file, idx)
    time_string = results['aggregations']['2']['buckets']
    data = [doc for doc in results['aggregations']['2']['buckets'][0]['3']['buckets']]
    key_time = []
    for date_val in time_string:
        key_time.append(date_val['key_as_string'])
    bar_data = []
    rem_list = ['score', 'bg_count', '4']
    for val, dt in zip(data, key_time):
        val['severity'] = (val['4']['buckets'][0]['key'])
        val['date'] = dt
        [val.pop(key) for key in rem_list]
        bar_data.append(val)
        # print(val)
    bar = [{
        "labels": "Top 10 Category By Severity Types - Sonicwall", "bar": bar_data}]
    # print(bar)
    return bar


# metric count
def unique_users_with_config_access(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = results['aggregations']['1']
    # data.pop('relation', None)
    data['labels'] = 'Sonicwall - Unique Users with config access'
    data["unit"] = "Count"
    # print([data])
    return [data]


# bar chart
def top_user_with_config_access(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    print(len(results['aggregations']['2']['buckets']))
    key_users = []
    for val in data:
        date_val = val['key_as_string'].split('T')[0]
        for key_val in val['3']['buckets']:
            final_dict_format = {}
            final_dict_format['date'] = date_val
            final_dict_format['key'] = key_val['key']
            final_dict_format['doc_count'] = key_val['doc_count']
            key_users.append(final_dict_format)
    bar = [{
        "label": "Sonicwall - User with Config Access", "bar": key_users}]
    print(bar)
    return bar


# bar
def administrative_activity(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    bar_data = []
    key_category = []
    for val in data:
        date_val = val['key_as_string'].split('T')[0]
        for key_val in val['3']['buckets']:
            final_dict_format = {}
            final_dict_format['date'] = date_val
            final_dict_format['key'] = key_val['key']
            final_dict_format['doc_count'] = key_val['doc_count']
            key_category.append(final_dict_format)
    # print(key_category)
    bar = [{
        "label": "Sonicwall - User with Config Access", "bar": key_category}]
    print(bar)
    return bar


# bar
def new_top_ten_category_by_severity_types(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    print(len(results['aggregations']['2']['buckets']))
    key_category = []
    for val in data:
        date_val = val['key_as_string'].split('T')[0]
        for key_val in val['3']['buckets']:
            final_dict_format = {}
            final_dict_format['date'] = date_val
            final_dict_format['key'] = key_val['key']
            final_dict_format['doc_count'] = key_val['doc_count']
            final_dict_format['severity'] = 'Low'
            key_category.append(final_dict_format)
    # print(key_category)
    bar = [{
        "label": "Top 10 Category By Severity Types - Sonicwall", "bar": key_category}]
    return bar


# table
def error_alert_count_table(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    key_category = []
    # print(data)
    for val in data:
        final_dict_format = {}
        final_dict_format['key'] = val['key']
        final_dict_format['doc_count'] = val['doc_count']
        key_category.append(final_dict_format)
    table = [{
        "labels": "Sonicwall - Error & Alert Count", "table": key_category}]
    # print(table)
    return table


# table
def request_category_scatter_count_table(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    key_category = []
    print(data)
    for val in data:
        final_dict_format = {}
        final_dict_format['key'] = val['key']
        final_dict_format['doc_count'] = val['doc_count']
        key_category.append(final_dict_format)
    table = [{
        "labels": "Sonicwall - Request category", "table": key_category}]
    print(table)
    return table


# bar
def system_access_by_category(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    bar_data = []
    key_category = []
    for val in data:
        date_val = val['key_as_string'].split('T')[0]
        for key_val in val['3']['buckets']:
            final_dict_format = {}
            final_dict_format['date'] = date_val
            final_dict_format['key'] = key_val['key']
            final_dict_format['doc_count'] = key_val['doc_count']
            key_category.append(final_dict_format)
    # print(key_category)
    bar = [{
        "label": "Sonicwall - System access by category", "bar": key_category}]
    print(bar)
    return bar


# bar
def priority_events_bar(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    bar_data = []
    key_category = []
    for val in data:
        date_val = val['key_as_string'].split('T')[0]
        for key_val in val['3']['buckets']:
            final_dict_format = {}
            final_dict_format['date'] = date_val
            final_dict_format['key'] = key_val['key']
            final_dict_format['doc_count'] = key_val['doc_count']
            key_category.append(final_dict_format)
    # print(key_category)
    bar = [{
        "label": "Sonicwall - Priority events", "bar": key_category}]
    # print(bar)
    return bar


# metric count
def blocked_trojan_count(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = results['hits']['total']
    data.pop('relation', None)
    data['labels'] = 'Sonicwall - Blocked Trojan Count'
    data["unit"] = "Count"
    # print([data])
    return [data]


# table
def blocked_trojan_details_table(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    key_category = []
    for val in data:
        final_dict_format = {}
        final_dict_format['key'] = val['key']
        final_dict_format['doc_count'] = val['doc_count']
        key_category.append(final_dict_format)
    # print(key_category)
    table = [{
        "label": "Sonicwall - Trojan Details", "table": key_category}]
    print(table)
    return table


# metric count
def web_attack_count(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = results['hits']['total']
    data.pop('relation', None)
    data['labels'] = 'Sonicwall - Web Attack Count'
    data["unit"] = "Count"
    # print([data])
    return [data]


# table
def web_attack_details_table(days, file, idx):
    results = ec.es_connection(days, file, idx)
    data = [doc for doc in results['aggregations']['2']['buckets']]
    key_category = []
    for val in data:
        final_dict_format = {}
        final_dict_format['key'] = val['key']
        final_dict_format['doc_count'] = val['doc_count']
        key_category.append(final_dict_format)
    # print(key_category)
    bar = [{
        "label": "Sonicwall - Web Attack Details", "table": key_category}]
    print(bar)
    return bar


# top_ten_src_ip(7, definition.src_ip, 1)
# log_insertion_count(7, definition.log_count_query,1)
# traffic_overview_count(7, definition.nw_traffic_query, 1)
# top_ten_destination_ip(7, definition.dest_ip, 1)
# threats_by_severity_bar(7, definition.threat_severity_bar, 3)
# threat_by_severity_count(7, definition.threat_count,3)
# ips_severity_table_count(7, definition.ips_severity_table, 3)
# new_top_ten_category_by_severity_types(7, definition.top_category_severity, 2)
# unique_users_with_config_access(7, definition.unique_user_count, 2)
# top_user_with_config_access(7, definition.top_user_config_access, 2)
# administrative_activity(7, definition.admin_activity, 2)
# error_alert_count_table(7, definition.error_alert_count_table, 3)
# request_category_scatter_count_table(7, definition.request_category_scatter_count_table, 4)
# system_access_by_category(7, definition.system_access_by_category, 1)
# priority_events_bar(7, definition.priority_events_bar, 3)
# blocked_trojan_count(7)
# blocked_trojan_details_table(7)
# web_attack_count(7)
# web_attack_details_table(7)
