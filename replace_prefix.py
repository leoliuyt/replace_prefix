#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import re
# from os import path
if len(sys.argv) > 1:
    old = sys.argv[1]
if len(sys.argv) > 2:
    new = sys.argv[2]
if len(sys.argv) > 3:
    project_path = sys.argv[3]
else:
    print '传入的参数过多'

print '带替换字符串:{0};\n目标字符串:{1};\n项目路径:{2}'.format(old,new,project_path)
print '-----------------'

def replace_prefix(old,new,path = './'):
    '''对以{old}开头的文件名中的文本内容进行替换，并对文件重命名

    old:原文件名前缀
    new:替换后文件名前缀
    path:待替换文件查找路径
    '''
    file_objs = os.walk(path)  
    # (当前路径,当前路径下的文件夹,当前路径下的文件)
    for root, _, files in file_objs:
        for file in files:
            if file.startswith(old):
                print '发现以{0}开头的文件:{1}'.format(old,file)
                newfile = str(file).replace(old,new,1)
                old_path = root + file
                new_path = root + newfile
                file_content_replace(old_path,new_path,old,new)
                # os.rename(old_path,new_path)
                os.remove(old_path)
                
def file_content_replace(oldfile,newfile,old,new):
    '''文件内容的替换

    替换规则是:找到以old开头的单词，替换为新前缀new，保留原来格式，
    例如匹配出的为Art,替换为YD
    匹配出的为art,替换为yd
    '''
    fp = open(newfile,'w')  #打开你要写得文件test2.txt
    lines = open(oldfile).readlines()  #打开文件，读入每一行
    for s in lines:
        replacestr = file_content_replace_reg(old,new,s)
        fp.write(replacestr)
        #fp.write(s.replace(old,new).replace(old.lower(),new.lower()))    # replace是替换，write是写入
    fp.close()  # 关闭文件

def file_content_replace_reg(old,new,text):
    ''' 通过正则表达式匹配并替换前缀
    '''
    def replace_prefix_handle(matched):
        matchedStr = matched.group(0)
        if matchedStr.startswith(old):
            return matchedStr.replace(old,new)
        elif matchedStr.startswith(old.lower()):
            return matchedStr.replace(old.lower(),new.lower())
        else:
            return matchedStr
    reg = r'\b'+'[({0})({1})]'.format(old,old.lower())+r'\w*\b'
    return re.sub(reg,replace_prefix_handle,text)

replace_prefix(old,new,project_path)