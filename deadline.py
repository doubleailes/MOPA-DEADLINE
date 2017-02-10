import os, sys
import getpass

# Get the group
# check if username is the same as the deadline name.



class deadlineMopa():
  
  def __init__(self):
    self.user = getpass.getuser().upper()
    render_quality = ['HD_','LD_','TEST_']
    self.params = render_quality
    
  def launchRender(self, qual=0):
    '''
    Launch a render.
    qual is the render mode (HD,LD,TEST)
    '''
    print('Render launched by ' + self.user)
    print('It was launched in ' + self.params[qual])
    print('Render Name => ' + self.params[qual] + self.user)
