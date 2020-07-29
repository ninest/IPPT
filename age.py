first_age_map = {
    "min": 0,
    "max": 21,
    "group": 1
}


age_map = {
  1: first_age_map
}
for i in range(1, 14):
  previous_age_map = age_map[i]

  # create next age group by adding 2 years to the current age interval
  current_age_min = previous_age_map["max"] + 1
  current_age_max = current_age_min + 2
  current_age_group = previous_age_map["group"] + 1

  current_age_map = {
      "min": current_age_min,
      "max": current_age_max,
      "group": current_age_group
  }

  age_map[current_age_group] = current_age_map



def get_age_group(age):
  # search in all age maps to see if the provided age is between the min and max
  for age_group, age_dict in age_map.items():
    if age_dict["min"] <= age <= age_dict["max"]:
      return age_group
