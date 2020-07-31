"""
Each age group is 2 years
To get from one age group down to the next, you have to minus 3
because an age group is 2 years inclusive
"""


def get_age_group(age):
  """Get age group

  Done by continuously reducing age and going to previous age group
  and counting how many times this is done

  Note that since arrays start with 0, to get the human-readable age
  group, add 1
  """

  group = 0
  while (age >= 22):
    group += 1
    age -= 3

  return group
