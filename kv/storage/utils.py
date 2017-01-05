from django.http import HttpResponse
import yaml
import re


def yaml_response(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return HttpResponse(
            re.sub('\n\.\.\.$', '', yaml.safe_dump(result, default_flow_style=False)),
            content_type='text/plain'
        )
    return wrapper
