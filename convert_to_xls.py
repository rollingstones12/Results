import pandas as pd
import json
import csv
from openpyxl import Workbook
import csv

arr = ['results_720_yolov2_resnet182',
'results_720_yolov2_resnet502',
'results_720_yolov3_resnet182',
'results_720_yolov3_resnet502',
'results_720_yolov3_tiny_resnet182',
'results_720_yolov3_tiny_resnet502',
'results_1080_yolov2_resnet182',
'results_1080_yolov2_resnet502',
'results_1080_yolov3_resnet182',
'results_1080_yolov3_resnet502',
'results_1080_yolov3_tiny_resnet182',
'results_1080_yolov3_tiny_resnet502']

for file in arr:
    # file_name = f+'.csv'
    # read_file = pd.read_csv(file_name)
    # read_file.to_excel(f+'xlsx', index=None, header=True)

    wb = Workbook()
    ws = wb.active
    with open('csv_files2/'+file +'.csv', 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save('xls_files/'+file+'.xlsx')