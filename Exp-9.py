#AWGN Exp-9
import numpy as np
import matplotlib.pyplot as plt

#Set the parameters
n_bits = 1000000
SNRdBs = np.arange(-18, 11, 1) SNRs = 10** (SNRdBs/10)

#Generate random bits
bits = np.random.randint(0, 2, n_bits)

#Loop over SNR values
BERs = []
for SNR in SNRs:
    #BPSK modulation
    symbols = 2*bits - 1
    noise_power = 1/SNR
    noise = np.sqrt(noise_power)*np.random.randn(n_bits) received = symbols + noise
    decoded_bits = (received >= 0).astype (int)

    #Calculate the bit error rate
    BER= np.sum(bits != decoded_bits) / n_bits BERs.append(BER)

# Plot the results
plt.semilogy (SNRdBs, BERs)
plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate')
plt.title('Bit Error Rate vs. SNR for BPSK modulation with AMGN')
plt.grid(True)
plt.show()
