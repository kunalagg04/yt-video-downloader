# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:18:37 2019

@author: Kunal Aggarwal
"""

import pytube

video_link = "https://www.youtube.com/watch?v=LW9pT246LrI"

yt = pytube.YouTube(video_link)

videos = yt.streams.first()

videos.download('C:\\\Users\\\Public')


