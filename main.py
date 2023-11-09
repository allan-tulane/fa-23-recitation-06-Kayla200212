def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    ###TODO
    if n == 0 or n == 1:
      return n
    else:
      return fib_recursive(n-1, counts)+fib_recursive(n-2,counts)
    
 
    
def fib_top_down(n, fibs):
    ###TODO
    if list[n] == -1:#if list isnt done
      if n==0 or n==1:#base 0 or 1
        fibs[n] = n
        return list[n]#return updated list
      else:#otherwise recursively do it and store values
        fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
    else:#or just return the list
      return list[n]


def fib_bottom_up(n):
    ###TODO
    list = [0] * (n+1)#list of n+1 elements set to 0
    list[1] = 1
    if n<=0:
      return [0]#cases with 0 or 1
    if n == 1:
      return [0,1]
    for i in range(2,n+1):#beginning at 2 and going from n+1
      list[i] = list[i-1] + list[i-2]#fibonacci step

    return list
    