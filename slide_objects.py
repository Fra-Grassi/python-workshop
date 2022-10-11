# Define classes of slides presented in the experiment
from psychopy import core, visual
from psychopy.hardware import keyboard
from display_methods import DispStatic, DispStaticResponse, DispDynamicResponse
import settings
import time


# -----------------------------------------------------------------------------------------------------------------


class StaticSlide:
    """Class for static slide.
    This slide can be empty or show a visual stimulus.
    Slide is displayed for a fixed duration, and no key response is recorded.
    It implements attribute 'display_method', which is an object of class family 'display_methods'.
    Class-specific attribute:
        - condition: [string] experimental condition the stimulus belongs to [default = None]
    Attributes passed to 'display_methods':
        - duration: [int] in seconds
        - screen: [psychopy visual.Window object]
        - stimulus_path: [string] path to image file to display [default = None]
        - stimulus_size: [tuple] W and H of image file to display. Will use units defined in main script [default = None]
    """
    def __init__(self, duration, screen, stimulus_path=None, stimulus_size=None, condition=None):
        self.condition = condition
        self.display_method = DispStatic(duration=duration, screen=screen, stimulus_path=stimulus_path,
                                         stimulus_size=stimulus_size)
        
    def show_slide(self):
        """ Use the method 'show_slide' provided by 'display_method'."""
        self.display_method.show_slide()


class StaticResponseSlide:
    """Class for static slide which detects key presses.
    This slide can be empty or show a visual stimulus.
    Slide is displayed for a fixed duration. Eventual key pressed and reaction time are recorded.
    Class-specific attribute:
        - condition: [string] experimental condition the stimulus belongs to [default = None]
    Attributes passed to 'display_methods':
        - duration: [int] in seconds
        - screen: [psychopy visual.Window object]
        - stimulus_path: [string] path to image file to display [default = None]
        - stimulus_size: [tuple] W and H of image file to display. Will use units defined in main script [default = None]
        - key_list: [list] list of possible keys for response
    """
    def __init__(self, duration, screen, key_list, stimulus_path=None, stimulus_size=None, condition=None):
        self.condition = condition
        self.display_method = DispStaticResponse(duration=duration, screen=screen, stimulus_path=stimulus_path,
                                                 stimulus_size=stimulus_size, key_list=key_list)
        
    def show_slide(self):
        """ Use the method 'show_slide' provided by 'display_method'."""
        self.display_method.show_slide()


class DynamicResponseSlide:
    """Class for dynamic slide which detects key presses.
    This slide can be empty or show a visual stimulus.
    Slide is displayed for a maximum duration or until one of allowed keys is pressed.
     Eventual key pressed and reaction time are recorded.
    Class-specific attribute:
        - condition: [string] experimental condition the stimulus belongs to [default = None]
    Attributes passed to 'display_methods':
        - duration: [int] in seconds
        - screen: [psychopy visual.Window object]
        - stimulus_path: [string] path to image file to display [default = None]
        - stimulus_size: [tuple] W and H of image file to display. Will use units defined in main script [default = None]
        - key_list: [list] list of possible keys for response
    """
    
    def __init__(self, duration, screen, key_list, stimulus_path=None, stimulus_size=None, condition=None):
        self.condition = condition
        self.display_method = DispDynamicResponse(duration=duration, screen=screen, stimulus_path=stimulus_path,
                                                  stimulus_size=stimulus_size, key_list=key_list)
    
    def show_slide(self):
        """ Use the method 'show_slide' provided by 'display_method'."""
        self.display_method.show_slide()
