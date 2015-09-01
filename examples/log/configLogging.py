# -*- encoding: utf-8 -*-
__author__ = 'tao'

"""通过YAML文件来配置log
"""

"""
注意：要使用logging module，必须升级python到2.7版本以上
CentOS 6.5 自带Python 2.6.6，不能卸载，也不能升级
要自己另外安装Python 2.7
详见 [How To Set Up Python 2.7.6 and 3.3.3 on CentOS 6.4]
(https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4)
"""

import os
import logging.config
import yaml

# current working example = `/Users/tao/IdeaProjects/Python/examples`
confDir = os.getcwd() + "/conf/"


def setup_logging(default_path = confDir + "logging.yaml",
                  default_level = logging.INFO,
                  env_key='LOG_CONF_FILE'):
    """
    如果要在命令行中传递参数`LOG_CONF_FILE`，按照如下方式：
    LOG_CONF_FILE=<实际参数>  python -m log.rotatingFileLogs
    """
    conf_path = os.getenv(env_key, None) or default_path

    if os.path.exists(conf_path):
        with open(conf_path) as f:
            config = yaml.load(f.read())    # 读出的config是JSON形式的字符串
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


