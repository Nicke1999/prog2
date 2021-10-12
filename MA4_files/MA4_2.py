#!/usr/bin/env python3

from integer import Integer
import matplotlib.pyplot as plt
from time import perf_counter 

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.Fib(40))

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

if __name__ == '__main__':
	#n = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
	#times_python = []
	#times_cpp = []
	#f = Integer(2)
	#for num in n:
		#start_py = perf_counter()
		#fib_py(num)
		#end_py = perf_counter()
		#time_py = end_py-start_py
		#times_python.append(time_py)
		#start_cpp = perf_counter()
		#fibonacci = f.Fib(num)
		#end_cpp = perf_counter()
		#time_cpp = end_cpp-start_cpp
		#times_cpp.append(time_cpp)
	#plt.plot(n, times_python, 'o', color = 'blue')
	#plt.plot(n, times_cpp, 'o', color = 'red')
	#plt.xlabel('N')
	#plt.ylabel('Time')
	#plt.title('Time Fibonacci')
	#plt.legend(['Pure Python','C++'])
	#print(f.Fib(47))
	#plt.show() 
	main()

# When we run fib for n = 47 we get a negative number. That is due to integer overflow and how C++ deals with that. When we hit
# the number that is big c++ basically loops back to the beginning at negative numbers.
