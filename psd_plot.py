import mne
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# read one sample data
mne_filename_al = "mne_data/C12_32Ch_48Subjects_al_raw_eeg.fif"
raw_al = mne.io.read_raw_fif(mne_filename_al, verbose=False)

mne_filename_fa = "mne_data/C12_32Ch_48Subjects_fa_raw_eeg.fif"
raw_fa = mne.io.read_raw_fif(mne_filename_fa, verbose=False)

picks = ["FP1", "AF3", "F7", "F3", "FP2", "AF4", "F8", "F4"]
raw_al.compute_psd(method="welch", fmin = 0, fmax=40, picks = picks).plot()
plt.title("alert")

raw_fa.compute_psd(method="welch", fmin = 0, fmax=40, picks = picks).plot()
plt.title("fatigue")
plt.show()