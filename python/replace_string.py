with open("recreate-depl.yml", "r") as file:
  content=file.read()
# replace the string
content_new = content.replace('image: adamtravis/rollouts:blue', 'image: adamtravis/rollouts:orange')

# write to the file 

with open("recreate-depl.yml", "w") as file:
  file.write(content_new)
  