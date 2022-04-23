#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from unmanic.libs.unplugins.settings import PluginSettings

import apprise

# Configure plugin logger
logger = logging.getLogger("Unmanic.Plugin.apprise_notifier")


class Settings(PluginSettings):
    settings = {
        "Apprise file": "",
    }

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

def notify():
    apobj = apprise.Apprise()
    logger.info("Send notification through AppRise".format())

def on_postprocessor_task_results(data):
    """
    Runner function - provides a means for additional postprocessor functions based on the task success.

    The 'data' object argument includes:
        library_id                      - The library that the current task is associated with
        task_processing_success         - Boolean, did all task processes complete successfully.
        file_move_processes_success     - Boolean, did all postprocessor movement tasks complete successfully.
        destination_files               - List containing all file paths created by postprocessor file movements.
        source_data                     - Dictionary containing data pertaining to the original source file.

    :param data:
    :return:
    
    """
    if data.get('task_processing_success') and data.get('task_processing_success'):
        notify(data.get('source_data'))

    return data
