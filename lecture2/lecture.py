from client.api.notebook import Notebook
from client.api import assignment
from client.utils import auth

args = assignment.Settings(server='clewolffautook21.eastus.cloudapp.azure.com/okpy')
ok = Notebook('./lecture.ok', args)

# This cell sets the css styles for the rest of the notebook.
# Unless you are particlarly interested in that kind of thing, you can safely ignore it

from IPython.core.display import HTML

def css_styling():
    styles = """<style>
div.exercise {    
    background-color: #e6f0ff;
    border-left: 5px solid #003380;
    padding: 0.5em;
    }
 </style>
"""
    return HTML(styles)
