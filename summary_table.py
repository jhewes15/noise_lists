from numpy import loadtxt
from tabulate import tabulate

run = [ [ 2, 0, 9 ], [ 3, 0, 9 ], [ 5, 0, 15 ], [ 28, 0, 10 ], [ 62, 0, 14 ], [ 83, 0, 10 ], [ 84, 0, 16 ], [ 95, 0, 19 ], [ 95, 44, 55 ], [ 95, 67, 76 ], [ 95, 85, 94 ], [ 95, 100, 109 ], [ 95, 120, 132 ], [ 95, 157, 166 ], [ 95, 174, 187 ], [ 95, 198, 207 ], [ 114, 0, 20 ], [ 114, 110, 130 ], [ 114, 275, 295 ], [ 114, 400, 420 ], [ 114, 640, 660 ], [ 114, 755, 775 ], [ 114, 865, 885 ], [ 115, 110, 130 ], [ 115, 220, 240 ], [ 115, 365, 385 ], [ 115, 475, 495 ], [ 115, 620, 640 ], [ 115, 850, 870 ], [ 115, 980, 1000 ], [ 117, 0, 20 ], [ 117, 115, 135 ], [ 119, 0, 20 ], [ 119, 110, 130 ], [ 119, 230, 250 ], [ 119, 350, 370 ], [ 121, 0, 20 ], [ 126, 0, 11 ], [ 128, 0, 14 ], [ 130, 0, 8 ], [ 131, 0, 11 ], [ 131, 14, 25 ], [ 131, 28, 37 ], [ 131, 42, 52 ], [ 131, 55, 67 ], [ 134, 0, 10 ], [ 138, 0, 10 ], [ 138, 15, 24 ], [ 138, 41, 50 ], [ 138, 54, 63 ], [ 138, 69, 78 ], [ 138, 114, 123 ], [ 138, 127, 136 ], [ 139, 13, 22 ], [ 139, 27, 36 ], [ 139, 41, 50 ], [ 139, 54, 63 ], [ 139, 70, 79 ], [ 139, 83, 92 ], [ 139, 96, 105 ], [ 139, 111, 120 ], [ 139, 127, 136 ], [ 139, 140, 149 ], [ 139, 155, 164 ], [ 140, 0, 9 ], [ 140, 13, 22 ], [ 140, 28, 37 ], [ 140, 41, 50 ], [ 140, 55, 64 ], [ 140, 71, 80 ]  ]

for i in run:
  run_name = 'run{:03d}_subrun{:03d}_{:03d}'.format(i[0],i[1],i[2])
  fname = './noise_channels/{}_all.dat'.format(run_name)
  f = open
  test = loadtxt(fname, delimiter=' ')
  if len(test) > 0:
    crate,slot,femch,rms = loadtxt(fname, delimiter=' ', unpack=True)

  if len(crate) == 0: continue

  noise_data = []
  for x in xrange(len(crate)):
    noise_data.append([ crate[x], slot[x], femch[x], rms[x] ])

  outfile = open('summary_tables/{}_all.dat'.format(run_name),'w')

  outfile.write(tabulate(noise_data, headers=["Crate","Slot", "FEM channel", "Mean RMS"]))

for i in run:
  run_name = 'run{:03d}_subrun{:03d}_{:03d}'.format(i[0],i[1],i[2])
  fname = './noise_channels/{}_low.dat'.format(run_name)
  test = loadtxt(fname, delimiter=' ')
  if len(test) > 0:
    crate,slot,femch,rms = loadtxt(fname, delimiter=' ', unpack=True)
  
  if len(crate) == 0: continue
  
  noise_data = []
  for x in xrange(len(crate)):
    noise_data.append([ crate[x], slot[x], femch[x], rms[x] ])

  outfile = open('summary_tables/{}_low.dat'.format(run_name),'w')

  outfile.write(tabulate(noise_data, headers=["Crate","Slot", "FEM channel", "Mean RMS"]))

for i in run:
  run_name = 'run{:03d}_subrun{:03d}_{:03d}'.format(i[0],i[1],i[2])
  fname = './noise_channels/{}_high.dat'.format(run_name)
  test = loadtxt(fname, delimiter=' ')
  if len(test) > 0:
    crate,slot,femch,rms = loadtxt(fname, delimiter=' ', unpack=True)
  
  if len(crate) == 0: continue
  
  noise_data = []
  for x in xrange(len(crate)):
    noise_data.append([ crate[x], slot[x], femch[x], rms[x] ])

  outfile = open('summary_tables/{}_high.dat'.format(run_name),'w')

  outfile.write(tabulate(noise_data, headers=["Crate","Slot", "FEM channel", "Mean RMS"]))