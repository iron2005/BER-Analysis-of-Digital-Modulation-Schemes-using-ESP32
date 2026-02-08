#include "demodulation.h"

enum MOD_TYPE { MOD_ASK, MOD_FSK, MOD_BPSK };
MOD_TYPE currentMode = MOD_BPSK;

const int SYMBOL_DELAY_MS = 300;
const int ASK_HIGH = 255;
const int ASK_LOW  = 0;
const int BPSK_POS = 127;
const int BPSK_NEG = -127;

uint8_t txBit;
int txSample;
int rxBit;

void setup() {
    Serial.begin(115200);
    delay(1500);
    randomSeed(esp_random());
    printMenu();
}

void loop() {

    if (Serial.available()) {
        char cmd = Serial.read();

        if (cmd == 'A' || cmd == 'a') currentMode = MOD_ASK;
        else if (cmd == 'F' || cmd == 'f') currentMode = MOD_FSK;
        else if (cmd == 'P' || cmd == 'p') currentMode = MOD_BPSK;

        printMenu();
    }

    txBit = random(0, 2);

    switch (currentMode) {
        case MOD_ASK:
            txSample = txBit ? ASK_HIGH : ASK_LOW;
            break;

        case MOD_FSK:
            txSample = (txBit)
                      ? (millis() % 200 < 100 ? 255 : 0)
                      : (millis() % 100 < 50  ? 255 : 0);
            break;

        case MOD_BPSK:
        default:
            txSample = txBit ? BPSK_POS : BPSK_NEG;
            break;
    }

    rxBit = demodulate(txSample);

    Serial.print("TX Bit: ");
    Serial.print(txBit);
    Serial.print(" | TX Sample: ");
    Serial.print(txSample);
    Serial.print(" | RX Bit: ");
    Serial.println(rxBit);

    delay(SYMBOL_DELAY_MS);
}

void printMenu() {
    Serial.println("\n=== Select Modulation Mode ===");
    Serial.println("A - ASK");
    Serial.println("F - FSK");
    Serial.println("P - BPSK");
    Serial.println("==============================");
}