from Controller import Controller
from UIHelper import UIHelper
from StyleBase import StyleBase
from RoutineParameters import RoutineParameters


class UI:
    def __init__(self, controller: Controller, ui_helper: UIHelper):
        self._controller = controller
        self._ui_helper = ui_helper
        self._start_up()

    # Prints a welcome and introductory message when the programme starts.
    def _start_up(self):
        self._ui_helper.print_function("Welcome to Yoga Routine Generator!\n"
                                       "We offer three styles of yoga:\n" \
                                       "- Yin is a restorative practice where poses are held for longer\n" \
                                       "- Vinyasa is a classic yoga flow\n" \
                                       "- Power is a strong, dynamic practice for building strength and balance")
        self._ui_helper.input_function("Press enter to begin")

    # Returns the boolean whether the user wants to give all inputs possible, or just those necessary.
    def _get_is_quick_start(self):
        while True:
            quick_start_input = self._ui_helper.input_function("Would you like to do a quick-start routine (Q) or a full-setup routine (F)? ")
            if "q" in quick_start_input.lower():
                return True
            elif "f" in quick_start_input.lower():
                return False
            else:
                self._ui_helper.print_function("Sorry, I didn't understand that - I was expecting a 'Q' or an 'F'")

    # Returns a Style class object corresponding to the user's chosen style.
    def _get_style(self) -> StyleBase:
        while True:
            style_input = self._ui_helper.input_function("Which style of yoga would you like to practise today?\n")
            try:
                return self._controller.initiate_style(style_input)
            except ValueError:
                self._ui_helper.print_function("Sorry, I didn't quite catch that - the styles we offer are yin, vinyasa and power")

    # Returns a float value of the number of seconds the user wants to practise for.
    def _get_duration(self) -> float:
        while True:
            try:
                duration = 60 * float(self._ui_helper.input_function(
                    "How many minutes would you liike to practise for? "))
                if duration > 7200:
                    self._ui_helper.print_function("Sorry, 2 hours is the maximum duration we offer")
                elif duration < 120:
                    self._ui_helper.print_function("Sorry, 2 minutes is the minimum duration we offer")
                else:
                    return duration
            except ValueError:
                self._ui_helper.print_function("Please enter a number")

    # Returns an int from 1-5 inclusive corresponding to the user's chosen intensity.
    def _get_intensity(self) -> int:
        while True:
            try:
                intensity = int(self._ui_helper.input_function("On a scale from 1-5 (low-high), how intense would you like your routine to be?"))
                if 0 < intensity < 6:
                    return intensity
                else:
                    self._ui_helper.print_function("Please choose a value from 1 to 5")
            except ValueError:
                self._ui_helper.print_function("Please enter a whole number")
        
    # Returns the boolean whether the user wants to include balancing poses.
    def _get_has_balances(self) -> bool:
        while True:
            balances_input = self._ui_helper.input_function("Would you like to include balancing poses in your routine? ")
            if "y" in balances_input:
                return True
            elif "n" in balances_input:
                return False
            else:
                self._ui_helper.print_function("Sorry, I didn't quite catch that - I was expecting a yes or a no")

    # Returns the boolean whether the user wants to include inversion poses.
    def _get_has_inversions(self) -> bool:
        while True:
            inversions_input = self._ui_helper.input_function("Would you like to include inversion poses in your routine? ")
            if "y" in inversions_input:
                return True
            elif "n" in inversions_input:
                return False
            else:
                self._ui_helper.print_function("Sorry, I didn't quite catch that - I was expecting a yes or a no")

    # Returns the boolean whether the user wants to finish with a meditation pose.
    def _get_has_meditation(self) -> bool:
        while True:
            meditation_input = self._ui_helper.input_function("Would you like to include a meditation at the end of your routine? ")
            if "y" in meditation_input:
                return True
            elif "n" in meditation_input:
                return False
            else:
                self._ui_helper.print_function("Sorry, I didn't quite catch that - I was expecting a yes or a no")

    # Returns a list of injured body parts, chosen by the user.
    def _get_injuries(self) -> [str]:
        injuries = []
        body_parts = "| "
        for body_part in self._controller.pose_repository.body_parts:
            body_parts += body_part + " | "

        while True:
            has_injuries = self._ui_helper.input_function("Do you have any injuries to be considered? ")
            if "y" in has_injuries.lower():
                self._ui_helper.print_function(body_parts)
                while True:
                    injuries_input = self._ui_helper.input_function("Which body part is injured? ")
                    if injuries_input in self._controller.pose_repository.body_parts:
                        injuries.append(injuries_input)
                        while True:
                            has_injuries = self._ui_helper.input_function("Do you have any other injuries to be considered? ")
                            if "y" in has_injuries.lower():
                                while True:
                                    injuries_input = self._ui_helper.input_function("Which body part is injured? ")
                                    if injuries_input in self._controller.pose_repository.body_parts:
                                        injuries.append(injuries_input)
                                        break
                                else:
                                    self._ui_helper.print_function("Sorry, I didn't quite catch that; please select a body part from the list above")
                            elif "n" in has_injuries.lower():
                                return injuries
                            else:
                                self._ui_helper.print_function("Sorry, I didn't quite catch that - I was expecting a yes or a no")
                    else:
                        self._ui_helper.print_function("Sorry, I didn't quite catch that; please select a body part from the list above")
            elif "n" in has_injuries.lower():
                return injuries
            else:
                self._ui_helper.print_function("Sorry, I didn't quite catch that - I was expecting a yes or a no")
            
    # Returns a list of up to two body parts to focus on, chosen by the user; cannot be injured body parts.
    def _get_focuses(self, injuries) -> [str]:
        focuses = []
        non_injuries = [body_part for body_part in self._controller.pose_repository.body_parts if body_part not in injuries]
        body_parts = "| "
        for body_part in non_injuries:
            body_parts += body_part + " | "

        while True:
            has_focuses = self._ui_helper.input_function("Are there any body parts you want to focus on? ")
            if "y" in has_focuses.lower():
                self._ui_helper.print_function(body_parts)
                while True:
                    focuses_input = self._ui_helper.input_function("Which body part would you like to focus on? ")
                    if focuses_input in non_injuries:
                        focuses.append(focuses_input)
                        while True:
                            has_focuses = self._ui_helper.input_function("Do you want a secondary focus? ")
                            if "y" in has_focuses.lower():
                                while True:
                                    focuses_input = self._ui_helper.input_function("Which body part is that? ")
                                    if focuses_input in non_injuries:
                                        focuses.append(focuses_input)
                                        return focuses
                                    else:
                                        self._ui_helper.print_function("Sorry, I didn't quite catch that; please select a body part from the list above")
                            elif "n" in has_focuses.lower():
                                return focuses
                            else:
                                self._ui_helper.print_function("Sorry, I didn't quite catch that - I was expecting a yes or a no")
                    else:
                        self._ui_helper.print_function("Sorry, I didn't qutie catch that; please select a body part from the list above")
            elif "n" in has_focuses.lower():
                return focuses
            else:
                self._ui_helper.print_function("Sorry, I didn't quite catch that - I was expecting a yes or a no")

    # Returns a RoutineParameters class object, dependent on is_quick_start for which inputs to get from user and which to use defaults.
    def get_inputs(self) -> RoutineParameters:
        try:
            is_quick_start = self._get_is_quick_start()
            user_style = self._get_style()
            duration = self._get_duration()
            intensity = self._get_intensity()
            if is_quick_start is True:
                has_balances = True
                has_inversions = True
                has_meditation = False
                injuries = []
                focuses = []
            elif is_quick_start is False:
                has_balances = self._get_has_balances()
                has_inversions = self._get_has_inversions()
                has_meditation = self._get_has_meditation()
                injuries = self._get_injuries()
                focuses = self._get_focuses()
        except ValueError:
            self._ui_helper.print_function("Error: no quick-start input given.")
        
        return RoutineParameters(user_style, duration, intensity, has_balances, has_inversions, has_meditation, injuries, focuses)
    
    # Returns a list of pose objects.
    def create_routine(self):
        return self._controller.get_routine(self.get_inputs())
    
    # Prints the name of each pose in the routine list of poses.
    def print_routine(self, routine):
        self._ui_helper.print_function("\nLet's begin")
        for pose in routine:
            self._ui_helper.print_function(pose.name)
            