# Differences between `yield` and `return` in Python
## Purpose
**return** statement is used to exit a function and optionally return a value to the caller. 
It terminates the execution of the function and returns a value (or defaults to returning None).

**yield** statement is used to create a generator, which can generate a sequence of values.
yield pauses the execution of the function, saving its state to allow it to resume later. Each time the generator's next() method is called, it picks up where it left off, generating the next value.


## Usage
  ```python
  def example_function():
      # code block
      return result
  
  def generator_function():
      # code block
      yield value


def simple_function():
    return 1
    return 2  # This line will never execute

result = simple_function()
print(result)  # Output: 1


def generator_function():
    yield 1
    yield 2

gen = generator_function()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

def test(n):
    for i in range(1,n+1):
        yield i**2
for num in test(n):
    print(num) #打印1到n的平方

