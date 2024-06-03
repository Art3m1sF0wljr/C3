# Get the size of the reference file
ref_file="tx_data.bin"
target_file="rx_data.bin"
size=$(stat -c%s "$ref_file")

# Truncate the target file
dd if="$target_file" of="$target_file.truncated" bs=1 count=$size
