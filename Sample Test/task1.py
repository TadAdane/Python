# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # import matplotlib.pyplot as plt
#
# import numpy as np
# import matplotlib.pyplot as plt
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# # file_r = open('data.txt', 'r')      # opens a file for reading
# # data = file_r.read()                # reads the whole file and saves to a string variable
# # file_r.close()                      # closes the file
# #
# # file_w = open('new_data.txt', 'w')  # opens a new file for writing
# # file_w.write(data)                  # writes contents of a variable to a file
# # file_w.close()                      # closes the second file
#
# file = open('data.txt', 'r')
#
# list_of_lines = file.read().splitlines()
#
# for line in list_of_lines:
#     print(line)
#
#
# for line in file.read().splitlines():  # for each line in file
#     numbers_strings = line.split('-')   # split the line into a list of strings
#                                         # the strings have to be converted to numeric values
#
#     numbers = []                        # create an empty list
#
#     for nbr in numbers_strings:         # for each element in the list of strings
#         numbers.append(int(nbr))        # convert the string to an integer and add to the list
#
#     print(sum(numbers))                 # sum all the integers
#
# file.close()
#
# x = np.linspace(0, 10, 1000)
# y = x**2
#
# plt.figure() # creates a new plot
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(["y=x^2"])
# plt.show() # show the plot window
#
# x = np.linspace(0, 10, 1000)
#
# plt.figure()
# plt.plot(x, 20*np.sin(x), 'r')
# plt.plot(x[::50], x[::50]**2, '^k')
# plt.plot(x, 5*np.cos(x), '--g')
# plt.legend(["y=20sin(x)", "y=x^2", "y=5cos(x)"])
# plt.show()

file_homework = open('homework.txt.txt', 'r')
line_of_words = file_homework.read().splitlines()
words_length = []
words = []
for separate_words in line_of_words:
    word_strings = separate_words.split(' ')
    #print(word_strings)

    for value in word_strings:
        if len(value) == 0:
            continue
        else:
            words_length.append(len(value))
            words.append(value)

    #print (words)

number_of_words = len(words_length)
#print (number_of_words)
sum = 0
for value in words_length:
    sum += value
print (sum/number_of_words)

for value in words:
    if value[0] == 'P':
        print(value)
    elif value[0] == 'p':
        print(value)