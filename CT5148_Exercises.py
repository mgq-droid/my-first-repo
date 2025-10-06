# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 06:30:47 2025

@author: Admin
"""

def simulate(prog, xsize, ysize):
    """Given a "program" *prog*, run that program by "moving around" and
    tracking what happens. Use a set of tuples to track locations visited.

    Return the number of junctions visited and the number of
    time-steps used.
    
    Examples of usage and results:

    >>> simulate("NNN", 100, 100)
    (4, 3)
    >>> simulate("NNNSSS", 100, 100)
    (4, 6)
    >>> simulate("NNNESSS", 100, 100)
    (8, 7)
    >>> simulate("NNNNNSSSSS", 3, 3)
    (3, 10)
    >>> simulate(plan(10, 10), 10, 10)
    (100, 99)
    """
    x, y = 0, 0
    visited = {(0, 0)}
    steps = 0
    # Process each command in the program
    for command in prog:
      # Figure out where this command wants to go
      if command == 'N':
          new_x, new_y = x, y + 1
      elif command == 'S':
          new_x, new_y = x, y - 1
      elif command == 'E':
          new_x, new_y = x + 1, y
      elif command == 'W':
          new_x, new_y = x - 1, y
      else:
          continue  # Unknown command, skip it
      
      # Check if new position is valid (on the grid)
      if 0 <= new_x < xsize and 0 <= new_y < ysize:
          # Valid move - update position
          x, y = new_x, new_y
          visited.add((x, y))
          steps += 1
      # If invalid, do nothing (car is smart, ignores bad commands)
      return len(visited), steps
    

def plan(xsize, ysize):
     program = []
     for col in range(xsize): # go through each column
         if col % 2 == 0: # Even columns (0, 2, 4, ...)
              program.append('N' * (ysize - 1))
         else: # Odd columns (1, 3, 5 ...)
          # Go DOWN (south)
              program.append('S' * (ysize - 1))
          
      # Move to next column (expect at last column)
         if col < xsize - 1:
              program.append('E')
     return ''.join(program)
    
    """Given the city limits, return a program which moves around the 
    entire city. The program should be a string, eg "NNESS".

  By the way, notice that doctest will insist that the "expected"
  string, below, must be in single-quotes (''), not double-quotes
  ("").

  Our plan is: starting from the southwest, we traverse all the way
  northwards, then one step east, then all the way southwards, then
  one step east, and so on.

  >>> plan(2, 2)
  'NES'
  >>> plan(2, 3)
  'NNESS'
    """




  
    
   

    





