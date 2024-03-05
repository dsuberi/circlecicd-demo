# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 6
        assert Add(5,5) == 25
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()