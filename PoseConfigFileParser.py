import json
from Pose import Pose


class PoseConfigFilerParser:

  def __innit__(self):
    pass

  @staticmethod
  def _deserialize_poses(poses_from_json) -> [Pose]:
    poses = []
    for pose_from_json in poses_from_json:
      poses.append(Pose(pose_from_json["name"], pose_from_json["major_body_part"],
                        pose_from_json["minor_body_parts"], pose_from_json["length"],
                        pose_from_json["intensity"],
                        pose_from_json["is_balance"], pose_from_json["is_inversion"], None))
    return poses

  @staticmethod
  def _deserialize_counterpose_joins_modifies_poses(counterposes_from_json, poses: [Pose]):
      for pose_pair_from_json in counterposes_from_json:
        pose_1 = next((pose for pose in poses if pose.name == pose_pair_from_json["item_1"]))
        pose_2 = next((pose for pose in poses if pose.name == pose_pair_from_json["item_2"]))

        if pose_1 is not None and pose_2 is not None:
          pose_1.counterpose = pose_2
          pose_2.counterpose = pose_1

  # Returns a list of all poses as Pose class objects.
  def create_poses_from_json(self):
    with open("poses.json") as pose_config_file:
      from_json = json.load(pose_config_file)
      poses = self._deserialize_poses(from_json["poses"])
      self._deserialize_counterpose_joins_modifies_poses(from_json["counterposes"], poses)
    return poses

  @staticmethod
  def create_pose_list_from_json(all_poses: [Pose], list_name: str) -> [Pose]):
    with open("poses.json") as pose_config_file:
      pose_list = []
      from_json = json.load(pose_config_file)
      poses_from_json = from_json[list_name]
      for pose_from_json in poses_from_json:
        for pose in all_poses:
          if poses_from_json["name"] == pose.name:
            pose_list.append(pose)
      return pose_list
      
