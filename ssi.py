'''
Shared code for ssi_server.py and ssi_expander.py.
'''

import re
import os.path

def InlineIncludes(path, web_path):
  """Read a file, expanding <!-- #include --> statements."""
  def get_include_file_content(x):
    file_to_read =  x.group(2)
    recursive_web_path = web_path
    if  len(os.path.dirname(web_path)) >2:
       file_to_read = os.path.join(os.path.dirname(web_path),file_to_read)[1:]
       recursive_web_path = "/%s/" % os.path.dirname(file_to_read)
    if os.path.exists(file_to_read):
      # Recursively process ssi calls in the included file
      return InlineIncludes(file_to_read, recursive_web_path)

  content = open(path).read()
  content = re.sub(r'<!-- *#include *(virtual|file)=[\'"]([^\'"]+)[\'"] *-->',
      get_include_file_content,
      content)
  return content

