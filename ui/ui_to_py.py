# -*- coding: utf-8 -*-
"""
Created on Fri May 19 12:00:13 2023

@author: krpc1
"""

import os
ui_path = "C:/Users/krpc1/OneDrive/Masaüstü/ImgFilterAPP/ImgFilterAPP/ui/imagefilter.ui"
py_path = "C:/Users/krpc1/OneDrive/Masaüstü/ImgFilterAPP/ImgFilterAPP/ui/imgAppUI.py"
os.system(f"pyuic5 {ui_path} -o {py_path}")