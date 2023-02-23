import itertools
from tqdm import tqdm
import logging
import pandas as pd
import os
os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Countdown')
logging.basicConfig(filename='D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Countdownexample.log', level=logging.DEBUG)
if os.path.isfile('example.log'):
    os.remove('example.log')
else:
    print("File not found")


def countdown(numbers, target):
    
    # Generate all possible combinations of 1, 2, 3, 4, and 5 numbers
    number_combinations = []
    for i in range(1, len(numbers)):  
        number_combinations.extend(list(itertools.permutations(numbers, i)))
    
    operation_combinations_dict = {}
    # Generate all possible combinations of the arithmetic operations as operation_combinations_0,1,2,3
    for i in range(len(numbers)):
        variable_name = f"operation_combinations_{i}"
        operation_combinations_dict[i] = list(itertools.product(['+', '-', '*', '/'], repeat=i))
    
    # 
    solutions=[]
    for nums in tqdm(number_combinations, desc='Numbers'):
        t = len(nums)
        for ops in tqdm(operation_combinations_dict[t-1], leave=False):
            expression = ''
            for i in range(len(nums)):
                if i == len(nums) -1:
                    expression += str(nums[i])
                else:                    
                    expression += str(nums[i]) + ops[i]
            if expression == '':
                continue
            try:
                result = eval(expression)
                #logging.debug(str(nums)+str(ops)+str(expression) + " equals " + str(result))
                if result == target:
                    solutions.append(expression)
            except ZeroDivisionError:
                pass
    
    logging.shutdown()
    # If no solution is found, return None
    if not solutions:
        return None
    else:
        return solutions

numbers = [2, 3, 5, 10, 25, 50]
target = 100

solutions = countdown(numbers, target)

solutions_df = pd.DataFrame(solutions)
solutions_df = solutions_df.drop_duplicates()
solutions_df.to_csv("solutions.csWv")


if solutions:
    for solution in solutions:
        print(solution)
else:
    print("No solution found.")


# if solutions:
#     with open('solutions.txt', 'w') as f:
#         for solution in solutions:
#             f.write(solution + '\n')
#     print("Solutions written to solutions.txt")
# else:
#     print("No solution found.")