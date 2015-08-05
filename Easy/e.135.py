#!/usr/bin/env python

import random
from sys import argv

script, n1, n2 = argv 

def random_operations(n1, n2):
  while True:
    equation = ''
    for cycle in range(4):
      equation += str(random.randint(int(n1), int(n2))) + ' '
      equation += random.choice(['+','-','*']) + ' '

    equation = equation[:-2]  #snips that extra operation
    print equation   
    answer = raw_input('>')
    result = eval(equation)
  
    if answer in 'qQ':
      break
    elif not answer.isdigit():
      print 'Enter integer next time.'
      continue
    elif int(answer) == result:
      print 'Correct!'
    else:
      print 'Incorrect...' 
   
 
random_operations(n1, n2)
