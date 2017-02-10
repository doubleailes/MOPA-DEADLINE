import os, sys
import getpass

# Get the group
# check if username is the same as the deadline name.



class deadlineMopa():
  
  def __init__(self):
    self.user = getpass.getuser()
    render_quality = ['HD_','LD_','TEST_']
    self.params = [render_quality]
    
  def launchRender(self):
    '''
    Launch a render.
    '''
    print('Render launched by ' + self.user)
    print('It was launched in ' + self.params[0][0])
