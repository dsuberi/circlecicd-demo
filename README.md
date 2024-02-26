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





