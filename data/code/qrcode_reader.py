import csv
import numpy as np
import pandas as pd
from pyzbar.pyzbar import decode
import cv2
from termcolor import colored


def get_qr_data(input_frame):
    """
    Decode the QR code from the input frame.
    """
    try:
        return decode(input_frame)
    except Exception as e:
        print(f"Error decoding QR code: {e}")
        return []

def draw_polygon(frame, qr_objects):
    """
    Draw a polygon around the QR code and display the decoded text.
    """
    for obj in qr_objects:
        text = obj.data.decode('utf-8')
        points = np.array([obj.polygon], np.int32).reshape((-1, 1, 2))
        cv2.polylines(frame, [points], True, (255, 100, 5), 2)
        cv2.putText(frame, text, (obj.rect.left, obj.rect.top - 10), cv2.FONT_HERSHEY_PLAIN, 2.5, (255, 100, 5), 2)
        print(colored(f"QR Code found: {text}", "green"))
    return frame

def check_device_in_csv(qr_data):
    """
    Check if the QR code data is present in the CSV file.
    """
    with open("data/devices.csv", mode='r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if qr_data in row:
                return True
    return False