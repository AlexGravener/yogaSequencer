from PoseReporistory import PoseRepository
from StyleYin importStyleYin
from StyleVinyasa import StyleVinyasa
from StylePower import StylePower
from RoutineParameters import RoutinePrameters
from Pose import Pose

class Controller:

    def __init__(self, pose_repository: PoseRepository):
        self.pose_repository = pose_repository
    
    # Returns the Style class object corresponding to the user's chosen style, otherwise errors.
    def initiate_style(self, style_input):
        if style_input.lower() == "yin":
            return StyleYin(self.pose_repository)
        elif style_input.lower() == "vinyasa":
            return StyleVinyasa(self.pose_repository)
        elif style_input.lower() == "power":
            return StylePower(self.pose_repository)
        else:
            raise ValueError("Style type not found")
        
    # Returns a list of Pose class objects from the user's chosen Style.generate_routine()
    @staticmethod
    def get_routine(routine_parameters: RoutineParameters) -> [Pose]:
        return routine_parameters.user_style.generate_routine(routine_parameters)
    