# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

#---------------------------------------------------------------------------------
def farm_action(weather,time_of_day,cow_milking_status,location_of_cows,season,slurry_tank,grass_status):
#---------------------------------------------------------------------------------
  action = ''

  extra_line = False
  if (action == 'milk cows\n') or (action == 'fertilize pasture\n') or (action == 'mow grass\n'):
     cows_moved = False if location_of_cows == 'pasture' else True
     extra_line = True
     location_of_cows == 'cowshed'
     
# action = cows to cowshed
# This needs to be done when one or more of the following statements are true:
#   The cows are on the pasture at night
#   The cows are standing in the rain

  if ((location_of_cows == 'pasture') and (time_of_day == 'night')) and (weather == 'rainy'):
     action = 'take cows to cowshed\n'

# action = milk cows
# This needs to be done when the cows require milking, but is only possible when:
#   The cows are in the cowshed

  if ((cow_milking_status == True) and (location_of_cows == 'cowshed')) or cows_moved == True:
    if action == '': action = 'milk cows\n'

# action = fertilize pasture
# This needs to be done when the slurry tank is full, but is only possible when:
#   The cows are in the cowshed
#   The weather is not sunny or windy

  if slurry_tank == True:
    if location_of_cows == 'cowshed':
      if (weather == 'rainy') or (weather == 'neutral'):
        if action == '': action = 'fertilize pasture\n'
      
# action = mow grass
# This needs to be done when all of the following are true:
#   The grass is long
#   It's spring
#   The weather is sunny
# But is only possible when:
#   The cows are not on the pasture

  if location_of_cows == 'cowshed':
    if (grass_status == True) and (season == 'spring') and (weather == 'sunny'):
      if action == '': action = 'mow grass\n'

# action = wait
# This is done when no other action applies.

  if action == '':
    action = 'wait\n'
    
# multiple actions when:
# (1) cows can be milked, 
# (2) the land can be fertilized
# (3) the grass can be mown
# AND the cows are in the pasture 
# we need to add an action before and after our "main" action. 
# The action before is take cows to cowshed, 
# the action after is take cows back to pasture. 
# But be careful: if the cows were already in the cowshed, 
# they should not be taken back to the pasture.

  if extra_line == True:
    action = 'take cows to cowshed\n' + action
    if cows_moved == True:
        action = action + 'take cows back to pasture\n'

# Remove newline if end of action

  if action[-1:] == '\n':
    action = action[0:-1]

  return action

#---------------------------------------------------------------------------------

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))

