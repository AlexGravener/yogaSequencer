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
      
