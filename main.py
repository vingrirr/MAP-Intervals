import pprint
import guidelines as g
import intervalCalculator as c
import duration
import jsonpickle




#todo: how to do import that is global?
#todo: how to write as json? Output interval information too and correct durations

#print('Building workout for:')
#pprint.pprint (g.workout_templates[3])
#workout = c.build_workout(g.workout_templates[3])
#pprint.pprint(workout.toJson())
#print(workout.toJSON())

#print('\r\n')
with open('workouts.txt','w') as f:
  f.write('[')
  for item in g.workout_templates:
    workout = c.build_workout(item)
    #pprint.pprint(workout.__dict__)
    #print('\r\n')
    #jsonStr = json.dumps(workout.__dict__)  
    f.write((workout.toJSON()))
    f.write(',')
    f.write('\r\n')
   # f.write(jsonpickle.encode(workout))
    #f.write(('\r\n\r\n'))

  f.write(']')

workout_list = []
#for item in g.workout_templates:
  #workout = c.build_workout(item)
  #workout_list.append(workout)

#with open('workouts.txt','w') as f:
 # f.write(jsonpickle.encode(workout_list))

#with open('workouts.txt','r') as f:
 # workout_list = jsonpickle.decode(f.read())

#for wrkout in workout_list: 
 # print(str(wrkout))
 # for line in f:
  #  workout = jsonpickle.decode(line)
   # print(str(workout))


print('Done')