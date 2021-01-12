# 0x09. Python - Everything is object

## Resources:books:
Read or watch:
* [9.10. Objects and values](https://intranet.hbtn.io/rltoken/n1x09X-KJSllpJkJorBw2A)
* [9.11. Aliasing](https://intranet.hbtn.io/rltoken/3teQMNNfDeyGvCtZfjsf5g)
* [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/JuPVygeoG27Q_qKxB2lP8g)
* [Mutation](https://intranet.hbtn.io/rltoken/UbL96sV3cIxewdQPW_zwRw)
* [9.12. Cloning lists](https://intranet.hbtn.io/rltoken/-t_1VsmKlgWHszL5y1YiKA)
* [Python tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/IdBAdTYNLuS3YpRRQIam6Q)

---
## Learning Objectives:bulb:
What I learned from this project:

* Why Python programming is awesome
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

---

### [0. Who am I?](./0-answer.txt)
* What function would you use to print the type of an object?


### [1. Where are you?](./1-answer.txt)
* How do you get the variable identifier (which is the memory address in the CPython implementation)?


### [2. Right count](./2-answer.txt)
* a = 89 and b = 100 point to the same object?


### [3. Right count =](./3-answer.txt)
* a = 89 and b = 89 point to the same object?


### [4. Right count =](./4-answer.txt)
* a = 89 and b = a point to the same object?


### [5. Right count =+](./5-answer.txt)
* a = 89 and b = a + 1 point to the same object?


### [6. Is equal](./6-answer.txt)
* If s1 = s2, what do print s1 == s2?


### [7. Is the same](./7-answer.txt)
* If s1 = s2, what do print s1 is s2?


### [8. Is really equal](./8-answer.txt)
* If s1 = "C" and s2 = "C", what do print s1 == s2?


### [9. Is really the same](./9-answer.txt)
* If s1 = "C" and s2 = "C", what do print s1 is s2?


### [10. And with a list, is it equal](./10-answer.txt)
* If l1 = [1] and l2 = [1], what do print l1 == l2?


### [11. And with a list, is it the same](./11-answer.txt)
* If l1 = [1] and l2 = [1], what do print l1 is l2?


### [12. And with a list, is it really equal](./12-answer.txt)
* If l1 = [1] and l2 = l1, what do print l1 == l2?


### [13. And with a list, is it really the same](./13-answer.txt)
* If l1 = [1] and l2 = l1, what do print l1 is l2?


### [14. List append](./14-answer.txt)
* If l1 = [1, 2, 3] and l2 = l1, and l1.append(2), what do print l2??


### [15. List add](./15-answer.txt)
* * If l1 = [1, 2, 3] and l2 = l1, and l1 = l1 + [2], what do print l2??


### [16. Integer incrementation](./16-answer.txt)
* If a = 1 and increment(a), what print a?
  ```python
  def incremente(n):
      n += 1
  ```


### [17. List incrementation](./17-answer.txt)
* If l = [1, 2, 3, 4] and increment(l), what print l?
  ```python
  def incremente(n):
      n.append(4)
  ```


### [18. List assignation](./18-answer.txt)
* If l1 = [1, 2, 3, 4] and l2 = [4, 5, 6] and assign_value(l1, l2), wat do print l1?
  ```python
  def incremente(n):
      n.append(4)
  ```


### [19. Copy a list object](./19-copy_list.py)
* A function def copy_list(l): that returns a copy of a list.


### [20. Tuple or not?](./20-answer.txt)
* If a = (), a is a tuple?



### [21. Tuple or not?](./21-answer.txt)
* If a = (1, 2), a is a tuple?



### [22. Tuple or not?](./22-answer.txt)
* If a = (1), a is tuple?



### [23. Tuple or not?](./23-answer.txt)
* If a = (1, ), a is tuple?



### [24. Who I am?](./24-answer.txt)
*  If a = (1) and b = (1), what do print a is b?


### [25. Tuple or not](./25-answer.txt)
* If a = (1, 2) and b = (1, 2), what do print a is b?


### [26. Empty is not empty](./26-answer.txt)
* If a = () and b = (), what do print a is b?


### [27. Still the same?](./27-answer.txt)
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```


### [28. Same or not?](./28-answer.txt)
```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

### [30. #pythonic](./101-locked_class.py)
* A function magic_string() that returns a string “Holberton” n times the number of the iteration.


### [31. Low memory cost](./103-line1.txt)
* A class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

<!--
### [32. int 1/3](./104-line1.txt)
* julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 



### [33. int 2/3](./105-line1.txt)
* julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 


-->
### [34. int 3/3](./106-line1.txt)
```python
print("I")
print("Love")
print("Python")
```
* [line1](./105-line1.txt): Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory?

### 35. Clear strings
```python
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
* [line1](./106-line1.txt): How many string objects are created by the execution of the first line of the script?
* [line2](./106-line2.txt): How many string objects are created by the execution of the second line of the script 
* [line3](./106-line3.txt): After the execution of line 3, is the string object pointed by a deleted?
* [line4](./106-line4.txt): After the execution of line 4, is the string object pointed by b deleted?
* [line5](./106-line5.txt): How many string objects are created by the execution of the last line of the script?
---

## Author
* **Estephania Calvo Carvajal** - [EstephaniaCalvoC](https://github.com/EstephaniaCalvoC)