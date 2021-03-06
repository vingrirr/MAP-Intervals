
def format_seconds(seconds):
  m, s = divmod(seconds, 60)
  h, m = divmod(m, 60)
  if h>0:
    return (f'{h:d}:{m:02d}:{s:02d}')
  else:
    return (f'{m:02d}:{s:02d}')

#todo: create method to go from hh:mm:ss to seconds
#or mm:ss to seconds

#different ways of formatting: 
#https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds/775075