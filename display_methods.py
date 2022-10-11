from psychopy import visual, core
from psychopy.hardware import keyboard


class DisplayMethod:
    """Abstract class for displaying slide
    Defines common attributes to all display methods:
        - duration: [int] in seconds
        - screen: [psychopy visual.Window object]
        - stimulus_path: [string] path to image file to display
        - stimulus_size: [tuple] Width and Height of image file to display. Will use units defined in main script
        - clock: psychopy core.Clock object to count time for slide presentation
    Also defines informal interface for method to show slide.
    """
    def __init__(self, duration, screen, stimulus_path, stimulus_size):
        self.duration = duration
        self.screen = screen
        self.stimulus = visual.ImageStim(win=self.screen)  # create empty psychopy visual stimulus object
        if stimulus_path:  # if image path is provided, add path and size to visual stimulus object
            self.stimulus.image = stimulus_path
            self.stimulus.size = stimulus_size
        self.clock = core.Clock()
        
    def show_slide(self):  # TODO: think of maybe changing this name to not being confused with Slide class method
        pass


class DispStatic(DisplayMethod):
    """Class for displaying a static slide, with or without visual stimulus, for a fixed duration.
    No response is recorded.
    """
    def __init__(self, duration, screen, stimulus_path, stimulus_size):
        super().__init__(duration, screen, stimulus_path, stimulus_size)

    def show_slide(self):
        """Overrides informal interface to display slide for a fixed duration."""
        self.clock.reset()
        t = self.clock.getTime()
        while t < self.duration:
            self.stimulus.draw()
            self.screen.flip()
            t = self.clock.getTime()


class DispStaticResponse(DisplayMethod):
    """Class for displaying a static slide, with or without visual stimulus, for a fixed duration.
    Key presses is recorded and stored.
    Implements attributes:
        - key_list: [list] list of possible keys for response
        - response_key: [string] stores eventual key pressed
        - response_rt: [float] stores eventual key press reaction time
        - keyboard: psychopy keyboard.Keyboard object to detect and record key press.
    """
    def __init__(self, duration, screen, stimulus_path, stimulus_size, key_list):
        super().__init__(duration, screen, stimulus_path, stimulus_size)
        self.key_list = key_list
        self.response_key = None
        self.response_rt = None
        self.keyboard = keyboard.Keyboard()
        self.keyboard.clock = self.clock  # assign clock to keyboard object to detect reaction time
        
    def show_slide(self):
        """Overrides informal interface to display slide for a fixed duration.
        If any key in 'key_list' is pressed, key name and reaction time is stored.
        """
        self.keyboard.clearEvents()  # flush eventual previous key presses
        self.clock.reset()
        t = self.clock.getTime()
        while t < self.duration:
            self.stimulus.draw()
            self.screen.flip()
            
            # Check that no key has already been pressed. If not, detect key press among the allowed keys.
            # Store name and reaction time of first key press detected
            if not self.response_key:
                key = self.keyboard.getKeys(self.key_list, clear=True)
                if key:
                    self.response_key = key[0].name
                    self.response_rt = key[0].rt
            
            t = self.clock.getTime()
        

class DispDynamicResponse(DisplayMethod):
    # TODO: this might be child of "DispStaticResponse"!
    """Class for displaying a dynamic slide, with or without visual stimulus.
    Slide is displayed for a maximum duration or until one of allowed keys is pressed.
    Key press is recorded and stored.
    Implements attributes:
        - key_list: [list] list of possible keys for response
        - response_key: [string] stores eventual key pressed
        - response_rt: [float] stores eventual key press reaction time
        - keyboard: psychopy keyboard.Keyboard object to detect and record key press
        """
    def __init__(self, duration, screen, stimulus_path, stimulus_size, key_list):
        super().__init__(duration, screen, stimulus_path, stimulus_size)
        self.key_list = key_list
        self.response_key = None
        self.response_rt = None
        self.keyboard = keyboard.Keyboard()
        self.keyboard.clock = self.clock  # assign clock to keyboard object to detect reaction time
        
    def show_slide(self):
        """Overrides informal interface to display slide until one key is pressed.
        If any key in 'key_list' is pressed, key name and reaction time is stored.
        """
        self.keyboard.clearEvents()  # flush eventual previous key presses
        self.clock.reset()
        t = self.clock.getTime()
        while t < self.duration:
            self.stimulus.draw()
            self.screen.flip()
            
            # Check that no key has already been pressed. If not, detect key press among the allowed keys.
            # Store name and reaction time of first key press detected, and stop displaying slide.
            if not self.response_key:
                key = self.keyboard.getKeys(self.key_list, clear=True)
                if key:
                    self.response_key = key[0].name
                    self.response_rt = key[0].rt
                    break  # in case of key press, stop displaying slide
                    
            t = self.clock.getTime()
