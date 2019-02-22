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


def show(names) :
    print(names)

if __name__=='__main__':
    print("project start")
    # file_dir = "D:\\Python_os\\os"  # 注意 \\ ；windows 下是这么表示的；Linux 和 Mac 是 /
    # file_name = "test.txt"
    # file_abs = os.path.join(file_dir, file_name)  # os.path.join(...) 表示路径链接
    #
    # '''判断路径或文件'''
    # print(1, os.path.isabs(file_dir))  # 判断是否绝对路径
    # print(2, os.path.isabs(file_name))
    # print(3, os.path.isabs(file_abs))
    # print(4, os.path.exists(file_abs))  # 判断是否真实存在
    # print(5, os.path.exists(os.path.join(file_dir, "xxx")))
    # print(6, os.path.isdir(file_dir))  # 判断是否是个目录
    # print(7, os.path.isdir(file_abs))
    # print(8, os.path.isfile(file_dir))  # 判断是否是个文件
    # print(9, os.path.isfile(file_abs))


    # shutil.copytree("E:\\projects\\JavaProjects\\IdeaProjects\\LocationArithmetic\\j-xfactory-poi\\JmtoolCompare",
    #                 "E:\\Users\\Halohoop\\Desktop\\teste2")
    # print("project start")
    # 总文件夹
    des_dir_path = "E:\\Users\\Halohoop\\Desktop\\halohoop"
    file_tail = ".halohoop"
    if not os.path.exists(des_dir_path):
        os.mkdir(des_dir_path)
    target_paths = ["E:\\Users\\Halohoop\\Desktop\\ssss",
                    "E:\\projects\\AndroidStudioProjects\\2018\\201812\\ELBSSDK"]
    for tp in target_paths:
        target_path = tp
        print("Dealing with " + target_path)
        target_dir_name = target_path.split(os.sep)[-1]
        new_target_root_dir = des_dir_path + os.sep + target_dir_name
        if not os.path.exists(new_target_root_dir):
            os.mkdir(new_target_root_dir)
        if os.path.exists(target_path):
            for i in os.walk(target_path):
                # show(type(i[0]))
                # show(type(i[1]))
                # show(type(i[2]))
                # show(i[0])
                # show(i[1])
                # show(i[2])
                # shutil.copy()
                tmp_dir_str = i[0]
                tmp_dir_list = i[1]
                tmp_file_list = i[2]
                print("Dealing with " + tmp_dir_str)
                if tmp_dir_str.endswith(".git") or tmp_dir_str.endswith(".gradle") or tmp_dir_str.endswith(".idea") or tmp_dir_str.endswith("build") or tmp_dir_str.endswith("classes") or tmp_dir_str.endswith("target"):
                    continue
                # start cp
                if tmp_dir_str == target_path:
                    # cp dirs
                    for j in tmp_dir_list:
                        try:
                            if not os.path.exists(new_target_root_dir + os.sep + j):
                                os.mkdir(new_target_root_dir + os.sep + j)
                        except:
                            pass
                    # cp files
                    for j in tmp_file_list:
                        shutil.copy(tmp_dir_str + os.sep + j,
                                    new_target_root_dir + os.sep + j + file_tail)
                else:
                    relative_tmp_dir_str = tmp_dir_str.replace(target_path + os.sep, "")
                    # cp dirs
                    try:
                        try:
                            if not os.path.exists(new_target_root_dir + os.sep + relative_tmp_dir_str):
                                os.mkdir(new_target_root_dir + os.sep + relative_tmp_dir_str)
                        except:
                            pass
                    except:
                        pass
                    # cp files
                    for j in tmp_file_list:
                        if j.endswith(".iml"):
                            continue
                        shutil.copy(tmp_dir_str + os.sep + j,
                                    new_target_root_dir + os.sep + relative_tmp_dir_str + os.sep + j + file_tail)









