'''
file to find error in my first idea of solution for day 6

'''
import task
import task_2

sol_error = task.Solution('2024/Day_6/task.txt')
sol_correct = task_2.Solution('2024/Day_6/task.txt')

print(sol_error.solution_1())
print(sol_error.solution_2())

print(sol_correct.solution_1())
print(sol_correct.solution_2())

print(sol_error.lst_of_obstacles.difference(sol_correct.lst_of_obstacles))