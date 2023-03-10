import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter


load_path = r'C:\Users\user\PycharmProjects\pythonProject3\heartsound_sig.csv'

# Load CSV file
data = np.loadtxt(load_path, delimiter=',', encoding='utf-8', skiprows=1)


# Print data
# for i in range(0, 1000):
#     print(data[i])

# Moving Average filter
def moving_average_filter(window_size):
    outp = np.array([])
    for i in range(0, len(data)):

        outp = np.append(outp, sum(data[i:i+window_size]) / window_size)

    return outp


# Band-pass filter_Butterworth
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(outp, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, outp)
    return y


# outp = moving_average_filter(100)
# filtered_data = butter_bandpass_filter(outpv, 400, 600, 48000, 1)
filtered_data = butter_bandpass_filter(data, 400, 600, 48000, 3)

# Graph
plt.plot(filtered_data)

plt.title('Heart Sound Signal')
plt.xlabel('Sample number')
plt.ylabel('Signal Value')


plt.show()


