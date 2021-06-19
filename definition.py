import os
'''Below files are using for fetching data from ES index.'''
query_dir = 'sonicwall_dashboard_query'
query_path = os.path.join(os.getcwd(), query_dir)

log_count_query = os.path.join(query_path,'log_insertion_count.json')
nw_traffic_query = os.path.join(query_path, 'traffic_overview_metric.json')
src_ip = os.path.join(query_path,'top_ten_source_ip.json')
dest_ip = os.path.join(query_path,'top_ten_destination_ip.json')
threat_count = os.path.join(query_path,'threat_by_severity_count.json')
ips_severity_table = os.path.join(query_path,'threats_by_severity_types_details.json')
threat_severity_bar = os.path.join(query_path,'threats_by_severity_types_details.json')
top_category_severity = os.path.join(query_path,'top_ten_category_by_severity_types.json')
unique_user_count = os.path.join(query_path,'unique_users_with_config_access.json')
top_user_config_access = os.path.join(query_path,'top_ten_user_with_config_access.json')
admin_activity = os.path.join(query_path,'administrative_access.json')
error_alert_count_table = os.path.join(query_path,'error_and_alert_count.json')
request_category_scatter_count_table = os.path.join(query_path,'request_category.json')
system_access_by_category = os.path.join(query_path,'system_access_by_category.json')
priority_events_bar = os.path.join(query_path,'priority_events.json')
blocked_trojan_count = os.path.join(query_path,'blocked_trojan_count.json')
blocked_trojan_details_table = os.path.join(query_path, 'trojan_details')
web_attack_count = os.path.join(query_path,'web_attack_count.json')
web_attack_details_table = os.path.join(query_path,'web_attack_details.json')

'''Below path will be used to store the screenshot taked related to the dashboard.'''
img_dir = 'screenshot'
img_path = os.path.join(os.getcwd(), img_dir)

'''Below path will be used to store the PDF generated report'''
report_dir = 'report'
report_path = os.path.join(os.getcwd(), report_dir)

'''Any resource which will be used , has to be stored in this path.'''
resource_dir = os.path.join(os.getcwd(),'resource_dir')
resource_comp_logo_path = os.path.join(resource_dir, 'ie_comp_logo.png')
