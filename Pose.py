from __future__ import annotations


class Pose:

  def __innit__(self, name: str, major_body_parts: [str], minor_body_parts: [str], length: int, intensity: int,
                is_balance: bool, is_inversion: bool, counterpose):
    self.name = name
    self.major_body_parts = major_body_parts
    self.minor_body_parts = minor_body_parts
    self.length = length
    self.intensity = intensity
    self.is_balance = is_balance
    self.is_inversion = is_inversion
    self.counterpose = counterpose

  # Returns the pose's counterpose if it has one, otherwise None.
  def get_counterpose(self) -> Pose:
    if self.counterpose:
      return self.counterpose
    else:
      return None
