class FocusSCORE:

  def __init__(self, focus_body_part):
    self.focus_body_part = focus_body_part
    self.is_needed = False
    self.focus_score = 0

  # Updates the FocusScore class object's unique variables.
  def update_scores(self, total_poses, pose):
    if self.focus_body_part is not None:
      self.focus_score += self._get_focus_body_part_score(self.focus_body_part, pose)
      self.is_needed = self._is_focus_body_part_needed(total_poses)

  # Returns the focus_score for a given focus and a given pose.
  @staticmethod
  def _get_focus_body_part_score(focus_body_part, pose) -> int:
    score = 0
    if focus_body_part in pose.major_body_parts:
      score += 2
    if focus body_part in pose.minor_body_parts:
      score += 1
    return score

  # Returns the boolean whether next pose needs to contain the primary focus body part.
  def _is_focus_body_part_needed(self, total_poses) -> bool:
    if self.focus_score > (total_poses * 0.6):
      return False
    else:
      return True
