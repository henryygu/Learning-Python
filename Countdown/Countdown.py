import itertools
from tqdm import tqdm
import logging
import pandas as pd
os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Countdown')
logging.basicConfig(filename='D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\Countdownexample.log', level=logging.DEBUG)
if os.path.isfile('example.log'):
    os.remove('example.log')
else:
    print("File not found")


def countdown(numbers, target):
    
    # Generate all possible combinations of 1, 2, 3, 4, and 5 numbers
    number_combinations = []
    for i in range(1, 6):  
        number_combinations.extend(list(itertools.permutations(numbers, i)))
    
    # Generate all possible combinations of the arithmetic operations
    operation_combinations_5 = list(itertools.product(['+', '-', '*', '/'], repeat=len(numbers)-1))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Try each combination of numbers and operations
    solutions = []
    list_of_expressions=[]
    for nums in tqdm(number_combinations, desc='Numbers'):
        for ops in tqdm(operation_combinations, desc='Operations', leave=False):
            expression = ''
            for i in range(len(nums)-1):
                expression += str(nums[i]) + ops[i]
            list_of_expressions.append(expression)
            
            if expression in list_of_expressions:
                continue
            else:
                expression += str(nums[-1])
            list_of_expressions.append(expression)
            
            
            try:
                result = eval(expression)
                logging.debug(str(nums)+str(ops)+str(expression) + " equals " + str(result))
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
solutions_df.to_csv("solutions.csv")


# if solutions:
#     for solution in solutions:
#         print(solution)
# else:
#     print("No solution found.")


# if solutions:
#     with open('solutions.txt', 'w') as f:
#         for solution in solutions:
#             f.write(solution + '\n')
#     print("Solutions written to solutions.txt")
# else:
#     print("No solution found.")