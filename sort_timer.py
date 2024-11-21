#Author: Jovane Cano
#GitHub User: jovanecano
#Date: 11/20/2024
#Description:

#importing necessary modules
import matplotlib.pyplot as plt
import random
import time
from functools import wraps

def sort_timer(func):
    '''a decorator function that will return the time (in seconds) it took for the sorting function to execute'''
    @wraps(func)
    def wrapper(arg1, arg2):
        start_time = time.perf_counter() #starting timeer
        func(arg1, arg2) #calls the sorting function
        end_time = time.perf_counter() #ends timer
        return end_time - start_time #returns the difference between end_time and start time
    return wrapper

@sort_timer
def bubble_sort(arr):
    '''bubble sort that will go through the list and swap elements if theyre in the wrong order'''
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j +1]: #swaps element in descending order if the next element is larger
                arr[j], arr[j +1] = arr[j +1], arr[j]

@sort_timer
def insertion_sort(arr):
    ''' insertion sort that will create a sorted list'''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]: #moves elements in order to make spacve for elements
            arr[j +1] = arr[j]
            j-= 1
        arr[j +1] = key #places key in correct index

def make_lists_of_sort_times(sort_func1, sort_func2, lengths):
    '''a function that will measure the sorting time for the two sorting algorightms for different list sizes'''
    times1 = [] #initializing empty list to store the times for the first sorting function
    times2 = [] #initializing empty list to store the times for the second sorting function
    for n in lengths:
        rand_list = [random.randint(1, 1000) for _ in range(n)]
        list1 = list(rand_list)
        list2 = list(rand_list)
        time1 = sort_func1(list1)
        time2 = sort_func2(list2)
        times1.append(time1)
        times2.append(time2)
    return times1, times2

def compare_sorts(sort_func1, sort_func2):
    '''function that will compare the performance of both sorting algorithms and plots the results of each'''
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    times1, times2 = make_lists_of_sort_times(sort_func1, sort_func2, lengths)

    plt.plot(lengths, times1, 'ro--', linewidth = 2, label='Bubble Sort') #plots the line for bubble sort
    plt.plot (lengths, times2, 'go--', linewidth=2, label='Insertion Sort') #plots line for insertion

    plt.xlabel('list size') #x-axis
    plt.ylabel('Time in seconds') #y-axis
    plt.title('Bubble Sort & Insertion Sort Performance Comparison') #title

    plt.show() #displays graph


    if __name__ == "__main__":
        compare_sorts(bubble_sort, insertion_sort)
