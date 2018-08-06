# CS50 Note
## Git
### Clone repository
> git clone `<url>`
### Track Files
> git add `<file>`
### Git Commit
>git commmit -m "`<messege>`"
### Git Push
> git push
### Git Pull
> git pull
### Check status
> git status
### View Log
> git log

> git reflog
### Go to History Version
> git reset --hard `<commit>`
>
> git reset --hard origin/master
## HTML
### List
#### Unordered List
```HTML
<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>
```
#### Ordered List
```HTML
<ol>
  <li></li>
  <li></li>
  <li></li>
</ol>
```
### Table
```HTML
<table>
  <tr>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
</tr>
</table>
```
### CSS import
```HTML
<link rel="stylesheet" href="style.css">
```
## Python
### Simple Example
```Python
name = input()
print(f"hello,{name}")
```
```
> dudu
> hello,dudu
```
### Types
#### Basic Types
```Python
i = 28 //integer
f = 2.8 //float
b = True //boolean
n = None //uninitialize?
```
#### String
```Python
name = "Alice"
```
#### Tuple
```Python
coordinates = (10.0,20.0)
```
#### List
```Python
names = ["Alice", "Bob", "Charlie"]
l = [28, "Alice", True]
```
#### Set
```Python
s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)
```
```
> {1,3,5}
```
#### Dictionary
```Python
ages = {"Alice":22, "Bob":27}
ages["Charlie"] = 30
ages["Alice"] += 1
print(ages)
```
```
> {'Alice':23, 'Bob':27, 'Charlie':30}
```
### Basic Logic
#### If
```Python
x = 28
if x > 0:
  print("x is positive")
elif x < 0:
  print("x is negative")
else
  print("x is zero")
```
```
> x is positive
```
#### For
```Python
names = ["Alice","Bob","Charlie"]
for name in names
  print(name)

for i in range(5)
  print(i)//print i from 0 to 4 each line
```
```
> 0
> 1
> 2
> 3
> 4
```
### Function
#### Simple Function
```Python
def square(x):
  return x * x

for i in range(5)
  print("{} squared is {}".format(i,square(i)))
```
```
> 0 squared is 0
> 1 squared is 1
> 2 squared is 4
> 3 squared is 9
> 4 squared is 16
```
#### Use Function in Another Program
modules.py
```Python
from functions import square

print(square(10))
```
functions.py
```Python
def square(x):
  return x * x

def main():
  for i in range(5)
    print("{} squared is {}".format(i,square(i)))

if __name__ == "__main__":
  main()
```
### Class
#### Simple Class
```Python
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)
```
```
> 3
> 5
```
