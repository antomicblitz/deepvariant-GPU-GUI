# Script created by Antonio Lamb using assistance from ChatGPT 4.0
# To do list: Fix downloads.
# Note, you need to have Docker, Windows Subsystem for Linux, and Ubuntu installed.
# Install python3, pip, tkinter, tqdm from ubuntu BASH using sudo apt-get install
import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def browse_input_bam():
    filepath = filedialog.askopenfilename()
    input_bam_var.set(filepath)

def browse_output_directory():
    folder = filedialog.askdirectory()
    output_directory_var.set(folder)

def browse_ref_genome():
    filepath = filedialog.askopenfilename()
    ref_genome_var.set(filepath)

def run_bash_script():
    input_bam = input_bam_var.get()
    output_directory = output_directory_var.get()
    ref_genome = ref_genome_var.get()
    model_type = model_type_var.get()
    num_shards = int(num_shards_var.get())
    num_shards_default = os.cpu_count()
    regions = regions_var.get()

    regions_flag = f"--regions {regions}" if regions else ""

    output_basename = os.path.splitext(os.path.basename(input_bam))[0]

    bash_command = f"""#!/bin/bash
# Pull the GPU-enabled DeepVariant container
sudo docker pull gcr.io/deepvariant-docker/deepvariant_gpu:latest
# Run the container with GPU support
sudo docker run \
  --gpus 1 \
  -v {os.path.dirname(input_bam)}:/input \
  -v {output_directory}:/output \
  -v {os.path.dirname(ref_genome)}:/ref_files \
  gcr.io/deepvariant-docker/deepvariant_gpu:latest \
  /opt/deepvariant/bin/run_deepvariant \
  --model_type={model_type} \
  --ref=/ref_files/{os.path.basename(ref_genome)} \
  --reads=/input/{os.path.basename(input_bam)} \
  --output_vcf=/output/{output_basename}.vcf.gz \
  --output_gvcf=/output/{output_basename}.g.vcf.gz \
  --num_shards={num_shards} \
   {regions_flag}
"""

    with open("bash_script.sh", "w") as file:
        file.write(bash_command)

    subprocess.run(["bash", "bash_script.sh"])

root = tk.Tk()
root.title("DeepVariant GUI")

input_bam_var = tk.StringVar()
output_directory_var = tk.StringVar()
ref_genome_var = tk.StringVar()
model_type_var = tk.StringVar(value="WGS")
num_shards_default = os.cpu_count()
num_shards_var = tk.StringVar(value=str(num_shards_default))
regions_var = tk.StringVar(value="chr20:100000-110000")

tk.Label(root, text="Input BAM:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=input_bam_var, width=50).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_input_bam).grid(row=1, column=2)
tk.Label(root, text="Output Directory:").grid(row=2, column=0, sticky="w")
tk.Entry(root, textvariable=output_directory_var, width=50).grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_output_directory).grid(row=2, column=2)

tk.Label(root, text="Reference Genome:").grid(row=3, column=0, sticky="w")
tk.Entry(root, textvariable=ref_genome_var, width=50).grid(row=3, column=1)
tk.Button(root, text="Browse", command=browse_ref_genome).grid(row=3, column=2)

tk.Label(root, text="Model Type:").grid(row=4, column=0, sticky="w")
tk.Entry(root, textvariable=model_type_var, width=50).grid(row=4, column=1)

tk.Label(root, text="Number of Shards:").grid(row=5, column=0, sticky="w")
tk.Entry(root, textvariable=num_shards_var, width=50).grid(row=5, column=1)

tk.Label(root, text="Regions:").grid(row=6, column=0, sticky="w")
tk.Entry(root, textvariable=regions_var, width=50).grid(row=6, column=1)

tk.Button(root, text="Run Script", command=run_bash_script).grid(row=7, column=1)

root.mainloop()
