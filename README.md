# Probabilistic Graphical Model HW1
Implement a method/function which takes a matrix representation of a DAG as input, along with a d-seperation query,
and outputs a value TRUE or FALSE. Specifically, there is an attached dag.txt file on Piazza that accompanies this
assignment, which is a 100x100 matrix of zeroes and ones. This matrix represents a DAG in the following way: if
Xi → Xj then the ij entry is 1, otherwise it is 0. Your function should come with an executable file which takes the
matrix as input, along with a query of the form: number number list, and returns TRUE iff the variables corresponding to those numbers are d-separated given the numbers in list. You may implement d-separation anyway
you like, but do not use implementations of d-seperation that are already out there in available software. The point
of this excercise is to get practice implementing this concept yourself, not to copy some code off the internet or out
of the source of some available software package. Furthermore, your implementation should work for matrices of any
(reasonable) size, not just 100x100.
