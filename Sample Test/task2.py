#
# import requests
# import numpy as np
#
# req = requests.get("https://jug.dpieczynski.pl/proj-eocst/_resources/python/_resources/test_2_sample/data_sample.csv")
# print(req)
#
# number = []
# for value in req:
#     number.append(value)
# print(number[0])
# print(number[1])

import  numpy as np
import csv
import requests
import matplotlib.pyplot as plt

# CSV_URL = 'https://jug.dpieczynski.pl/proj-eocst/_resources/python/_resources/test_2_sample/data_sample.csv'
#


req = requests.get("https://jug.dpieczynski.pl/proj-eocst/_resources/python/_resources/test_2_sample/data_sample.csv")
req_text = req.text
# print (req_text)
req_arr = np.genfromtxt(req_text.strip().split('\n'), delimiter=',')

# req_arr = np.array(req_text)
x = req_arr[ :,0]
y1 = req_arr[ :,1]
y2 = req_arr[ :,2]
y3 = req_arr[ :,3]

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xticks(color='w')
plt.yticks(color='w')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# with requests.Session() as s:
#     download = s.get(CSV_URL)
#
#     decoded_content = download.content.decode('utf-8')
#
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#
#     numbers = []
#     for row in my_list:
#         numbers.append(row)
#     num_array = np.array(numbers)
#     #print (num_array)
#
#     x = num_array[ :,0]
#     x.sort()
#     print (x[0])
#     # print ("___________________________________________________________________________________________")
#     y1 = num_array[ : ,1]
#     y2 = num_array[ : ,2]
#     y3 = num_array[ : ,3]
#
#
#     #y1.sort()
#     #print(y1)
#     print (y1[0])
#     # print ("___________________________________________________________________________________________")
#     # print (y2)
#     # print ("___________________________________________________________________________________________")
#     # print (y3)
#     # print ("___________________________________________________________________________________________")
#
#     plt.figure()  # creates a new plot
#     plt.plot(x, y1)
#     # plt.plot(x, y2)
#     # plt.plot(x, y3)
#     # plt.xticks(color='w')
#     # plt.yticks(color='w')
#     #plt.xlabel('x')
#     #plt.ylabel('y')
#     # x1 = [1, 2, 3, 4, 5]
#     # y_ = [2, 0, -2, 0, 2]
#     # plt.plot(x1, y_)
#
#     plt.show()
#
#     # plt.figure()  # creates a new plot
#     # plt.plot(x, y2)
#     # #plt.xlabel('x')
#     # #plt.ylabel('y')
#
#     # plt.show()
#     #
#     # plt.figure()  # creates a new plot
#     # plt.plot(x, y3)
#     # #plt.xlabel('x')
#     # #plt.ylabel('y')
#     #
#     # plt.show()
#     # # print (num_array.shape[0])
#     # # print (num_array.shape[1])

# url = "https://jug.dpieczynski.pl/proj-eocst/_resources/python/_resources/test_2_sample/data_sample.csv"
# response = requests.get(url)
# text = response.text
#
# # Convert the text into a numpy array
# data = np.genfromtxt(text.strip().split('\n'), delimiter=',')
#
#     # Get the number of columns
# num_cols = data.shape[1]
#
#     # Plot the data
# for i in range(1, num_cols):
#     plt.plot(data[:, 0], data[:, i])
#
# plt.show()