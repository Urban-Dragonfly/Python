# Function that accepts positional or keyword arguments
def fun_default(a, b, c):
    pass

# Function that accepts only positional arguments
def fun_positional(a, b, c, /):
    pass

# Function that accepts only keyword arguments
def fun_keyword(*, a, b, c):
    pass

# Testing fun_default (should accept both positional and keyword arguments)
fun_default(1, 2, 3)           # Positional arguments
fun_default(a=1, b=2, c=3)     # Keyword arguments
fun_default(1, b=2, c=3)       # Mixed arguments

# Testing fun_positional (should accept only positional arguments)
fun_positional(1, 2, 3)        # Correct usage

# This should raise an error (TypeError)
try:
    fun_positional(a=1, b=2, c=3)
except TypeError as e:
    print(f"Error: {e}")

# Testing fun_keyword (should accept only keyword arguments)
fun_keyword(a=1, b=2, c=3)     # Correct usage

# This should raise an error (TypeError)
try:
    fun_keyword(1, 2, 3)
except TypeError as e:
    print(f"Error: {e}")