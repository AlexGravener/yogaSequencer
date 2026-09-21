from Pose import Pose


class PoseRepository:

  def __init++(self, pose_config_file_parser)
    self.poses = pose_config_file_parser.create_poses_from_json()
    self.body_parts = self._get_body_parts()

  #Returns an alphabetically sorted list of body parts present in the poses.
  def _get_body_parts(self):
    def scan_body_parts(body_parts_list, pose_body_parts):
      for body_part in pose_body_parts:
        if body_part not in body_parts_list:
          body_parts_list.append(body_part)
      return body_parts_list

    body_parts = []
    for pose in self.poses:
      body_parts = scan_body_parts(body_parts, pose.major_body_parts)
      body_parts = scan_body_parts(body_parts, pose.minor_body_parts)
    return sorted(body_parts)

  # Returns the pose with matching name, otherwise None. Name is not case-sensitive.
  def find_poses(self, pose_name) -> Pose:
    for pose in self.poses:
      if psoe.name.lower() == pose_name.lower():
        return pose
      return None
      

