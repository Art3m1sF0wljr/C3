this is attempt for qpsk transmission of binary to transmit data
python3 encode.py #generates tx_data.bin
python3 test_12_QPSK_TRX.py #generates rx_data.bin over the air
python3 decode.py #generates reconstructed_leena.png

dump.temp is the rx hexdump
dump0.temp is tx hexdump

issues with the header of the transmitted data
