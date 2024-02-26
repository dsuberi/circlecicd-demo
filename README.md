## 1. Create a Simple Python Project

Create a folder circlecicd-demo

Load the above folder in VS Code

Create a new file “main.py” inside the circlecicd-demo folder.

Write the following codes in "main.py"

```python
def Add(a, b):
        return a + b
        
def SayHello():
        print("Hello CIS 411")

if __name__ == '__main__':
        SayHello()
```
Run this file with following command in your terminal to get the Hello message

> python3 main.py

Create a file named "main-test.py" to test our main file.

```python
# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()
```

Run this file with following command in your terminal

>python3 main-test.py

## 2. Push The Project To Github

Create a github repository for this project. Go to (github)[https://github.com/] and make a new repository named "circlecicd-demo".

Push the project (which is currently on the local computer) to the github repo. (Make sure to change the username to be yours. Mine is dsuberi.) In your terminal:

>git init
>git add .
>git commit -m "Initial commit"
>git remote add origin https://github.com/dsuberi/circlecicd-demo.git
>git push -u origin master



