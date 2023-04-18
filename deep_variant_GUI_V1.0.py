# Script created by Antonio Lamb using assistance from ChatGPT 4.0
# To do list: Fix downloads.
# Note, you need to have Docker, Windows Subsystem for Linux, and Ubuntu installed.
# Install python3, pip, tkinter, tqdm from ubuntu BASH using sudo apt-get install
import os
import tkinter as tk
from tkinter import filedialog
import subprocess
from urllib.request import urlretrieve
from tqdm import tqdm

class TqdmUpTo(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_with_progress_bar(url, output_path):
    with TqdmUpTo(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urlretrieve(url, filename=output_path, reporthook=t.update_to)

def browse_input_directory():
    folder = filedialog.askdirectory()
    input_directory_var.set(folder)

def browse_output_directory():
    folder = filedialog.askdirectory()
    output_directory_var.set(folder)

def download_reference_files():
    index_file_url = "https://drive.google.com/uc?export=download&id=1u3GLKR6Y31_X2hW7i-VWytBHNp1urYH0"
    dict_file_url = "https://drive.google.com/uc?export=download&id=1u3GLKR6Y31_X2hW7i-VWytBHNp1urYH0"

    index_file_path = os.path.join("Index Files", "hg38.fa")
    dict_file_path = os.path.join("Index Files", "hg38.fa.fai")

    if not os.path.exists("Index Files"):
        os.makedirs("Index Files")

    if not os.path.isfile(index_file_path):
        download_with_progress_bar(index_file_url, index_file_path)

    if not os.path.isfile(dict_file_path):
        download_with_progress_bar(dict_file_url, dict_file_path)

    download_button.config(state="disabled", text="Files Downloaded")

import os

def run_bash_script():
    input_directory = input_directory_var.get()
    output_directory = output_directory_var.get()
    model_type = model_type_var.get()
    num_shards = num_shards_var.get()
    regions = regions_var.get()

    regions_flag = f"--regions {regions}" if regions else ""

    bam_files = " ".join([f"/input/{os.path.basename(f)}" for f in os.listdir(input_directory) if f.endswith(".bam")])

    bash_command = f"""#!/bin/bash
# Pull the GPU-enabled DeepVariant container
sudo docker pull gcr.io/deepvariant-docker/deepvariant_gpu:latest

# Run the container with GPU support
sudo docker run \
  --gpus all \
  -v {input_directory}:/input \
  -v {output_directory}:/output \
  -v $(pwd)/Index_Files:/index_files \
  gcr.io/deepvariant-docker/deepvariant_gpu:latest \
  /opt/deepvariant/bin/run_deepvariant \
  --model_type={model_type} \
  --ref=/index_files/hg38.fa \
  --reads={bam_files} \
  --output_vcf=/output/output.vcf.gz \
  --output_gvcf=/output/output.g.vcf.gz \
  --num_shards={num_shards} \
  {regions_flag}
"""

    with open("bash_script.sh", "w") as file:
        file.write(bash_command)

    subprocess.run(["bash", "bash_script.sh"])

root = tk.Tk()
root.title("DeepVariant GUI")

input_directory_var = tk.StringVar()
output_directory_var = tk.StringVar()
model_type_var = tk.StringVar(value="WGS")
num_shards_var = tk.IntVar(value=16)
regions_var = tk.StringVar(value="chr20")

index_file_path = os.path.join("Index Files", "hg38.fa.fai")
dict_file_path = os.path.join("Index Files", "hg38.dict")

if not os.path.exists("Index Files") or not (os.path.isfile(index_file_path) and os.path.isfile(dict_file_path)):
    download_button = tk.Button(root, text="Download Reference Files", command=download_reference_files)
    download_button.grid(row=0, column=1)

tk.Label(root, text="Input Directory:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=input_directory_var, width=50).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_input_directory).grid(row=1, column=2)

tk.Label(root, text="Output Directory:").grid(row=2, column=0, sticky="w")
tk.Entry(root, textvariable=output_directory_var, width=50).grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_output_directory).grid(row=2, column=2)

tk.Label(root, text="Model Type:").grid(row=3, column=0, sticky="w")
tk.Entry(root, textvariable=model_type_var, width=50).grid(row=3, column=1)

tk.Label(root, text="Number of Shards:").grid(row=4, column=0, sticky="w")
tk.Entry(root, textvariable=num_shards_var, width=50).grid(row=4, column=1)

tk.Label(root, text="Regions:").grid(row=5, column=0, sticky="w")
tk.Entry(root, textvariable=regions_var, width=50).grid(row=5, column=1)

tk.Button(root, text="Run Script", command=run_bash_script).grid(row=6, column=1)

root.mainloop()