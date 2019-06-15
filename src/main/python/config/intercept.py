from flask import Flask
from flask import request
from flask import redirect
from flask import session

app = Flask(__name__)  # type:Flask
app.secret_key = "DragonFire"


@app.before_request
def is_login():
    if request.path == "/login":
        return None

    if not session.get("user"):
        return redirect("/login")


@app.route("/login")
def login():
    return "Login"


@app.route("/index")
def index():
    return "Index"


@app.route("/home")
def home():
    return "Login"


app.run("0.0.0.0", 5000)


@program.after_request
def call_after_request_callbacks(response):
    for callback in getattr(g, 'after_request_callbacks', ()):
        callback(response)
    return response


@program.before_request
def before():
    start = datetime.utcnow()

    @after_this_request
    def after(response):
        if response.status_code == 200:
            if request.headers.get('Authorization'):
                end = datetime.utcnow()
                dur = end - start
                request_log = get_request_log()
                response_log = get_response_log(response)
                extra_info = {
                    'request': request_log,
                    'response': response_log,
                    'start': start,
                    'end': end,
                    'duration': str(dur)
                }
                logger = init_logger_with_token(extra_info)
                logger.info(request_log['route'])
                level = 'INFO'
                # log to operation user_operation_log
                if request_log['method'].lower() != 'get' and request_log['route'] != '/resource_manager/obtain_real_time_data':
                    route_array = request_log['route'].split('/')[1:]
                    if len(route_array) >= 2:
                        match_str = '/' + route_array[0] + '/' + route_array[1]
                    else:
                        match_str = '/' + route_array[0]
                    operation_type = None
                    if constants.api_translate.get(match_str):
                        operation_type = constants.api_translate[match_str]['operation_type']
                        match_str = constants.api_translate[match_str]['operation']
                    if operation_type == "门禁管理":
                        from services.access_control import access_control_log_supplement
                        extra_info = access_control_log_supplement(match_str, request_log, extra_info)
                    log_service.save_log(match_str, operation_type, extra_info, level)

        return response


# log uncaught exceptions
def dump_environment(e, **extra):
    log_error(e)
    # return make_response(e, 400)


got_request_exception.connect(dump_environment)


# Default handler for uncaught exceptions in the app
@program.errorhandler(500)
def internal_error(e):
    log_error(e)
    return make_response(e, 500)


# Default handler for all bad requests sent to the app
@program.errorhandler(400)
def handle_bad_request(e):
    log_error(e)
    return make_response(e, 400)


# Default handler for all bad requests sent to the app
@program.errorhandler(403)
def handle_forbidden(e):
    log_error(e)
    return make_response(e, 403)


# Default handler for all bad requests sent to the app
@program.errorhandler(410)
def handle_gone(e):
    log_error(e)
    return make_response(e, 400)


# Default handler for all bad requests sent to the app
@program.errorhandler(404)
def handle_not_found(e):
    log_error(e)
    return make_response(e, 404)


def log_error(e):
    if request.headers.get('Authorization'):
        request_log = get_request_log()
        extra_info = {
            'request': request_log,
            'error': str(e)
        }
        logger = init_logger_with_token(extra_info)
        logger.error(e)
        level = 'ERROR'

        # log to operation user_operation_log
        if request_log['method'].lower() != 'get':
            route_array = request_log['route'].split('/')[1:]
            match_str = '/' + '/'.join(route_array)
            operation_type = None
            if constants.api_translate.get(match_str, {}).get('operation'):
                operation_type = constants.api_translate[match_str]['operation_type']
                match_str = constants.api_translate[match_str]['operation']
            log_service.save_log(match_str, operation_type, extra_info, level)


def get_request_log():
    # parse args and forms
    route = '/' + request.base_url.replace(request.host_url, '')
    request_log = {
        'route': route,
        'method': request.method,
        'ip': request.remote_addr
    }
    if len(request.get_data()) != 0:
        try:
            body = request.get_json()
        except:
            body = json_util.loads(request.get_data())
        for i in ["password", "old_password", "new_password", "identityCard"]:
            if i in body:
                body[i] = '******'
        request_log['body'] = json_util.dumps(body)
        # 当接口为同步数据库时，过滤body中的字段
        if route == '/b_fsu/synchronous_configuration':
            new_data = {}
            new_list = []
            for i in body['data']:
                new_data['SOID'] = i.get('SOID')
                new_data['NODENAME'] = i.get('NODENAME')
                new_data['FSUID'] = i.get('FSUID')
                new_data['FSUNODEID'] = i.get('FSUNODEID')
                new_list.append(deepcopy(new_data))
            body['data'] = new_list
            request_log['body'] = json_util.dumps(body)

    values = ''
    if len(request.values) > 0:
        for key in request.values:
            values += key + ': ' + request.values[key] + ', '
        request_log['values'] = values
    return request_log


def get_response_log(response):
    return {
        'status': response.status
    }

