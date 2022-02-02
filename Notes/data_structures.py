'''

Data Structures:

    1. Linked List - 
     -> Good for inserting since we have a pointer to the locations.
     -> Bad for search since we have to iterate through every element in the worst case.

    2. Array - 
     -> You can do binary search in optimal time O (lg n)
     -> Bad for inserting since we need to move every location past a memory location for a single element to be inserted at that position.

    3. Heap - 
     -> We will use this for a Binary Search Tree (BST)
     -> Realization of an abstract data type called a priority queue
     -> What is a priority queue?
        -> Maintains a set S of elements x, with each element associated with a numerical key value
        -> Operations supported - 
           1. insert(S, x) - insert an element x into S
           2. min(S) - return the element with the minimum key associated
           3. extract_min(S) - do the same as min(S) but then delete that x from S.
           4. decrease_key(S,x,k) - decrease the key associated with x to k in S.
        -> A priority queue can be implemented using an array
    -> Binary min heap - 
       -> An array visualized as a binary tree
       -> Heap as an array (1 indexed) - 
          -> root: first element in the array - A[1]
          -> parent (i): floor (i/2) (index of the parent)
          -> left child (i): 2i (index of the left child)
          -> right child (i) 2i + 1 (index of the right child)
       -> This shows us the indices. What about the data?
       -> min heap property - 
          -> key(Parent(i)) <= key(i) (Ordering constraint), for all i > 1
          -> A[Parent(i)] <= A[i]
        -> Operations that can be performed - 
           -> Insert - # of comparisons O (lg n)
           -> Decrease-key - O (lg n)






    4. Binary Search Tree (BST) - 
    -> Rooted Binary Trees - 
       -> Empty
       -> Consists of a node called the root
       -> Order matters



'''
