# PSW
This is a simple python password storage system can be used to store and retrieve API key from a binary file

## Modes Of Operations
This Python module has two mode `Sign up` and `login` .
For Sign up you can use the following code example 
```python
import pws
pws.sign_up()
```
For login you can use the following code example
```python
import pws
a = str(input("Enter your username: "))
b = str(input("Enter your password: "))

pws.login(a, b)
```

For further privacy you can use the `getpass` module in the password section
```python
import pws
from getpass import getpass as p
a = str(input("Enter your username: "))
b = p("Enter your password: ")

pws.login(a, b)
```
