from django.shortcuts import get_object_or_404
from utils import yaml_response
from models import Group, Record
# from collections import OrderedDict


@yaml_response
def index(request):
    groups = Group.objects.order_by('-last_modified')
    return dict(groups=[group.key for group in groups])


@yaml_response
def group(request, group_pk):
    group = get_object_or_404(Group, key=group_pk)
    records = Record.objects.filter(group=group).order_by('-last_modified')
    return dict(records=[{record.key: record.value} for record in records])


@yaml_response
def record(request, group_pk, record_pk):
    if request.method == 'POST':
        group = Group.objects.filter(key=group_pk).first()
        if not group:
            group = Group.objects.create(key=group_pk)
        record = Record.objects.filter(key=record_pk, group=group).first()
        if not record:
            record = Record.objects.create(key=record_pk, group=group)
        record.value = request.POST.get('value')
        record.save()
    else:
        record = get_object_or_404(Record, key=record_pk, group_id=group_pk)
    return record.value
