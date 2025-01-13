from unittest.mock import Mock
import uuid

UUID_ERROR_MESSAGE = "The mocked uuid was not as expected"

class ElectricComponent:
    def __init__(self, component_type: str, component_id: int):
        self.component_type = component_type
        self.component_id = component_id

class IdentifierGenerator:
    @staticmethod
    def generate_uuid(component: ElectricComponent) -> str:
        seed = f"{component.component_type}-{component.component_id}"
        return uuid.uuid5(uuid.NAMESPACE_DNS, seed)


def mock_uuid(component: ElectricComponent):
    return f"{component.component_type}-{component.component_id}"



# Using a literal return in return_value
try:
    cable = ElectricComponent("cable", 1)
    IdentifierGenerator.generate_uuid = Mock(return_value="cable-1")
    assert IdentifierGenerator.generate_uuid(cable) == "cable-1"
    print("The mocked uuid is as expected")

    # Won't work because the value does not change
    cable.component_id = 2
    assert IdentifierGenerator.generate_uuid(cable) == "cable-2"
    print("The mocked value dynamically changes")
except AssertionError:
    print(UUID_ERROR_MESSAGE)

# Try to mock the generated uuid with method as return value
try:
    cable = ElectricComponent("cable", 1)

    # This does not work because it returns the method
    IdentifierGenerator.generate_uuid = Mock(return_value=mock_uuid)
    cable_uuid = IdentifierGenerator.generate_uuid(cable)
    assert cable_uuid == "cable-1"
except AssertionError:
    print(UUID_ERROR_MESSAGE)

# Different method of using method as return value
try:
    cable = ElectricComponent("cable", 1)

    # This doesn't work because it misses parameters
    IdentifierGenerator.generate_uuid = Mock(return_value=mock_uuid())
    cable_uuid = IdentifierGenerator.generate_uuid(cable)
    assert cable_uuid == "cable-1"
except TypeError as e:
    print(e)

# Use side_effect to mock a generated uuid
try:
    cable = ElectricComponent("cable", 1)
    IdentifierGenerator.generate_uuid = Mock(side_effect=mock_uuid)
    assert IdentifierGenerator.generate_uuid(cable) == "cable-1"
    print("The mocked uuid was as expected")

    # Works because the parameters used with mock_uuid change
    cable.component_id = 2
    assert IdentifierGenerator.generate_uuid(cable) == "cable-2" 
    print("The mocked value is dynamic")
except AssertionError:
    print(UUID_ERROR_MESSAGE)

# Use an iterator with side_effect
try:
    cable = ElectricComponent("cable", 1)

    # Side effect also can be used with an iterable to loop through it and return values from it
    IdentifierGenerator.generate_uuid = Mock(side_effect=["test_cable", "test_cable_2"])
    cable_uuid = IdentifierGenerator.generate_uuid(cable)
    assert cable_uuid == "test_cable"
    cable_uuid = IdentifierGenerator.generate_uuid(cable)
    assert cable_uuid == "test_cable_2"
except AssertionError:
    print(UUID_ERROR_MESSAGE)