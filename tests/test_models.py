# tests/test_models.py
from src.pytemplate.domain.models import TrafficLightState

# eval all possible enumeration values
def test_enum_values():
    assert TrafficLightState.RED.value == "RED"
    assert TrafficLightState.YELLOW.value == "YELLOW"
    assert TrafficLightState.GREEN.value == "GREEN"

# eval all possible enum strings
def test_enum_str_method():
    assert str(TrafficLightState.RED) == "RED"
    assert str(TrafficLightState.YELLOW) == "YELLOW"
    assert str(TrafficLightState.GREEN) == "GREEN"
