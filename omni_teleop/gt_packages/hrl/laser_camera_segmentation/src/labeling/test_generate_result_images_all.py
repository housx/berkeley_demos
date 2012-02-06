#!/usr/bin/python
#
# Copyright (c) 2010, Georgia Tech Research Corporation
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Georgia Tech Research Corporation nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY GEORGIA TECH RESEARCH CORPORATION ''AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL GEORGIA TECH BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

#  \author Martin Schuster (Healthcare Robotics Lab, Georgia Tech.)
import roslib; roslib.load_manifest('laser_camera_segmentation')


import laser_camera_segmentation.processor as processor
import laser_camera_segmentation.configuration as configuration       
        
import time 

from dumpObj import dumpObj

import subprocess    
        
cfg = configuration.configuration('/home/martin/robot1_data/usr/martin/laser_camera_segmentation/labeling')
pc = processor.processor(cfg)

#testresults_all = pc.load_testresults_all()
#print testresults_all
#pc.print_testresults_all_latex(testresults_all)

scan_dataset = pc.scans_database.get_dataset(0)
#get size of training set in total
while False != scan_dataset:
    if scan_dataset.is_labeled: #former: is_testset
        output = subprocess.Popen(["python", 'test_generate_result_images.py',str(scan_dataset.id)]).communicate()[0]
    
    #get next one
    scan_dataset = pc.scans_database.get_next_dataset()