# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
"""
A Bootstrap-powered simple theme for Shoop.
"""
import shoop.apps
import shoop.xtheme


class Theme(shoop.xtheme.Theme):
    identifier = "shoop_simple_theme"
    name = "Shoop Simple Theme"
    template_dir = "shoop_simple_theme/"


class AppConfig(shoop.apps.AppConfig):
    name = __name__
    verbose_name = Theme.name
    label = "shoop_simple_theme"
    provides = {
        "xtheme": __name__  + ":Theme"
    }


default_app_config = __name__ + ".AppConfig"
