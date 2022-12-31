# -*- coding:utf-8 -*-
"""
@Time: 2022/12/25
@Description:
"""
from config.conf import world_env
from util.log_util import create_logger

# logger = create_logger(log_dir=LOG_DIR)
logger = create_logger(world_env.log_dir)
