# Read file .raw and print the output in a human-readable format
import sys
import numpy as np

RAW_FILE = sys.argv[1] if len(sys.argv)>1 else "output_0.raw"
SHAPE = tuple(map(int, sys.argv[2].split(","))) if len(sys.argv)>2 else (1, 1000)

data = np.fromfile(RAW_FILE, dtype=np.float32)
print("Top-5 classes:", data.argsort()[-5:][::-1])
