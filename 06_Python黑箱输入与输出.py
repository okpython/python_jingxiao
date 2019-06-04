#!/usr/bin/python
#coding=utf-8

# 输入输出基础
# 最简单直接的输入来自键盘操作

name = input('your name:')
gender = input('you are a boy?(y/n)')

welcome_str = 'welcome to the matrix {prefix} {name}.'
welcome_dict = {
    'prefix':'Mr.' if gender == 'y' else 'Mrs',
    'name':name
}

print('authorizing...')
print(welcome_str.format(**welcome_dict))






















