import numpy
import scipy.io.wavfile
import matplotlib.pyplot as plt
from scipy.fftpack import dct

sample_rate, signal = scipy.io.wavfile.read('OSR_us_000_0010_8k.wav')  # File assumed to be in the same directory
signal = signal[0:int(3.5 * sample_rate)]  # Keep the first 3.5 seconds
preemphasis = 0.97
   
def pre_emphasize(self, signal):
    # apply pre-emphasis filtering on waveform
    preemph_wav = [np.append(signal[0],signal[1:]-self.preemphasis*signal[:-1])]
    return preemph_wav

plt.plot(pre_emphasize(signal))
plt.show