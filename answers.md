# CMPS 2200 Recitation 06
## Answers

**Name:**__kayla willis_______________________
**Name:**__cameron mclaren_______________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
W(n) = W(n - 1) + W(n - 2) + C

W(n) = 2W(n-1) + C W(n) = 4W(n-2) + 3C W(n) = 8W(n-3) + 3C

W(n) = 2^k (n - k) + (2^k - 1)C

W(0):
n - k = 0
k = n W(n) = 2^k W(0) + (2^n - 1)C ≈ 2^n

Therefore, the work of the algorithm is O(2^n)
- **3)**
S(n) = S(n-1) + 1

root value = 1 
level 1 value = 1

(the recursion tree is balanced --> max cost per level multiplied by the number of levels)

1 * n --> Therefore, the span of the algorithm belongs in O(n) 
- **4)**
The value of counts will grow like the fibonacci sequence does, representing how many times the fibonacci sequence is called when computing the fibonacci number in question. example: counts[1] and counts[0] will both be called only once whereas counts[4] will be called for n=4 once and each time for n=3 and n=2 and n=1.
- **6)**
The max times itll be called is n. The algorithm will be called from the input of n until it reaches 0. Thus the work will be n as well as the span. It is a linear function.
- **8)**
It will be read twice since we are taking the input n and checking n-1 and n-2, so two times. This will also have O(n) work and span because it is also a linear function proportional to the number n. It is not performed recursively.