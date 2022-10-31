import cv2
import medipipe as mp
import numpy as np
import time, os

action = ['come', 'away', 'spin']
seq_length = 30
secs_for_action = 30

mp_hands    = mp.solutions.hands
mp_drawing  = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands            = 1,
    min_detection_confidence = 0.5,
    min_traking_confidence   = 0.5
)

cap = cv2.VideoCapture(0)
