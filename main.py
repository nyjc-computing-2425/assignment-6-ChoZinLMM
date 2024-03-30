from datetime import datetime
import time

# Part 1
def clock(n):
    """
    """
    seconds = 0
    while seconds < n:
      print(time.strftime("%H:%M:%S"))
      seconds += 1
      time.sleep(1)

# Part 2
def lcm(a, b):
    """
    """
    while a != b:
      if a < b:
        a += a
      elif b < a:
        b += b
    else:
      return(a)


# Part 3
def gcf(a, b):
    """
    """
    if b == 0:
      return(a)
    else:
      while b != 0:
        r = a % b
        a = b
        b = r
        if b == 0:
          break
      else:
        return(a)

  
