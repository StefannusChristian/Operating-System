How to Run the Program:
python arrayreciprocal.py --thread (1 - number of your computer logical processors) --array (array size)

Example:
python arrayreciprocal.py --thread 8 --array 1000000
This means that the program will run the algorithm with 8 threads which means that
it will split the array with the size of 1000000 to 8 smaller arrays, then
it will simultaneously sum them.