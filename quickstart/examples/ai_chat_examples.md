# AI Chat Examples 🤖

Here are some practical examples of using Cursor's AI chat features:

## 1. Code Generation

### Generate a Function
```
Input: Create a function that validates an email address

Response: Here's a Python function to validate email addresses:

def validate_email(email: str) -> bool:
    """
    Validates an email address using regex pattern.
    
    Args:
        email: String containing the email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

### Generate a Class
```
Input: Create a simple bank account class

Response: Here's a Python class for a bank account:

class BankAccount:
    def __init__(self, account_number: str, balance: float = 0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance
    
    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdrawal", amount))
        return self.balance
```

## 2. Code Explanation

### Get Code Explanation
```
Input: /explain
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

Response: This is an implementation of the QuickSort algorithm. Here's how it works:

1. Base case: If array has 1 or fewer elements, return it (already sorted)
2. Choose a pivot: Selects middle element as pivot
3. Partition array into three parts:
   - left: elements less than pivot
   - middle: elements equal to pivot
   - right: elements greater than pivot
4. Recursively sort left and right partitions
5. Combine sorted parts: left + middle + right

The list comprehensions create the partitions efficiently.
```

## 3. Code Review

### Get Code Review
```
Input: /review
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

Response: Here's a review of the code:

Good:
✓ Simple and readable implementation
✓ Uses clear variable names
✓ Follows basic coding principles

Suggestions for improvement:
1. Add type hints for better clarity
2. Add error handling for empty lists
3. Add docstring for documentation
4. Consider using sum() built-in

Here's an improved version:

def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        float: The average value
        
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

## 4. Bug Fixing

### Fix Code Issues
```
Input: /fix
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n)  # Bug here!

Response: Here's the fixed version with explanation:

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence (0-based)
        
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  # Fixed recursive call

The bug was in the recursive call: fibonacci(n) should be fibonacci(n-2)
```

## 5. Documentation Generation

### Generate Documentation
```
Input: /docs
class Cache:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = {}
        self.access_count = {}
    
    def get(self, key):
        if key in self.cache:
            self.access_count[key] += 1
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if len(self.cache) >= self.max_size:
            least_used = min(self.access_count.items(), key=lambda x: x[1])[0]
            del self.cache[least_used]
            del self.access_count[least_used]
        self.cache[key] = value
        self.access_count[key] = 0

Response: Here's the documented version:

```python
class Cache:
    """
    A Least Frequently Used (LFU) cache implementation.
    
    This cache maintains a maximum size and evicts the least frequently accessed
    items when the cache is full.
    
    Attributes:
        max_size (int): Maximum number of items the cache can hold
        cache (dict): Storage for cached key-value pairs
        access_count (dict): Tracks number of accesses for each key
    """
    
    def __init__(self, max_size=100):
        """
        Initialize the cache.
        
        Args:
            max_size (int, optional): Maximum cache size. Defaults to 100.
        """
        self.max_size = max_size
        self.cache = {}
        self.access_count = {}
    
    def get(self, key):
        """
        Retrieve a value from the cache.
        
        Args:
            key: The key to look up
            
        Returns:
            The cached value or None if key not found
        """
        if key in self.cache:
            self.access_count[key] += 1
            return self.cache[key]
        return None
    
    def put(self, key, value):
        """
        Add or update a value in the cache.
        
        If the cache is full, removes the least frequently used item
        before adding the new item.
        
        Args:
            key: The key to store
            value: The value to cache
        """
        if len(self.cache) >= self.max_size:
            least_used = min(self.access_count.items(), key=lambda x: x[1])[0]
            del self.cache[least_used]
            del self.access_count[least_used]
        self.cache[key] = value
        self.access_count[key] = 0
```