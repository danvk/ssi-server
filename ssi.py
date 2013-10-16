'''
Shared code for ssi_server.py and ssi_expander.py.
'''

import re
import os.path

def InlineIncludes(path, web_path):
  """Read a file, expanding <!-- #include --> statements."""
  def get_include_file_content(x):
    file_to_read =  x.group(2)
    if  len(os.path.dirname(web_path)) >2:
       file_to_read = os.path.join(os.path.dirname(web_path),file_to_read)[1:]
    if os.path.exists(file_to_read):
        return file(file_to_read).read()
    
  content = file(path).read()
  content = re.sub(r'<!-- *#include *(virtual|file)=[\'"]([^\'"]+)[\'"] *-->',
      get_include_file_content,
      content)
  return content

