# Mocks: Regular, Magic and autospeced
Mocks are used for testing when we don't want to create a real object. 

To explore Mocks a bit more, here is a comparison between [Mock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock), [MagicMock](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock) and [autospecing an object](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec).
The main code is in [src](.src.py).

## Mock vs MagicMock
As is well known [MagicMocks](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock) differ from regular ones by providing mock dunder methods, e.g. `.__float()` no longer throws an error.

What surprised me a bit was that regular Mocks still come with some dunder methods  pre-configured: 
`__hash__`, `__str__` and `__sizeof__`are all present. Kind of make sense. These methods are very basic.


## autospec provides a MagicMock .... kind of
[create_autospec()](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.create_autospec) takes a class definition and will create a MagicMock specifically for that class: it knows which methods are there and their function signature.
This means that calling a non-existent method or calling a method with incorrect args/kwargs will fail on 
an autospeced mock but succeed in a regular MagicMock. As expected from python,  it does not do type checking.

A strange result of these restrictions is that while `create_autospec` returns a `MagicMock`, it does not set 
most of the dunder methods. For instance, if `__len__` is not defined in the input class it will also not be callable in the Mock object.
