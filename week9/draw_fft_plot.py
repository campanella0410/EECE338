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

# X���� ���ļ���
freqs = np.fft.fftfreq(fftsize, Ts)

# Y���� �Ŀ�. Ǫ���� ��ȯ�� �Ŀ��� ���Ҽ� ũ�� 
power = np.abs(data_fft)**2

#  plot�ϴ� �ڵ� 
plt.figure(figsize=(10, 5))  # ũ�� ���� 
plt.plot(freqs[:fftsize // 2], power[:fftsize // 2])  # ���� ���ļ� �κи� �÷��ϵ��� ������ 
plt.title("FFT of " + args.filename)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.xscale('LOG scale')  # Ǫ���� ��ȯ�� �α� ������
plt.yscale('LOG scale')
plt.grid(True)

############################################

plt.show()
