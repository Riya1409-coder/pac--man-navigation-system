class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self._data = []

    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, s):
        self._data.append(s)

    def top(self):
        return self._data[-1]
    
    def pop(self):
        return self._data.pop()
    
    def get(self):
        return self._data
    # You can implement this class however you like