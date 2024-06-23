this is attempt for qpsk transmission of binary to transmit data<br>
python3 encode.py #generates tx_data.bin<br>
python3 test_12_QPSK_TRX.py #generates rx_data.bin over the air<br>
python3 decode.py #generates reconstructed_leena.png<br>
<br>
dump.temp is the rx hexdump<br>
dump0.temp is tx hexdump<br>
<br>
issues with the header of the transmitted data<br>
<br>
edit:fixed issues, now is works as intending XD<br>
