from unittest.mock import Mock, MagicMock, create_autospec

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.rage: int = 0


    def __repr__(self) -> str:
        return f"Hello, I'm {self.name} and {self.age} years old"
    
    def rageup(self, annoyance: int) -> None:
        self.rage += annoyance

    def complain(self, topic: str, target: str = "void") -> str:
        return f"You know what {target}, I am {self.rage} points annoyed by {topic}"
    def __len__(self) -> int:
        return self.age


def annoy(person: Person, annoyance: int) -> None:
    person.rageup(annoyance)


DUNDER_METHODS = [
    "__lt__",
    "__gt__",
    "__le__",
    "__ge__",
    "__int__",
    "__contains__",
    "__len__",
    "__iter__",
    "__exit__",
    "__aexit__",
    "__complex__",
    "__float__",
    "__bool__",
    "__index__",
    "__hash__",
    "__str__",
    "__sizeof__"
]

basic_mock = Mock()
magic_mock = MagicMock()
person_spec_mock = create_autospec(Person)
mock_variety = [(basic_mock, "basic_mock"), (magic_mock, "magic_mock"), (person_spec_mock, "person_spec_mock")]


assert isinstance(person_spec_mock, MagicMock)
print("auto_spec mock is a MagicMock")

for mock, name in mock_variety:
    print(50*"=")
    print(f"Trying to access some methods of {name}")
    print(50*"=")
    try:
        mock.complaint()
        print(f"Successfully called non_existent method on {name}")
    except:
        print(f"Failed to call non_existent method on {name}")

    try:
        mock.complain("LINQ", "home", 4)
        print(f"Successfully called method with incorrect number of parameters on {name}")

    except:
        print(f"Failed to call method with incorrect number of parameters on {name}")

    try:
        mock.complain("LINQ", tafget="Bob")
        print(f"Successfully called method with incorrect keyword agrument on {name}")
    except:
        print(f"Failed to call method with incorrect keyword agrument on {name}")


    try:
        mock.complain("LINQ", target=Person("Bob", 56))
        print(f"Successfully called method with incorrect type for keyword argument on {name}")
    except:
        print(f"Failed to call method with incorrect type for keyword argument on {name}")


    for dunder_method in DUNDER_METHODS:
        try:
            dunder = getattr(mock, dunder_method)
            dunder()
            print(f"Successfully called dunder method {dunder_method} on {name}")
        except:
            print(f"Failed to call dunder method {dunder_method} on {name}")


