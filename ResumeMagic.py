# -*- coding: utf-8 -*-

"""
name='',
version='',
packages=,
url='',
license='',
author='',
author_email='',
description=''
"""
import os
import shutil

if __name__=='__main__':
    target_dir = "E:\\Users\\Halohoop\\Desktop\\halohoop"
    tail = ".halohoop"
    for i in os.walk(target_dir):
        dir_str = i[0]
        files_list = i[2]
        print("Dealing with " + dir_str)
        for file_name in files_list:
            if file_name.endswith(tail):
                new_file_name = file_name[0:-len(tail)]
                file_path = dir_str + os.sep + file_name
                new_file_path = dir_str + os.sep + new_file_name
                shutil.copy(file_path, new_file_path)
                os.remove(file_path)
