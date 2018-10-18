from app01 import models
from stark.service.stark import site, StarkConfig,Option
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.urls import reverse


class UserInfoConfig(StarkConfig):
    def display_checkbox(self, row=None, header=False):
        if header:
            return "选择"
        return mark_safe("<input type='checkbox' name='pk' value='%s' />" % row.pk)

    list_display = [
        StarkConfig.display_checkbox, 'username', 'admission', 'type', 'one', 'two', 'three', 'four',
    ]

    def multi_init(self, request):
        pass
    multi_init.text = "批量初始化"
    action_list = [
        multi_init,
    ]


    search_list = ['name', 'qq']

