from Pose import Pose
from PoseRepository import PoseRepository
import random
from PoseConfigFileParser import PoseConfigFileParser
from FocusScore import FocusScore


class StyleBase:

  def __init__(self, pose_repository: PoseRepository):
    self._pose_repository = pose_repository
    self._starting_poses = PoseConfigFileParser.create_pose_list_from_json(self._pose_repository.poses,
                                                                           "starting_poses")
    self._warm_up_poses = PoseConfigFileParser.create_pose_list_from_json(self._pose_repository.poses,
                                                                           "warm_up_poses")
    self._cool_down_poses = PoseConfigFileParser.create_pose_list_from_json(self._pose_repository.poses,
                                                                           "cool_down_poses")
    self._meditation_poses = PoseConfigFileParser.create_pose_list_from_json(self._pose_repository.poses,
                                                                           "meditation_poses")

  # Returns a new version of the given pose_list based on user inputs for balances, inversions and injuries.
  @staticmethod
  def get_routine_pose_list(pose_list, has_balances, has_inversions, injuries):
    poses = []
    for pose in pose_list:
      pose_is_incorrect_type = (pose.is_balance and not has_balances) or \
                               (pose.is_inversion and not has_inversions)
      pose_has_injury = any((injury in pose.major_body_parts) or (injury in pose.minor_body_parts)
                            for injury in injuries)

      if not pose_is_incorrect_type and not pose_has_injury:
        poses.append(pose)
    return poses

  # Returns a list of allowed_poses dependent on intensity.
  @staticmethod
  def _get_allowed_poses_for_start( pose_list: [Pose], intensity: int) -> [Pose]:
    allowed_poses = [pose for pose in pose_list if pose.intensity <= intensity]
    return allowed_poses

  # Returns a list of allowed_poses dependent on intensity, excluded_pose and focuses.
  def _get_allowed_poses_for_main_routine(pose_list: [Pose], intensity: int, excluded_pose: Pose,
                                         focus_scores_list: [FocusScore]) -> [Pose]:
    for focus_score in focus_scores_list:
      if focus_score.is_needed:
        allowed_poses = [pose for pose in pose_list if pose.intensity <= intensity and exlcuded_pose.name !=
                         pose.name and (focus_score.focus_body_part in pose.major_body_parts or
                                        focus_score.focus_body_part in pose.minor_body_parts)]
        return allowed_poses

    return [pose for pose in pose_list if pose.intensity <= intensity and excluded_pose.name != pose.name]

  # Returns a list of allowed_poses dependent on intensity and excluded_pose.
  @staticmethod
  def _get_allowed_poses_for_end(pose_list: [Pose], intensity: int, excluded_pose: Pose) -> [Pose]:
    allowed_poses = [pose for pose in pose_list if pose.intensty <= intensity and excluded_pose.name !=
                     pose.name]
    return allowed_poses

  # Returns a random pose from a given list of allowed_poses, otherwise errors if none available.
  def pick_pose(self, pose_list: [Pose], intensity: int, excluded_pose: Pose, focus_scores_list: [FocusScore]) -> \
          Pose:
    if excluded_pose is not None and focus_scores_list is not None:
      allowed_poses = self._get_allowedposes_for_main_routine(pose_list, intensity, excluded_pose
                                                              focus_scores_list)
    elif excluded_pose is not None:
      allowed_poses = self._get_allowed_poses_for_end(pose_list, intensity, excluded_pose)
    else:
      allowed_poses = self._get_allowed_poses_for_start(pose_list, intensity)
    if len(allowed_poses) > 0:
      new_pose = random.choice(allowed_poses)
      return new_pose
    else:
      raise Exception("Error picking pose: no poses available")

  def generate_routine_selection(self, duration: int, pose_list: [Pose], intensity: int, excluded: Pose,
                                 focus_scores_list: [FocusScore]) -> [Pose]:
    generated_routine = []
    generated_length = 0
    excluded_pose = excluded
    while generated_length < duration:
      next_pose = self.pick_pose(pose_list, intensity, excluded_pose, focus_scores_list)
      excluded_pose = next_pose
      generated_routine.append(next_pose)
      generated_length += next_pose.length + self.pose_length_modifier
      for focus_score in focus_scores_list:
        focus_score.update_score(len(generated_routine), next_pose)
    return generated_routine
