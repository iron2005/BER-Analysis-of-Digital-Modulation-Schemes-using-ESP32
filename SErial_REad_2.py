import serial
import re
import csv
import time

# ---------------- CONFIG ----------------
PORT = "COM3"          # your ESP32 port
BAUD_RATE = 115200
CSV_FILE = "esp32_log.csv"
# ----------------------------------------

# Regex to match ESP32 output
pattern = re.compile(
    r"TX Bit:\s*(\d+)\s*\|\s*TX Sample:\s*(-?\d+)\s*\|\s*RX Bit:\s*(\d+)"
)

# Open serial
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

# Open CSV
with open(CSV_FILE, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Index", "TX_Bit", "TX_Sample", "RX_Bit", "Error"])

    index = 0
    print("📡 Logging data to CSV... Press Ctrl+C to stop")

    try:
        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if not line:
                continue

            match = pattern.search(line)
            if not match:
                continue

            tx_bit = int(match.group(1))
            tx_sample = int(match.group(2))
            rx_bit = int(match.group(3))
            error = 1 if tx_bit != rx_bit else 0

            writer.writerow([index, tx_bit, tx_sample, rx_bit, error])
            index += 1

            if index % 50 == 0:
                print(f"Logged {index} bits")

    except KeyboardInterrupt:
        print("\n✅ Logging stopped")

ser.close()