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

Create a github repository for this project. Go to [github](https://github.com/) and make a new repository named "circlecicd-demo".

Push the project (which is currently on the local computer) to the github repo. (Make sure to change the username to be yours. Mine is dsuberi.) In your terminal:

>git init

>git add .

>git commit -m "Initial commit"

>git remote add origin https://github.com/dsuberi/circlecicd-demo.git

>git push -u origin master


## 3. Setting Up CI With CircleCI

Our github repo is set up, now we want to enable CI on it by setting up CircleCI.

Create a configuration file so that CircleCI will know what we want it to do:
- Create a folder named ".circleci" and inside of it create a file named "config.yml".
- Open ".circleci/config.yml" and add the following code:

```yml
version: 2.1

jobs:
  build:
    working_directory: ~/circleci-python
    docker:
      - image: "cimg/python:3.8.4"
    steps:
      - checkout
      - run: python3 main.py
  test:
    working_directory: ~/circleci-python
    docker:
      - image: "cimg/python:3.8.4"
    steps:
      - checkout
      - run: python3 main-test.py

workflows:
  build_and_test:
    jobs:
      - build
      - test:
          requires:
            - build
```

- Notice that we have two types of tasks (jobs) that we want CircleCI to do: We want to run main.py, and we want to run our tests. We're also specifying that for every branch we want to perform the build job, and the test job.

- Push the new config file to github.

>git add .

>git commit -m "Adding CircleCI config file"

>git push

- We also need to give CircleCI access to our repo so that they're authorized to run these jobs. Go to [CircleCI's website](https://circleci.com/), login in with your github account, and authorize them to access your circlecicd-demo repo that we just created. 

  - Open [CircleCI](https://circleci.com/)
  - Click **"Got To Application"**
  - Click "**Signed up for CircleCI with GitHub**"
  - Click **Log in with Github**
  - After login, navigate to **Projects** Menu (left side)
  - Click **Set Up Project** button next to **circlecicd-demo**
  - Choose "**Fastest:** Use the .circleci/config.yml in my repo"
  - Click "**Set Up Project**"

- CircleCI should detect the code changes and run our build_and_test workflow for our branch. We should be able to see the jobs run on CircleCI's website.

## 4. Testing That CircleCI Is Working

We have CI running now so let's test it out. Let's add a line to our unit test for our Add function to make sure 5 + 5 is equal to 10.

Check out a new branch:

> git checkout -b add-test


​Add the following line of code to our TestAdd() function in "main-test.py":

```python
assert Add(5,5) == 10
```

Push this branch up to github.

> git add .

> git commit -m "Adds test to make sure 5 + 5 is equal to 10"

> git push --set-upstream origin add-test


Go to our github repo and make a Pull Request for this branch to see if CircleCI is running the jobs.

We should see a build job and a test job with green checkmarks since they pass. We have CI working properly.

Now, let's see what happens if we mess up old code by making our Add function do multiplication instead of tradition. In "main.py" change our Add function to multiply instead of add.

```python
return a * b
```

Commit this change and push our updated branch to github.

> git add .

> git commit -m "Add function now multiplies instead of adds"

> git push


If we look at our Pull Request, we should see that the build step passes since the code is still functional, but now our test fails since 2 * 3 isn't 5. So now we'd know the code change being introduced by this branch is harmful and we shouldn't merge this PR (and CircleCI can use that info to stop other jobs, like making sure not to deploy if the tests fail). 
