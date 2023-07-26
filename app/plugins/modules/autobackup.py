import glob
import os
import time
from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from threading import Event
from app.plugins.modules._base import _IPluginModule
from app.utils import SystemUtils
from config import Config
from web.action import WebAction


class AutoBackup(_IPluginModule):
    # 插件名称
    module_name = "自动备份"
    # 插件描述
    module_desc = "自动备份NAStool数据和配置文件。"
    # 插件图标
    module_icon = "backup.png"
    # 主题色
    module_color = "bg-green"
    # 插件版本
    module_version = "1.0"
    # 插件作者
    module_author = "thsrite"
    # 作者主页
    author_url = "https://github.com/thsrite"
    # 插件配置项ID前缀
    module_config_prefix = "autobackup_"
    # 加载顺序
    module_order = 22
    # 可使用的用户级别
    auth_level = 1

    # 私有属性
    _scheduler = None

    # 设置开关
    _enabled = False
    # 任务执行间隔
    _cron = None
    _cnt = None
    _full = None
    _bk_path = None
    _onlyonce = False
    _notify = False
    # 退出事件
    _event = Event()

