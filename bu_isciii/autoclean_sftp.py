#!/usr/bin/env python
#   sftp_autoclean.py
#
#   Gaol: automatically remove service from sftp after X days after the last update/access  
#       Sub goals:
#           1. Get service regex
#           2. Get sftp service metadata from jsons
#           3. Mark services that are stored for long period-time
#           4. Provide a log-completition file. 
#           5. linting -- pep8 & black

# import
import os
import shutil
import sys
import logging
import rich
import questionary
from datetime import datetime, timedelta

# =================================================================
# Backbone and utils
# =================================================================

# temp cp from utils
def prompt_path(msg):
    source = questionary.path(msg).unsafe_ask()
    return source

def prompt_yn_question(msg):
    confirmation = questionary.confirm(msg).unsafe_ask()
    return confirmation

# New functions(mv to utils)
def timestamp_converter(timestamp): # import datetime
    date_formated = datetime.fromtimestamp(timestamp)
    return date_formated

def last_updated_file(datetime_list):
    latest_date = max(datetime_list)
    return latest_date

class LastMofdificationFinder:
    def __init__(self, path):
        self.path = path
        self.last_modified_time = 0
    
    def find_last_modification(self):
        self.get_last_modified(self.path)
        return timestamp_converter(self.last_modified_time)

    def get_last_modified(self, directory):
        last_modified_time = os.path.getmtime(directory)

        for root, dirs, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                file_modified_time = os.path.getmtime(file_path)
                if file_modified_time > last_modified_time:
                        last_modified_time = file_modified_time

        if last_modified_time > self.last_modified_time:
                    self.last_modified_time = last_modified_time

# TODO: Add a handle method
class AutoremoveSftpService:
    def __init__(self, path):
        if path is None:
            # TODO: Replace with stderr() once implemented
            print("Directory where the sftp site is allocated")
            # TODO: Replace with bu_isciii.utils.prompt_path() once implemented
            self.path = prompt_path(msg="Path")
        else:
            self.path = path

    # TODO: modify this. PR to make this method reusable outside the class
    def check_path_exists(self):
        # if the folder path is not found, then bye
        if not os.path.exists(self.path):
            print( # TODO: replace with stderr.print
                "[red] ERROR: It seems like finding the correct path is beneath me. I apologise. The path: %s does not exitst. Exiting.."
                % self.path
            )
            sys.exit()
    
    def list_sftp_services(self): # TODO: dict_sftp_ **
        self.sftp_services = {}
        for service_dir in os.listdir(self.path):
            service_fullPath = os.path.join(self.path, service_dir)
            service_finder   = LastMofdificationFinder(service_fullPath)
            service_last_modification = service_finder.find_last_modification()
            self.sftp_services[service_dir] = service_last_modification
    
    def mark_toDelete(self, window=2): # TODO: 14 days
        self.window = timedelta(days=window)
        self.marked_services = []

        for key, value in self.sftp_services.items():
            if datetime.now() - value > self.window:
                self.marked_services.append(key) 

    def remove_oldservice(self): # prompt thing
        if len(self.marked_services) == 0:
            sys.exit(f"The sftp site has not service folders older than {self.window} days. Skiping autoclean_sftp...")
        else:
            service_elements='\n'.join(self.marked_services)
            print(f"The following services will be deleted:\n{service_elements}") # replace with isciii std err
            confirm_sftp_delete = prompt_yn_question("Are you sure? (Y/n): ")
            if confirm_sftp_delete:
                for service in self.marked_services:
                    try:
                        print(f"Deleting service {service}: {os.path.join(self.path, service)}") # replace with isciii std err
                        #shutil.rmtree(os.path.join(self.path, sftp_folder))
                    
                    except OSError as o:
                        print(f"[ERROR] Cannot delete service folder {service}: {os.path.join(self.path, service)}") # replace with isciii std err & import colors
    
sftp_site_autoclean = AutoremoveSftpService(None)
sftp_site_autoclean.check_path_exists()
sftp_site_autoclean.list_sftp_services()
sftp_site_autoclean.mark_toDelete()
sftp_site_autoclean.remove_oldservice()