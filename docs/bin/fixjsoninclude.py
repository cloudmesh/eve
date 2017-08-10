import glob
from pprint import pprint

output = """
\\begin{{figure}}[!h]
\\begin{{verbatim}}
{lines}
\\end{{verbatim}}
\\caption{{{caption}}}
\\end{{figure}}
 """

include = """
{lines}
"""

# Read in the file
with open('objects.tex', 'r') as file :
  lines = file.readlines()

lineno = 0
for line in lines:
  line = line.replace("\n","")      
  lineno = lineno + 1
  if '%' not in line and 'JSONINPUT' in line:
    print (79 * "%")
    print ("%", lineno, line)
    line = line.replace("\JSONINPUT","")
    line = line.replace("}","")
    line = line.replace("{",",")    

    data = {}
    n,  data["kind"], data["filename"], data["caption"], data["label"] = line.split(",")
    data["filename"] = "../cloudmesh/specification/examples/" + data["filename"]

    with open(data["filename"], 'r') as file :
       data["lines"] = file.readlines()

    data["lines"] = ''.join(data["lines"]).strip()
    #pprint (data)    
    print (79 * "%")
    print (output.format(**data))
    print (79 * "%")
  elif '%' not in line and '\input{' in line:
    print (79 * "%")
    print ("%", lineno, line)

    line = line.replace("}","")
    line = line.replace("{",",")    

    data = {}

    n,  data["filename"] = line.split(",")
    data["filename"] = data["filename"] + ".tex"

    
    with open(data["filename"], 'r') as file :
        data["lines"] = file.readlines()
    
    data["lines"] = ''.join(data["lines"]).strip()
    print (79 * "%")
    print (include.format(**data))
    print (79 * "%")
          
      
  else:
      print (line)
      pass
