def tail(filename):
	with open(filename, "rb") as f:
		# Start at the end of the file
		f.seek(0, 2)
		file_size = f.tell()

		# Track number of newlines found
		newline_count = 0
		buffer = b""

		# Iterate backward until we find the last 3 lines or reach the beginning
		for i in range(file_size - 1, -1, -1):
			f.seek(i)
			char = f.read(1)

			# Check if the character is a newline
			if char == b"\n":
				newline_count += 1
				# If we've found 3 newlines, break out of the loop
				if newline_count == 3:
					break
			# Accumulate characters in reverse order
			buffer = char + buffer

		# Print out the last 3 lines
		print(buffer.decode("utf-8"))


# Usage example
tail("logfile.txt")
