import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------- LOAD DATA --------
df = pd.read_csv("esp32_log.csv")

tx_bits = df["TX_Bit"].values
tx_samples = df["TX_Sample"].values

# -------- AWGN PARAMETERS --------
SNR_dB = 8        # 🔁 Change this (e.g., 2, 5, 10) to see BER variation

signal_power = np.mean(tx_samples**2)
SNR_linear = 10**(SNR_dB / 10)
noise_power = signal_power / SNR_linear

noise = np.sqrt(noise_power) * np.random.randn(len(tx_samples))

# Add noise
rx_samples = tx_samples + noise

# -------- BIT DECISION --------
# For ASK / OOK (threshold detector)
threshold = 0.5 * np.max(tx_samples)
rx_bits = (rx_samples > threshold).astype(int)

# -------- ERROR & BER --------
errors = (tx_bits != rx_bits).astype(int)
ber = np.cumsum(errors) / np.arange(1, len(errors) + 1)

x = np.arange(len(tx_bits))

# -------- PLOTTING --------
plt.figure(figsize=(12, 10))

# 1️⃣ TX Signal
plt.subplot(5, 1, 1)
plt.plot(tx_samples)
plt.title("TX Modulated Signal")
plt.ylabel("Amplitude")

# 2️⃣ RX Signal (With AWGN)
plt.subplot(5, 1, 2)
plt.plot(rx_samples)
plt.title(f"RX Signal with AWGN (SNR = {SNR_dB} dB)")
plt.ylabel("Amplitude")

# 3️⃣ TX vs RX Bits
plt.subplot(5, 1, 3)
plt.step(x, tx_bits, where="post", label="TX")
plt.step(x, rx_bits, where="post", label="RX")
plt.ylabel("Bit")
plt.legend()
plt.ylim(-0.2, 1.2)

# 4️⃣ Bit Errors
plt.subplot(5, 1, 4)
plt.step(x, errors, where="post")
plt.title("Bit Errors")
plt.ylabel("Error")
plt.ylim(-0.2, 1.2)

# 5️⃣ BER
plt.subplot(5, 1, 5)
plt.plot(ber)
plt.title("BER")
plt.ylabel("BER")
plt.xlabel("Bit Index")
plt.ylim(0, 1)

plt.tight_layout()
plt.show()