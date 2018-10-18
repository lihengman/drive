from app01 import models
from stark.service.stark import site, StarkConfig, Option
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import render, HttpResponse, reverse
from app01.config.userinfo import UserInfoConfig


site.register(models.UserInfo, UserInfoConfig)