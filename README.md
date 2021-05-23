# oh-my-ds
Python library to pretty print data structures

# Installation

```python3
pip3 install ohmyds
```

# Usage

Right now only binary tree is supported

```python3

from ohmyds import binary_tree

root = binary_tree.create_tree([1,2,3,4,None,5,None,6,7,8])
```

For binary tree, you can do two operations right now - level order traversal and print

```python3
print(root)
```

The above command will print binary tree in a beautiful way (beauty is in the eyes of the beholder!)

```
 _1    
/  \   
3  2_  
 \   \ 
 5   4 
    / \
    7 6
```
