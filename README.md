# BER-Analysis-of-Digital-Modulation-Schemes-using-ESP32

## Overview

This project implements and analyzes a digital communication system using multiple modulation schemes — ASK (OOK), FSK, and BPSK — on an ESP32 platform. The system evaluates Bit Error Rate (BER) performance by combining embedded firmware implementation with Python-based signal processing, noise modeling, and visualization.

The project bridges communication theory and practical embedded implementation, enabling empirical BER analysis under noisy conditions.

## Objectives

-> Implement ASK, FSK, and BPSK modulation techniques

-> Capture transmitted and received data using ESP32 ADC

-> Log TX/RX data via serial communication

-> Perform BER analysis using Python

-> Study the effect of noise and detection thresholds

->Visualize signals, bit decisions, and BER trends

## System Architecture

Binary Data 
   → Modulation (ASK / FSK / BPSK)
   → Channel (Noise Model)
   → ADC Sampling
   → Bit Detection
   → Serial Logging (CSV)
   → Python Analysis & Visualization

## Components Used

### Hardware

  ESP32 microcontroller

  ESP32 internal ADC

  External signal source (planned)

### Software

  Arduino IDE (ESP32 firmware)

  Python

    NumPy

    Pandas

    Matplotlib

## Features Implemented

  -> ASK / OOK modulation

  -> Frequency Shift Keying (FSK)

  -> Binary Phase Shift Keying (BPSK)

  -> ADC-based signal acquisition

  -> Threshold-based and coherent bit detection

  -> Serial data logging to CSV

  ### Python-based:

    AWGN noise modeling

    BER computation

    Reproducible simulations

    Multi-plot signal visualization

## Future Scope

-> Integration of real analog signals using a function generator

-> BER evaluation under actual hardware noise

-> Comparison with theoretical BER curves

-> Improved receiver filtering and synchronization

-> Extension to higher-order modulation schemes
