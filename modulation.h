#ifndef MODULATION_H
#define MODULATION_H

enum MOD_TYPE {
    MOD_ASK,
    MOD_FSK,
    MOD_BPSK
};

void setup_modulator(int fs, int bitrate);
void set_modulation_mode(MOD_TYPE mode);
int generate_modulated_sample();

#endif