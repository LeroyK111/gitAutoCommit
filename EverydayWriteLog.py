#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime as dt
import os
import random


folderPath = os.path.dirname(os.path.abspath(__file__))


class Test(object):
    def run(self) -> None:
        # 创建子文件夹log
        logPath = os.path.join(folderPath, "src")
        if not os.path.exists(logPath):
            os.mkdir(os.path.join(folderPath, "src"))
        # 创建文件
        xxx = random.random()
        logPath += "/%s.py" % xxx
        with open(logPath, "a", encoding="utf-8") as f:
            f.write(str(dt.now()) + str(xxx) + "\n")


if __name__ == "__main__":
    Test().run()
