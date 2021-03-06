
import pprint
import math
import workout as w
import guidelines
def build_workout(workout_template):
  '''this will build a workout based on a workout template'''
  item = w.Workout()
  
  g = guidelines.get_rep_set(workout_template['total_reps'])

  if g is not None:
    #print('Guideline is: \r\n')
    #pprint.pprint(g)
    #print("\r\n")
    
    #say 17 reps in 3 sets, then 2 sets will need an extra rep
    reps_per_set = math.floor(workout_template['total_reps'] / g['num_sets'])
    #print("reps/set is: "+str(reps_per_set)+"\r\n")

    extra = workout_template['total_reps'] % g['num_sets']    
    #print("Extra is: "+str(extra)+"\r\n")

    item.id = workout_template['Id']
    item.title = '{} x ~{} at {} MAP'.format(g['num_sets'], reps_per_set, workout_template['MAP'])
    item.MAP = workout_template['MAP']
    item.total_reps= workout_template['total_reps']
    item.set_recovery =g['set_recovery']

    #now build out intervals
    #for 0 to g['num_sets'], if we have an extra, add that on and decrement the extra

    for i in range(0,g['num_sets']):
      interval = w.IntervalSet()      
      if extra > 0:
        interval.rep_count = reps_per_set +1
        extra -= 1
      else:
        interval.rep_count = reps_per_set

      interval.work_duration = workout_template['work_duration']
      interval.recovery_duration = g['rep_recovery']

     # print("Adding interval: \r\n")
     # print(interval)
      item.interval_set.append(interval)
  
  return item
  


