import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse
from scipy import fftpack
import time  # Import the time library

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename)
fftsize = len(data)
start_time = time.time()  # Start timing before FFT
data_fft = fftpack.fft(data, fftsize)
end_time = time.time()  # End timing after FFT

# Calculate the duration
duration = end_time - start_time
print(f"FFT computation time: {duration:.6f} seconds")

# Plotting the result
plt.figure(figsize=(12, 6))
plt.plot(np.abs(data_fft[:fftsize // 2]))  # Plot magnitude spectrum
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()