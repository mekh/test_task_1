#!/usr/bin/python
# Initial conditions: objects-figures of the next types are given: square, triangle, circle, trapezoid.
# Each figure can be drawn, the figure area or figure color can be obtained.
# Also, each of the figures has it's own unique methods. For example: get radius, length of hypotinuse,
# side's length, etc.
# 
# The task: generate random set of random number of figures.
# After array is generated, print the list of generated figures, for ex.:
# Figure: trapezoid, area: 15292.01 sq.u., height: 94.15 u., color: indigo
# Figure: circle, area: 30239.04 sq.u., circumference: 616.44 u., color: violet
# Figure: square, area:  2626.32 sq.u., side: 51.25 u., color: orange

import random
from math import pi as pi
import sys

class Figures():
  def __init__(self):
    self.color = random.choice(('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'))
    self.area = None
    self.name = None
    
  def get_color(self):
    return self.color

  def get_area(self):
    return self.area

  def draw(self):
    if not self.area or not self.name:
      return 'Nothing to draw.'
    else:
      return "Draw figure: %s, color: %s, area: %.2f sq.u." % (self.name, self.color, self.area)


class Triangle(Figures):
  def __init__(self):
    Figures.__init__(self)
    self.name = 'triangle'
    self.a, self.b = (random.uniform(1, 100) for x in range(2))
    self.c = (self.a**2 + self.b**2)**.5
    self.area = self.a * self.b/2.0

  def get_hypo(self):
    return self.c

  def __str__(self):
    return "Figure: %10s, area: %10.2f sq.u., hypotenuse: %14.2f u., color: %s" % (self.name, self.get_area(), self.get_hypo(), self.color)


class Trapezoid(Figures):
  def __init__(self):
    Figures.__init__(self)
    self.name = 'trapezoid'
    self.a, self.h, self.b1, self.b2 = (random.uniform(1, 100) for x in range(4))
    self.b = self.b1 + self.b2 + self.a     #   ____a____
    self.c = (self.b1**2 + self.h**2)**.5   # c/|      h|\d
    self.d = (self.b2**2 + self.h**2)**.5   # /_|___b___|_\
    self.area = (self.a + self.b)*self.h/2  # b1         b2

  def get_perimeter(self):
    return self.a + self.b + self.c + self.d

  def __str__(self):
    return "Figure: %10s, area: %10.2f sq.u., height: %18.2f u., color: %s" % (self.name, self.get_area(), self.h, self.color)


class Square(Figures):
  def __init__(self):
    Figures.__init__(self)
    self.name = 'square'
    self.a = random.uniform(1, 100)
    self.area = self.a**2

  def get_diagonal(self):
    return (2 * self.a**2)**.5
  
  def __str__(self):
    return "Figure: %10s, area: %10.2f sq.u., side: %20.2f u., color: %s" % (self.name, self.get_area(), self.a, self.color)


class Circle(Figures):
  def __init__(self):
    Figures.__init__(self)
    self.name = 'circle'
    self.r = random.uniform(1, 100)
    self.area = pi * self.r**2

  def get_C(self):
    self.circumference = 2 * pi * self.r
    return self.circumference

  def get_r(self):
    return self.r

  def __str__(self):
    return "Figure: %10s, area: %10.2f sq.u., circumference: %11.2f u., color: %s" % (self.name, self.get_area(), self.get_C(), self.color)


def str_to_class(str):
    return getattr(sys.modules[__name__], str)


def fnumber():
  while True:
    try:
      num = int(raw_input('Input the number of figures to generate: '))
      if num <= 0:
        print 'The number must be greater than zero!\nPlease try again.\n'
        continue
      else:
        return num
    except ValueError:
      print 'The number must be an integer!\nPlease try again.\n'
      continue

def main():
  figures = ('Trapezoid', 'Triangle', 'Square', 'Circle')
  num_to_generate = fnumber()

  figure_set = [random.choice(figures) for i in range(num_to_generate)]

  for item in figure_set:
    figure = str_to_class(item)()
    print figure

if __name__ == '__main__':
  main()
