import datetime
from functools import wraps
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from .commands import Error, Redirect, NotFoundError
from django.views.decorators.http import require_http_methods
from django.conf import settings

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_TIME_FORMAT = "%H-%M-%S"
DEFAULT_DATETIME_FORMAT = "%sT%s" % (DEFAULT_DATE_FORMAT, DEFAULT_TIME_FORMAT)
DATE_FORMAT = settings.DATE_FORMAT if hasattr(settings, 'DATE_FORMAT') else DEFAULT_DATE_FORMAT
TIME_FORMAT = settings.TIME_FORMAT if hasattr(settings, 'TIME_FORMAT') else DEFAULT_TIME_FORMAT
DATETIME_FORMAT = settings.DATETIME_FORMAT if hasattr(settings, 'DATETIME_FORMAT') else DEFAULT_DATETIME_FORMAT


class JsonEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime(DATETIME_FORMAT)
        elif isinstance(o, datetime.date):
            return o.strftime(DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(TIME_FORMAT)
        else:
            return super().default(o)


class JsonAnswer(JsonResponse):
    def __init__(self, data, **kwargs):
        data["version"] = settings.VERSION if hasattr(settings, 'VERSION') else '0.0.0'
        data["mode"] = settings.DEPLOY_MODE if hasattr(settings, 'DEPLOY_MODE') else ""
        super().__init__(data, encoder=JsonEncoder, **kwargs)
        self['Access-Control-Allow-Origin'] = 'http://localhost:3000' # TODO


def api_request(view):
    def _decorator(request, *args, **kwargs):
        try:
            if request.method == 'POST':
                try:
                    kwargs['data'] = json.loads(request.body.decode('utf-8'))
                except KeyError:
                    raise Error(internal_code=0, response_code=400, text='Data key is missing')
                except ValueError:
                    raise Error(internal_code=0, response_code=400, text='Data is not json')
            return JsonAnswer({'data': view(request, *args, **kwargs)})
        except Error as error:
            return JsonAnswer({"error": {
                'code': error.internal_code,
                'text': error.text}},
                status=error.response_code)
        except Redirect as redirect:
            return JsonAnswer({"redirect": redirect.path}, status=301)
        except Exception:
            #return JsonAnswer({"error": {'code': 0, 'text': 'error_unknown_error'}}) # TODO
            raise
    return wraps(view)(_decorator)


def get_api_request(view):
    return require_http_methods(['GET', ])(api_request(view))


def post_api_request(view):
    return require_http_methods(['POST', ])(api_request(view))

def delete_api_request(view):
    return require_http_methods(['DELETE', ])(api_request(view))
