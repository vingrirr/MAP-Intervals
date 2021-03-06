rep_set_lookup=[{
 'min_reps':24,
 'max_reps':30,
 'num_sets':4,
 'rep_recovery':60,
 'set_recovery':180
},
{
 'min_reps':14,
 'max_reps':23,
 'num_sets':3,
 'rep_recovery':120,
 'set_recovery':300
},
{
 'min_reps':8,
 'max_reps':13,
 'num_sets':2,
 'rep_recovery':180,
 'set_recovery':600
},
{
 'min_reps':3,
 'max_reps':7,
 'num_sets':1,
 'rep_recovery':300,
 'set_recovery':0
}
]

def get_rep_set(total_reps):  
  result = None
  for i in range(0,len(rep_set_lookup)):
    # same as min reps <= total_reps < max reps, so +7
    if total_reps in range(int(rep_set_lookup[i]['min_reps']),int(rep_set_lookup[i]['max_reps'])+1):
      result = rep_set_lookup[i]
      break
  
  return result



#there's a pattern here,
#see if other templates make sense that aren't in the paper?
workout_templates=[{
 'Id':1,
 'MAP':1.10,
 'total_reps':22,
 'work_duration':30
},
{
 'Id':2,
 'MAP':1.10,
 'total_reps':8,
 'work_duration':60
},
{
 'Id':3,
 'MAP':1.10,
 'total_reps':4,
 'work_duration':90
},
{
 'Id':4,
 'MAP':1.05,
 'total_reps':30,
 'work_duration':30  
},
{
 'Id':5,
 'MAP':1.05,
 'total_reps':12,
 'work_duration':60
},
{
 'Id':6,
 'MAP':1.05,
 'total_reps':7,
 'work_duration':90 
},
{
 'Id':7,
 'MAP':1.05,
 'total_reps':4,
 'work_duration':120
},
{
 'Id':8,
 'MAP':1.00,
 'total_reps':18,
 'work_duration':60 
},
{
 'Id':9,
 'MAP':1.00,
 'total_reps':10,
 'work_duration':90 
},
{
 'Id':10,
 'MAP':1.00,
 'total_reps':6,
 'work_duration':120 
},
{
 'Id':11,
 'MAP':1.00,
 'total_reps':4,
 'work_duration':150 
},
{
 'Id':12,
 'MAP':0.95,
 'total_reps':24,
 'work_duration':60 
},
{
 'Id':13,
 'MAP':0.95,
 'total_reps':14,
 'work_duration':90 
},
{
 'Id':14,
 'MAP':0.95,
 'total_reps':9,
 'work_duration':120 
},
{
 'Id':15,
 'MAP':0.95,
 'total_reps':7,
 'work_duration':150 
},
{
 'Id':16,
 'MAP':0.95,
 'total_reps':5,
 'work_duration':180 
},
{
 'Id':17,
 'MAP':0.95,
 'total_reps':3,
 'work_duration':210
},
{
 'Id':18,
 'MAP':0.90,
 'total_reps':20,
 'work_duration':90 
},
{
 'Id':19,
 'MAP':0.90,
 'total_reps':14,
 'work_duration':120 
},
{
 'Id':20,
 'MAP':0.90,
 'total_reps':10,
 'work_duration':150 
},
{
 'Id':21,
 'MAP':0.90,
 'total_reps':8,
 'work_duration':180 
},
{
 'Id':22,
 'MAP':0.90,
 'total_reps':6,
 'work_duration':210 
},
{
 'Id':23,
 'MAP':0.90,
 'total_reps':4,
 'work_duration':240 
},
{
 'Id':24,
 'MAP':0.90,
 'total_reps':3,
 'work_duration':270 
},
{
 'Id':25,
 'MAP':0.85,
 'total_reps':30,
 'work_duration':90
},
{
 'Id':26,
 'MAP':0.85,
 'total_reps':22,
 'work_duration':120 
},
{
 'Id':27,
 'MAP':0.85,
 'total_reps':16,
 'work_duration':150 
},
{
 'Id':28,
 'MAP':0.85,
 'total_reps':13,
 'work_duration':180 
},
{
 'Id':29,
 'MAP':0.85,
 'total_reps':10,
 'work_duration':210 
},
{
 'Id':30,
 'MAP':0.85,
 'total_reps':8,
 'work_duration':240 
},
{
 'Id':31,
 'MAP':0.85,
 'total_reps':7,
 'work_duration':270 
},
{
 'Id':32,
 'MAP':0.85,
 'total_reps':6,
 'work_duration':300 
},
{
 'Id':33,
 'MAP':0.85,
 'total_reps':5,
 'work_duration':330
},
{
 'Id':34,
 'MAP':0.85,
 'total_reps':4,
 'work_duration':360 
},
{
 'Id':35,
 'MAP':0.85,
 'total_reps':3,
 'work_duration':390 
},
]