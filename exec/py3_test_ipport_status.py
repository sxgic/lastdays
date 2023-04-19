# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 批量测试端口号
import sys
import telnetlib

def telnet(host, port):
    """
    测试端口号通不通
    :return:
    """
    try:
        #  timeout单位s
        telnetlib.Telnet(host = host, port = port, timeout = 2)
        print(f"{host} {port} 端口开放")
    except:
        print(f"{host} {port} 端口未开放")
        # 或什么都不打印
        # pass

def for_port():
    """
    添加端口到列表中
    使用示例: python3 telnet_for.py 39.105.137.91 81 82 83 84
    :return:
    """
    port_list = [
        "120.55.66.68:13000",
        "120.55.66.68:13001",
        "120.55.66.68:13002",
        "120.55.66.68:13003",
        "121.40.169.210:13000",
        "121.40.169.210:13001",
        "121.40.169.210:13002",
        "121.40.169.210:13003",
        "118.178.239.90:13000",
        "118.178.239.90:13001",
        "118.178.239.90:13002",
        "118.178.239.90:13003",
        "121.41.40.81:13000",
        "121.41.40.81:13001",
        "121.41.40.81:13002",
        "121.41.40.81:13003"
    ]

    for ip_port in port_list:
        info = ip_port.split(":")
        telnet(info[0], info[1])

if __name__ == '__main__':
    for_port()

