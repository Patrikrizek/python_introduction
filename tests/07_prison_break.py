# For this task create a program that determines the number of freed prisoners in the unique prison arrangement described below.
# A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.

# [1, 1, 0, 0, 0, 1, 0]
    # Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again. You can only move from left to right and not go back.

# So, if we use the example above:
# [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 1st cell
    # The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked

# [0, 0, 1, 1, 1, 0, 1] 
    # You free the prisoner in the 3rd cell (2nd one locked).
    # The locked cell 1st, 2nd and 6th become unlocked and the unlocked cells 3rd, 4th, 5th and 7th become locked

# [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 6th cell (3rd, 4th and 5th locked).
    # The locked cells 3rd, 4th, 5th and 7th become unlocked and the unlocked cells 1st, 2nd and 6th become locked

# [0, 0, 1, 1, 1, 0, 1]
# # You free the prisoner in the 7th cell - and you are done!

# Here, we have set free 4 prisoners in total.
# Create a program that, given this unique prison arrangement, returns the number of freed prisoners.

# Examples
    # freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4
    # freed_prisoners([1, 1, 1]) ➞ 1
    # freed_prisoners([0, 0, 0]) ➞ 0
    # freed_prisoners([0, 1, 1, 1]) ➞ 1

def freed_prisoners(prisoners):
  freed = 0
  
  for i in range(len(prisoners)):
    if prisoners[i] == 1: 
      freed += 1
      for j in range(len(prisoners)):
          prisoners[j] = 1 - prisoners[j] 
      if i==len(prisoners):
        break
  print(freed)
  
freed_prisoners([1, 1, 0, 0, 0, 1, 0])
freed_prisoners([1, 1, 1])
freed_prisoners([0, 0, 0])
freed_prisoners([0, 1, 1, 1])
