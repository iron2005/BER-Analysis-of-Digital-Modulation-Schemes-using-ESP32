#include "modulation.h"

static MOD_TYPE current_mode = MOD_BPSK;

static int fs = 10000;          // Sampling frequency
static int samples_per_bit = 100;
static int sample_count = 0;
static int bit = 1;

void setup_modulator(int sampling_rate, int bitrate) {
    fs = sampling_rate;
    samples_per_bit = fs / bitrate;
}

void set_modulation_mode(MOD_TYPE mode) {
    current_mode = mode;
    sample_count = 0;
}

int generate_modulated_sample() {
    sample_count++;

    // Toggle bit every bit period
    if (sample_count % samples_per_bit == 0) {
        bit = !bit;
    }

    switch (current_mode) {

        case MOD_ASK:
            return bit ? 255 : 0;

        case MOD_FSK:
            // Two different frequencies (simulated)
            return (sample_count % (bit ? 20 : 10)) < 5 ? 255 : 0;

        case MOD_BPSK:
        default:
            return bit ? 255 : -255;
    }
}