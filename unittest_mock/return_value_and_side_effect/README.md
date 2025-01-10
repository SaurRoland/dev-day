## Difference between side_effect and return_value
side_effect and return_value are similar in some ways. Ways that seem kind of counterintuative.
In Mock objects you have acces to the side_effect and return_value parameters.
The parameter return_value kind of speaks for itself, it allows you to return a value when mocking a method.

The parameter side_effect is where it gets "interesting".
It allows you to do a multitude of things, first off it can be used to raise an exception when the mock is called.
Second off, when you supply it with a function, it will call the function and return the value from the function.
Lastly, you can loop through a supplied iterable and return the values in it.

From the looks of it, side_effect seems to just do everything.