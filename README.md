![alt text](https://github.com/antomicblitz/deepvariant-GPU-GUI/blob/main/google-deep-variant-gui.PNG?raw=true)
# google-deepvariant-GPU-GUI V1.0
The script provides a graphical user interface (GUI) to run the DeepVariant pipeline using the GPU-enabled Docker container. The use of docker greatly simplifies the installation of dependencies and makes it possible to run the pipelines in just a few clicks. The GUI simplifies the process of specifying input files, output directories, reference genomes, and other options for running DeepVariant, making it more accessible to users without extensive command-line experience. 

Here's a summary of the script's functionality:

The script creates a tkinter-based GUI with input fields and browse buttons for selecting the required directories and files. These include the input BAM file, output directory, reference genome, reference genome index, and optional regions of interest.

The script allows users to choose the model type (WGS or WES) and specify the number of shards for parallel processing.

Once the user has provided all the necessary inputs and clicked the "Run Script" button, the script generates a bash command to run the DeepVariant pipeline using the specified options.

The script writes the generated bash command to a temporary file (bash_script.sh) and executes it using the subprocess module. This step involves pulling the DeepVariant GPU-enabled Docker container, running the container with the appropriate volume mounts, and executing the DeepVariant pipeline inside the container.

The output VCF and gVCF files are written to the specified output directory, with filenames derived from the input BAM file.

For further information, check here: Refer to https://github.com/google/deepvariant 
# Requirements
## Windows
In windows, you need to install Docker and WSL2, and Ubuntu for WSL2

From Ubuntu, you need to run the following in a BASH terminal to install all dependencies:
apt-get install python pip tkinter tqdm

once these are installed, download this folder directly (or use the git command "git pull google-deepvariant-GUI) to download the folder.

Tip: If you are running WSL2, make sure that you give enough RAM or the process might fail. By defauly, WSL2 only allocates 50% of the RAM. Follow this guide:https://fizzylogic.nl/2023/01/05/how-to-configure-memory-limits-in-wsl2#:~:text=Memory%20usage%20in%20WSL2&text=Memory%20is%20limited%20to%20half,and%20all%20CPU%2FGPU%20cores.

## Mac or Linux
As long as the python environment to run the script is set up correctly and you have installed all the dependencies, it should work. Make sure docker is installed.

# Running the GUI

Once it is downloaded, use the cd command to enter into the google-deep-variant-GUI folder (cd google-deep-variant-GUI folder)

run the GUI using this command from the Ubuntu Bash Terminal: python deep_variant_GUI.py

**This has only been tested on Windows 11, but should also work on any Mac or Linux machine with the proper environment. You will need the following installed: Docker for Windows and Windows Subsystem for Linux 2 (WSL2).
Be aware that the uncompressed reference genome file (in this case hg38.fa) and index file (hg38.fai) should be in the Index_Files folder within the working directory. If you don't have them already, the tool has the option to download them from UCSC, but you should make sure that they are same version you used for your alignment. If not, you can use "samtools faidx [yourfasta.fa]" to make your index file. If you used a different reference file, you need to make your own index or the script will fail. Just make sure they are both in the Index_Files directory.**

# Inputs
Before you start running, you need to have the following input files:

A reference genome in FASTA format and its corresponding index file (.fai).

An aligned reads file in BAM format and its corresponding index file (.bai). You get this by aligning the reads from a sequencing instrument, using an aligner like BWA for example.

These files should be together in a directory that is specified in the GUI. **Make sure the .fa and .fai files have the same name.**

# Outputs
VCF and gVCF variant calling file ready for filtering and downstream processing. You can specify the output directory.

# Settings:
The GUI allows you to change important settings, like which model to use for variant calling, how many processors to use, and which region of the chromosome to perform the variant calling for the BAM file. The settings you can change are given below.
Refer to the readme file from Google Deepvariant for more information if something is not clear: https://github.com/google/deepvariant

## Model Type
The tool lets you specify the Model Type used based on the sequencing . **Replace this string with exactly one of the following [WGS,WES,PACBIO,ONT_R104,HYBRID_PACBIO_ILLUMINA]**

DeepVariant is trained on different datasets for different sequencing technologies to optimize variant calling performance. Here's a brief explanation of each option:

**WGS**: Whole Genome Sequencing - This option is for data generated from sequencing an entire genome. The model is trained on datasets that contain reads from the entire genome.

**WES**: Whole Exome Sequencing - This option is for data generated from sequencing only the exome (protein-coding regions) of a genome. The model is trained on datasets that contain reads from targeted exome capture.

**PACBIO**: Pacific Biosciences - This option is for data generated using the Pacific Biosciences (PacBio) sequencing platform, which is known for its long-read sequencing technology. The model is trained on datasets that contain long reads from the PacBio platform.

**ONT_R104**: Oxford Nanopore Technologies - This option is for data generated using the Oxford Nanopore Technologies (ONT) sequencing platform, another long-read sequencing technology. The model is trained on datasets that contain long reads from the ONT platform.

**HYBRID_PACBIO_ILLUMINA**: Hybrid PacBio-Illumina - This option is for data generated using a combination of both PacBio and Illumina sequencing platforms. The model is trained on datasets that contain a mix of long reads from PacBio and short reads from Illumina.

## Number of Shards
Shards: In the context of the DeepVariant pipeline, shards refer to the division of the input data (in this case, the genome data) into smaller, more manageable pieces. By sharding the data, each piece is run independently and in parallel, which can significantly speed up the overall analysis. The number of shards to use depends on the size of your input data and the computational resources available. Default is number of shards = number of CPUs.


## Regions
Here you can specify which chromosome(s) or regions to perform the variant calling. Here are examples of valid arguments (remember to use without parantheses):
"chr2" 
"chr2:100000-120000"
"chr1 chr2 chr3"
etc. 

Note, keep in mind that if your chromosome names are different in your indexed reference genome, you should use this naming convention instead. You can check in the index file. 

If there are any issues, please contact:
contact@lambconsulting.bio
