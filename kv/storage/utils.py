from django.http import HttpResponse
import yaml
import re


def yaml_response(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if isinstance(result, (str, unicode)):
            data = result
        else:
            data = re.sub('\n\.\.\.$', '', yaml.safe_dump(result, default_flow_style=False)),
        return HttpResponse(
            data,
            content_type='text/plain'
        )
    return wrapper
