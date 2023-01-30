#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime as dt
import os


folderPath = os.path.dirname(os.path.abspath(__file__))


class Test(object):
    def run(self) -> None:
        # 创建子文件夹log
        logPath = os.path.join(folderPath, "log")
        if not os.path.exists(logPath):
            os.mkdir(os.path.join(folderPath, "log"))
        # 创建日志文件
        logPath += "/log.txt"
        with open(logPath, "a", encoding="utf-8") as f:
            f.write(str(dt.now())+"\n")


if __name__ == "__main__":
    Test().run()
