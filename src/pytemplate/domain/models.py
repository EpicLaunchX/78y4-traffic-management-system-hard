# domain/models.py
from enum import Enum

# controls traffic light state
class TrafficLightState(Enum);
  RED = "RED"
  GREEN = "GREEN"
  YELLOW = "YELLOW"

  def __str__(self):
    return self.value
