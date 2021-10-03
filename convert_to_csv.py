import pandas as pd
import json
import csv

arr = ['results_144_yolov2_resnet18',
'results_144_yolov2_resnet50',
'results_144_yolov2_tiny_resnet18',
'results_144_yolov2_tiny_resnet50',
'results_144_yolov3_resnet18',
'results_144_yolov3_resnet50',
'results_144_yolov3_tiny_resnet18',
'results_144_yolov3_tiny_resnet50',
'results_360_yolov2_resnet18',
'results_360_yolov2_resnet50',
'results_360_yolov2_tiny_resnet18',
'results_360_yolov2_tiny_resnet50',
'results_360_yolov3_resnet18',
'results_360_yolov3_resnet50',
'results_360_yolov3_tiny_resnet18',
'results_360_yolov3_tiny_resnet50',
'results_720_yolov2_resnet18',
'results_720_yolov2_resnet50',
'results_720_yolov2_tiny_resnet18',
'results_720_yolov2_tiny_resnet50',
'results_720_yolov3_resnet18',
'results_720_yolov3_resnet50',
'results_720_yolov3_tiny_resnet18',
'results_720_yolov3_tiny_resnet50',
'results_1080_yolov2_resnet18',
'results_1080_yolov2_resnet50',
'results_1080_yolov2_tiny_resnet18',
'results_1080_yolov2_tiny_resnet50',
'results_1080_yolov3_resnet18',
'results_1080_yolov3_resnet50',
'results_1080_yolov3_tiny_resnet18',
'results_1080_yolov3_tiny_resnet50',
'results_2160_yolov2_resnet18',
'results_2160_yolov2_resnet50',
'results_2160_yolov2_tiny_resnet18',
'results_2160_yolov2_tiny_resnet50',
'results_2160_yolov3_resnet18',
'results_2160_yolov3_resnet50',
'results_2160_yolov3_tiny_resnet18',
'results_2160_yolov3_tiny_resnet50']

for f in arr:
    file_name = f
    with open(file_name+'.txt') as f:
        data = json.load(f)

    output = open(file_name+'.csv', 'w', encoding='UTF8')
    writer = csv.writer(output)

    row = ["Frame Number",'Vehicle Make','Probability',"Object ID"]
    writer.writerow(row)

    for ele in data.keys():
        for i in range(len(data[ele])):
             car_id = ele
             car_names = data[ele][i][0]
             car_prob = data[ele][i][1]
             frame_num = data[ele][i][2]
             for ind in range(len(car_names)):
                 row = [frame_num, car_names[ind], car_prob[ind], car_id]
                 writer.writerow(row)

# print(len(data['0'][0]))
# print(data['0'][0])
