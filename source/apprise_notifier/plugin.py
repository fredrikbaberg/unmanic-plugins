#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from unmanic.libs.unplugins.settings import PluginSettings

import apprise

# Configure plugin logger
logger = logging.getLogger("Unmanic.Plugin.apprise_notifier")


class Settings(PluginSettings):
    settings = {
        'Discord Webhook': '',
        'Notify on Task Failure?': False,
    }

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

def notify():
    """
    Send notification using Apprise.
    """
    apobj = apprise.Apprise()
    data = 'Notification data.'
    logger.info("Sent notification ({}) through Apprise.".format(data))

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
    if data.get('library_id'):
        settings = Settings(library_id=data.get('library_id'))
    else:
        settings = Settings()

    if not data.get('task_processing_success') and not settings.get_setting('Notify on Task Failure?'):
        return data

    notify()

    return data
