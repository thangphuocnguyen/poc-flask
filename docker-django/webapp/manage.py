#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":

    env = os.environ.get('ENVIRONMENT', '')

    setting_file = ""

    if env == "staging":
        setting_file = "djangoprj.config.settings.staging"
    elif env == "production":
        setting_file = "djangoprj.config.settings.production"
    else:
        setting_file = "djangoprj.config.settings.local"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting_file)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
