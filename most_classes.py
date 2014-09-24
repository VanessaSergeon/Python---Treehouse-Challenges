# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewher
# too!
#
# Your code goes below here.

def most_classes(dict):
  most = 0
  the_most = 'me'
  for key in dict:
    count = 0;
    for value in dict[key]:
      count = count + 1
    if count > most:
      most = count
      the_most = key
  print the_most