#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2020-12-10
# @Author  : mh

import os
from PyPDF2 import PdfReader, PdfWriter
import time

INPUT_FILE = "数据挖掘与应用（SAS）（张俊妮）.pdf"   # 待分割文件
OUTOUT_FILE_NAME = "dataminingsplit"  # 分割后的文件名
SUBFILE_PAGE_NUM = 70  # 分割页数


def subsplit(a, reader, pageCount):
    output = PdfWriter()
    outfile = OUTOUT_FILE_NAME + str(a) + ".pdf"  # 分割后的文件

    for ipage in range(SUBFILE_PAGE_NUM):
        kp = ipage + SUBFILE_PAGE_NUM * a
        if kp < pageCount:
            output.add_page(reader.pages[kp])

    # 写入到目标PDF文件
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()


def split():
    reader = PdfReader(open(INPUT_FILE, "rb"))
    pageCount = len(reader.pages)

    subFileNum = (int)(pageCount / SUBFILE_PAGE_NUM)
    if pageCount % SUBFILE_PAGE_NUM > 0:
        subFileNum += 1

    for k in range(subFileNum):
        subsplit(k, reader, pageCount)


if __name__ == '__main__':
    time1 = time.time()
    split()
    time2 = time.time()
    print('time consumed %s s.' % (time2 - time1))
