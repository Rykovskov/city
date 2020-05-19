#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
import time
import sys
import traceback
import datetime
import compare_pic
from pathlib import Path
import imutils
import psycopg2

class Human:
    """This class ia a base human class"""
    human_count = 0
    age = 25

    def __init__(self):
        """Constructor"""
        pass
    def save_state(self):
        #Save state to base
        pass
