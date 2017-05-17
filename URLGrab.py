# -*- coding: utf-8 -*-
#! /usr/bin/env python3

'''
This code is modified from pymbook.readthedocs.io
I'm using it as a jumping-off point
'''

import requests
import os
import sys

def download_url(url):
    ''' download URL, save to current directory '''
    req = requests.get(url)
    #uses string argument, returns requests.models.Response object
    if req.status_code == 404:
        print("No such file found at {}".format(url))
        return
    filename = url.split('/')[-1]
    if filename in os.listdir():
        print("Filename {} already exists!".format(filename))
        return
    with open(filename, 'w') as fobj:
        fobj.write(req.text)
        # type of req.content is bytes
        print("Download over.")
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("One URL argument please.")
        sys.exit(0)
    download_url(sys.argv[1])
    