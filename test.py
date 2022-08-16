import pandas as pd
import mne

df = pd.read_csv('data/C10_32Ch_48Subjects_al.csv') 

#From the link above - there is more info on how to define channel type etc for info structure
n_channels = list(df.columns)
sampling_freq = 256
info = mne.create_info(n_channels, sfreq=sampling_freq, ch_types='eeg')
raw = mne.io.RawArray(df.values.T, info)

#...preprocessing ...
# raw.save('Data.fif')
# raw.plot(duration=60, proj=False, n_channels=len(raw.ch_names),
#          remove_dc=False)

for cutoff in (0.1, 0.2):
    raw_highpass = raw.copy().filter(l_freq=cutoff, h_freq=None)
    with mne.viz.use_browser_backend('matplotlib'):
        fig = raw_highpass.plot(duration=20, proj=False,
                                n_channels=len(raw.ch_names), remove_dc=False)
    fig.subplots_adjust(top=0.9)
    fig.suptitle('High-pass filtered at {} Hz'.format(cutoff), size='xx-large',
                 weight='bold')

input()



