# -*- coding: utf-8 -*-
# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header begin-----------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

# __::((odmkFFmpeg.py))::__

# Python ODMK img processing research
# ffmpeg experimental

# *****************************************************************************
# /////////////////////////////////////////////////////////////////////////////
# header end-------------------------------------------------------------------
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# *****************************************************************************

import os
from math import ceil
import numpy as np
import matplotlib.pyplot as plt

# from subprocess import check_output, check_call
from subprocess import check_call

from odmkClear import *

# temp python debugger - use >>>pdb.set_trace() to set break
import pdb


# // *---------------------------------------------------------------------* //

clear_all()

# /////////////////////////////////////////////////////////////////////////////
# #############################################################################
# begin : function definitions
# #############################################################################
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# /////////////////////////////////////////////////////////////////////////////
# #############################################################################
# end : function definitions
# #############################################################################
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# // *---------------------------------------------------------------------* //

print('// //////////////////////////////////////////////////////////////// //')
print('// *--------------------------------------------------------------* //')
print('// *---::ODMK EYE ffmpeg Experiments::---*')
print('// *--------------------------------------------------------------* //')
print('// \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ //')

# /////////////////////////////////////////////////////////////////////////////
# #############################################################################
# begin : Loading & Formatting img and sound files
# #############################################################################
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::Search for .jpg images in eyeDir directory::---*')
print('// *--------------------------------------------------------------* //')

eyeDir = 'C:/usr/eschei/odmkPython/odmk/eye/imgSrc/exp1/'

# generate list all files in a directory
imgSrcList = []
try:
    for filename in os.listdir(eyeDir):
        if img.endswith('.jpg'):
            imgSrcList.append(filename)
    if imgSrcList == []:
        print('\nError: No .jpg files found in directory\n')
    else:
        imgCount = len(imgSrcList)
        print('\nFound '+str(imgCount)+' images in the eyeDir directory!')
        eye_name = imgSrcList[0]
        eye_name = eye_name.split("00")[0]
        print('\nSet eye_name = "'+eye_name+'"')
        print('\nCreated numpy array: <<imgSrcList>>\n')
except OSError:
    print('\nError: directory:\n'+eyeDir+'\ncannot be found\n')
    
print('// *--------------------------------------------------------------* //')

# /////////////////////////////////////////////////////////////////////////////
# #############################################################################
# begin : eye generator - ffmpeg function calls
# #############################################################################
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

movie_name = eye_name+'.mpg'
print('\nSet movie_name = '+movie_name)
print('\nRunning ffmpeg... '+eyeName)

overwrite = True
n_interpolation_frames = 1
frame_rate = 30
bitrate = '5000k'

# Find num digits required to represent max index
n_digits = int(ceil(np.log10(imgCount))) + 2

fmt_str = eye_name+'%'+str(n_digits)+'d.jpg'

movie_cmd = ["ffmpeg",
             '-an',  # no sound!
             '-r',  '%d' % frame_rate,
             '-i', os.path.join(eyeDir, fmt_str),
             '-y' if overwrite else '-n',
             # '-vcodec', codec,
             '-b:v', bitrate,
             movie_name]

check_call(movie_cmd)


# /////////////////////////////////////////////////////////////////////////////
# #############################################################################
# end : eye generator - ffmpeg function calls
# #############################################################################
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# // *---------------------------------------------------------------------* //

#plt.show()

print('\n')
print('// *--------------------------------------------------------------* //')
print('// *---::done::---*')
print('// *--------------------------------------------------------------* //')

# // *---------------------------------------------------------------------* //



