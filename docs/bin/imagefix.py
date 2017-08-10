import glob

images = glob.glob("flat/*.pdf") + glob.glob("flat/*.png")

    
# Read in the file
with open('flat/merged.tex', 'r') as file :
  filedata = file.read()


for image in images:
    name = image.replace("flat/", "")
    base, ending = name.split(".")
    print (base, "->", name)
    filedata = filedata.replace(base, name)

# Write the file out again
with open('flat/objects.tex', 'w') as file:
  file.write(filedata)
