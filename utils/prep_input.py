# prep_inputs.py
import sys, numpy as np
from PIL import Image

IMG = sys.argv[1] if len(sys.argv)>1 else "cat.jpg"
OUT_DIR = sys.argv[2] if len(sys.argv)>2 else "."

W = H = 224
mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
std  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

img = Image.open(IMG).convert("RGB").resize((W, H))
arr = (np.array(img).astype(np.float32)/255.0 - mean) / std   # HWC
arr = arr.transpose(2,0,1)[None, ...].astype(np.float32)      # NCHW with batch=1
arr.tofile(f"{OUT_DIR}/input_0.bin")

with open(f"{OUT_DIR}/input_list.txt", "w") as f:
    f.write(f"{OUT_DIR}/input_0.bin\n")   # "<tensor_name> <path/to/bin>"
print(f"Wrote {OUT_DIR}/input_0.bin & {OUT_DIR}/input_list.txt")
