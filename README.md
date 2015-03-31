# noise_lists

## Dependencies
* numpy
* pandas
* root_numpy
* tabulate

## Load tool
```
python list_maker.py
python summary_table.py
```

## Make list files
Noise files need to be rsync'd/symlinked into this directory, in
the folder noise_files.

At the moment these scripts rely on a janky list of runs & subruns
that needs to be edited by hand. Happy to implement a better
solution if people want it.

First off, the script loops over all root files and averages RMS. It
makes cuts equivalent to 6ADC for high noise and 0.5ADC for low noise,
normalised to gain.

Though the high & low noise cuts are normalised to gain, the output
to text files is raw ADC (this wasn't always the case, so beware
older output files).

First you need to generate text files into noise_channels directory:
```
python list_maker.py
```

## Make summary tables
Second script takes the raw text files and converts them into summary
tables which are easier to read by eye. For this you just need to do:
```
python summary_table.py
```

