import datetime
import json
#todo: build method to calculate total duration
#todo: should build its own title
class Workout:
    def __init__(self, id=0, title='', MAP=0.0, total_reps=0, set_recovery=0):
      self.id = id
      self.title = title
      self.MAP = MAP
      self.total_reps = total_reps
      self.set_recovery = set_recovery                  
      self.interval_set = []

    def __str__(self):
      map_percent = "{:.0%}".format(self.MAP)

      str_intervals = ''
      for item in self.interval_set:
        str_intervals += str(item)
        str_intervals += '\r\n'

      return f'Workout: MAP: {map_percent}, Total Reps: {self.total_reps}, Set Recovery: {self.set_recovery}, Interval Sets: {str_intervals}'

    #this seems to work with any class?
    #https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
    def toJSON(self):
      return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



class IntervalSet:
  def __init__(self, rep_count=0, work_duration=0, recovery_duration=0):
    self.rep_count=rep_count
    self.work_duration  = work_duration
    self.recovery_duration = recovery_duration

  def __str__(self):
    return f'IntervalSet: Rep Count:{self.rep_count}, Work Duration: {str(datetime.timedelta(seconds =self.work_duration))}, Recovery Duration:{str(datetime.timedelta(seconds =self.recovery_duration))}'

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


