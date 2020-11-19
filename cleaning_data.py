#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:15:26 2020

@author: rommanesoukaina
"""

""" Cleaning data: removing html tags,  line breaks and replacing some charachters """
import re

def clean_data(text):
    clean_tags = re.compile('<.*?>')
    clean_data = re.sub(clean_tags, ' ', text)
    clean_data = clean_data.replace('&nbsp', ' ')
    clean_data = clean_data.replace('Java script', 'Javascript')
    clean_data = clean_data.replace('C++', 'cpp')
    clean_data = clean_data.replace('c ++', 'cpp')
    clean_data = clean_data.replace('C ++', 'cpp')
    clean_data = clean_data.replace('c++', 'cpp')
    clean_data = clean_data.replace('C#', 'csharp')
    clean_data = clean_data.replace('C #', 'csharp')
    clean_data = clean_data.replace('c#', 'csharp')
    clean_data = clean_data.replace('c #', 'csharp')
    clean_data = clean_data.replace('Front end', 'Front-End')
    clean_data = clean_data.replace('front end', 'Front-End')
    clean_data = clean_data.replace('back end', 'Back-End')
    clean_data = clean_data.replace('Back end', 'Back-End')
    clean_data = clean_data.replace('J2EE', 'JEE')
    clean_linebreaks = re.compile('\n')
    clean_data = re.sub(clean_linebreaks, ' ', clean_data)
    return (clean_data)

