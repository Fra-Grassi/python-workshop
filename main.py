from psychopy import visual
from slide_objects import StaticSlide, StaticResponseSlide
import settings
from utils import Results

# Prepare psychopy screen
win = visual.Window(size=(1080, 720),
                    pos=(0, 0),
                    fullscr=False,
                    useRetina=True,
                    screen=1,
                    color=(123, 123, 123),
                    colorSpace='rgb255',
                    units='pix')

# Create blank slide:
empty_slide = StaticSlide(duration=settings.blank_screen_dur, screen=win)

# Prepare stimulus slide:
response_slides = []
for i in range(settings.trial_num):
    this_slide = StaticResponseSlide(duration=settings.stim_dur, screen=win,
                                     stimulus_path=settings.stim_path, stimulus_size=settings.stim_size,
                                     condition="response cond", key_list=["left", "down", "right"])
    response_slides.append(this_slide)

# Test

# Prepare results object:
results = Results()

for n in range(settings.trial_num):
    
    results.updated = False  # Reset flag
    response_slide = response_slides[n]
    # Show slides:
    empty_slide.show_slide()
    response_slide.show_slide()
    
    # Update and save results:
    results.update_results(trial_num=n+1, slide_obj=response_slide)
    print(results.results)
    results.save_results(filepath=settings.results_path)
