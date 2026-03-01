import adi
import matplotlib.pyplot as plt
import numpy as np

# 1. Initialize
sdr = adi.Pluto('ip:192.168.2.1')
sdr.sample_rate = int(2.5e6)
sdr.rx_lo = int(800e6) # Target an LTE band for your 'shadow' project
sdr.rx_buffer_size = 1024 # Get a small chunk

# 2. Capture
samples = sdr.rx()

# 3. Plot Time Domain (The raw wave)
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(np.real(samples[:100])) # Plot first 100 Real (I) samples
plt.plot(np.imag(samples[:100])) # Plot first 100 Imaginary (Q) samples
plt.title("Time Domain (I and Q)")

# 4. Plot Frequency Domain (The Spectrum)
plt.subplot(2, 1, 2)
# Calculate Power Spectral Density
plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.rx_lo/1e6)
plt.title("Frequency Domain (Spectrum)")

plt.tight_layout()
plt.show()
