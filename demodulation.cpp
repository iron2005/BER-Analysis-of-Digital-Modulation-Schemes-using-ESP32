#include "demodulation.h"

void setup_demodulator() {
    // Nothing needed for now
}

int demodulate(int sample) {
    return (sample > 0) ? 1 : 0;
}