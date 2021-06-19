import flask
from flask import request, jsonify
import elastictodf as edf
import definition

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''hi'''


# # A route to return all of the available entries in our catalog.
@app.route('/api/sonicwall/srcip/top_ten', methods=['GET'])
def api_all():
    days = request.args.get('days')
    resp = jsonify(edf.top_ten_src_ip(days, definition.src_ip, 1))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# metric
@app.route('/api/sonicwall/log_insertion_count', methods=['GET'])
def api_logcount():
    days = request.args.get('days')
    resp = jsonify(edf.log_insertion_count(days, definition.log_count_query, 1))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# metric
@app.route('/api/sonicwall/nwtraffic', methods=['GET'])
def api_nwtarffic():
    days = request.args.get('days')
    resp = jsonify(edf.traffic_overview_count(days, definition.nw_traffic_query, 1))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# pie
@app.route('/api/sonicwall/destip/top_ten', methods=['GET'])
def api_destip_topten():
    days = request.args.get('days')
    resp = jsonify(edf.top_ten_destination_ip(days, definition.dest_ip, 1))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# metric
@app.route('/api/sonicwall/threat_by_severity_count', methods=['GET'])
def api_threat_by_severity_count():
    days = request.args.get('days')
    resp = jsonify(edf.threat_by_severity_count(days, definition.threat_count, 3))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# table
@app.route('/api/sonicwall/ips_severity_table_count', methods=['GET'])
def api_ips_severity_table_count():
    days = request.args.get('days')
    resp = jsonify(edf.ips_severity_table_count(days, definition.ips_severity_table, 3))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# bar
@app.route('/api/sonicwall/threats_by_severity_bar', methods=['GET'])
def api_threats_by_severity_bar():
    days = request.args.get('days')
    resp = jsonify(edf.threats_by_severity_bar(days, definition.threat_severity_bar, 3))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# bar
@app.route('/api/sonicwall/top_ten_category_by_severity_types', methods=['GET'])
def api_top_ten_category_by_severity_types():
    days = request.args.get('days')
    resp = jsonify(edf.new_top_ten_category_by_severity_types(days, definition.top_category_severity, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# metric
@app.route('/api/sonicwall/unique_users_with_config_access', methods=['GET'])
def api_unique_users_with_config_access():
    days = request.args.get('days')
    resp = jsonify(edf.unique_users_with_config_access(days, definition.unique_user_count, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# bar
@app.route('/api/sonicwall/top_user_with_config_access', methods=['GET'])
def api_top_user_with_config_access():
    days = request.args.get('days')
    resp = jsonify(edf.top_user_with_config_access(days, definition.top_user_config_access, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# bar
@app.route('/api/sonicwall/administrative_activity', methods=['GET'])
def api_administrative_activity_bar():
    days = request.args.get('days')
    resp = jsonify(edf.administrative_activity(days, definition.admin_activity, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# table
@app.route('/api/sonicwall/error_alert_count_table', methods=['GET'])
def api_error_alert_count_table():
    days = request.args.get('days')
    resp = jsonify(edf.error_alert_count_table(days, definition.error_alert_count_table, 3))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# table
@app.route('/api/sonicwall/request_category_scatter_count_table', methods=['GET'])
def api_request_category_scatter_count_table():
    days = request.args.get('days')
    resp = jsonify(edf.request_category_scatter_count_table(days, definition.request_category_scatter_count_table, 4))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# bar
@app.route('/api/sonicwall/system_access_by_category', methods=['GET'])
def api_system_access_by_category():
    days = request.args.get('days')
    resp = jsonify(edf.system_access_by_category(days, definition.system_access_by_category, 1))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# bar
@app.route('/api/sonicwall/priority_events_bar', methods=['GET'])
def api_priority_events_bar():
    days = request.args.get('days')
    resp = jsonify(edf.priority_events_bar(days, definition.priority_events_bar, 3))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# metric
@app.route('/api/sonicwall/blocked_trojan_count', methods=['GET'])
def api_blocked_trojan_count():
    days = request.args.get('days')
    resp = jsonify(edf.blocked_trojan_count(days, definition.blocked_trojan_count, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# table
@app.route('/api/sonicwall/blocked_trojan_details_table', methods=['GET'])
def api_blocked_trojan_details_table():
    days = request.args.get('days')
    resp = jsonify(edf.blocked_trojan_details_table(days, definition.blocked_trojan_details_table, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# metric
@app.route('/api/sonicwall/web_attack_count', methods=['GET'])
def api_web_attack_count():
    days = request.args.get('days')
    resp = jsonify(edf.web_attack_count(days, definition.web_attack_count, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


# web_attack_details_table
@app.route('/api/sonicwall/web_attack_details_table', methods=['GET'])
def api_web_attack_details_table():
    days = request.args.get('days')
    resp = jsonify(edf.web_attack_details_table(days, definition.web_attack_details_table, 2))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.run()
