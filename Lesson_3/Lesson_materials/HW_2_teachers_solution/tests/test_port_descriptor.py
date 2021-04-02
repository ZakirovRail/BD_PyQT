import pytest
# from BD_PyQT.Lesson_3.Lesson_materials.port_descriptor import Port
# from Lesson_3.Lesson_materials.port_descriptor import Port
# from Lesson_materials.port_descriptor import Port
from Lesson_3.Lesson_materials.HW_2_teachers_solution.port_descriptor import Port
# from port_descriptor import Port


class ServerSocket:
    port = Port(default=7777)

def test_default():
    sut = ServerSocket()
    assert sut.port == 7777

def test_set():
    sut = ServerSocket()
    sut.port = 1234
    assert sut.port == 1234

test_data = [
        (0, ValueError),
        (65366, ValueError),
        ("foo", TypeError),
        (10.5, TypeError),
        (object(), TypeError),
    ]

@pytest.mark.parametrize("value, expected_exc", test_data)
def test_set_invaid_value_raises(value, expected_exc):
    sut = ServerSocket()
    with pytest.raises(expected_exc):
        sut.port = value

def test_multi_use_store_different_values():
    class SUT:
        port1 = Port(default=7777)
        port2 = Port(default=7777)
    sut = SUT()
    sut.port1 = 100
    sut.port2 = 200

    assert sut.port1 == 100
    assert sut.port2 == 200

def test_multi_instances_store_different_values():
    sut1 = ServerSocket()
    sut2 = ServerSocket()

    sut1.port = 100
    sut2.port = 200

    assert sut1.port == 100
    assert sut2.port == 200

@pytest.mark.parametrize("value, expected_exc", test_data)
def test_invalid_default_value_raises(value, expected_exc):
    with pytest.raises(expected_exc):

        class SUT:
            port = Port(default=value)
