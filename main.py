from PoseRepository import PoseRepository
from PoseConfigFileParser import PoseConfigFileParse
# from StyleRepository import StyleRepository
from StyleBase import StyleBase
from StyleYin import StyleYin
from StyleVinyasa import StylVinyasa
from StylePower import StylePower
from Controller import Controller
from UI import UI
from UIHelper import UIHelper

pose_config_file_parser = PoseConfigFileParser()
pose_repository = PoseRepository(pose_config_file_parser)
controller = Controller(pose_repository)
ui_helper = UIHelper()
ui = UI(controller, ui_helper)

ui.print_routine(ui,create_routine())
 