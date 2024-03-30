import time

# Part 1
def clock(n):
    """
    Parameters
    ----------
    n = int
      represents the number of seconds

    Prints
    ------
    The time every second, for n number of seconds
      """
    seconds = 0
    while seconds < n:
      print(time.strftime("%H:%M:%S"), end = "\r")
      seconds += 1
      time.sleep(1)

# Part 2
def lcm(a, b):
    """
    Function to find the lowest common multiple of a and b
    Parameters
    ----------
    a = integer
    b = integer

    Returns
    --------
    The lowest common multiple of a and b
    """
    a_original = a
    b_original = b
    while a != b:
      if a < b:
        a += a_original
      elif b < a:
        b += b_original
    
    return(a)

#Part 3
def gcf(a, b):
    """
    Parameters
    ----------
    a = int
    b = int

    Returns
    -------
    The greatest common factor of a and b
    """
    if b == 0:
      return(a)
    else:
      while b != 0:
        r = a % b
        a = b
        b = r   
      
      return(a)