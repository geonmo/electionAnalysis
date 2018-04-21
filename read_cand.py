# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os, sys, time
from croll import NewsCrawler 
import urllib.request
import urllib.parse
import datetime
from bs4 import BeautifulSoup

infile = open("vote.csv")
line = infile.readline().split(',')

outfile = open("output.csv","w")

for line in infile.readlines() :
    line_spl = line.split(",")
    #print(line_spl)
    name, wide, region = line_spl[5], line_spl[1], line_spl[2]

    keyword = "%s %s %s"%(name, wide, region)
    nc = NewsCrawler(keyword, "")
    time.sleep(0.2)
    result= "%s, %d, %s\n"%(name,nc.getTotal(), nc.getInfo())
    print(result)
    outfile.write(result)


