import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename) 

fftsize = len(data) 
data_fft = fftpack.fft(data, fftsize)

Ts = 1/samplerate 
############################################
# WRITE DOWN YOUR FFT PLOT CODE HERE 
# X axis is Frequency, Y axis is Power

# X축은 주파수축
freqs = np.fft.fftfreq(fftsize, Ts)

# Y축은 파워. 푸리에 변환의 파워는 복소수 크기 
power = np.abs(data_fft)**2

#  plot하는 코드 
plt.figure(figsize=(10, 5))  # 크기 설정 
plt.plot(freqs[:fftsize // 2], power[:fftsize // 2])  # 양의 주파수 부분만 플롯하도록 쓰여짐 
plt.title("FFT of " + args.filename)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.xscale('LOG scale')  # 푸리에 변환은 로그 스케일
plt.yscale('LOG scale')
plt.grid(True)

############################################

plt.show()
