# google-deepvariant-GUI 
This application is a work in progress, but will generate a user-friendly GUI for setting up and running a GPU version of Google's DeepVariant with GPU capabilities in a Docker container.
For further information, check here: Refer to https://github.com/google/deepvariant 
# Requirements
## windows
In windows, you need to install Docker and WSL2, and Ubuntu for WSL2

From Ubuntu, you need to run the following in a BASH terminal to install all dependencies:
apt-get install python pip tkinter tqdm samtools

once these are installed, download this folder directly (or use the git command "git pull google-deepvariant-GUI) to download the folder.

Tip: If you are running WSL2, make sure that you give enough RAM or the process might fail. By defauly, WSL2 only allocates 50% of the RAM. Follow this guide:https://fizzylogic.nl/2023/01/05/how-to-configure-memory-limits-in-wsl2#:~:text=Memory%20usage%20in%20WSL2&text=Memory%20is%20limited%20to%20half,and%20all%20CPU%2FGPU%20cores.

## Mac or Linux
As long as the python environment is set up correctly and you have installed all the dependencies, it should work.

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
This setting specifies the number of CPUs to use for DeepVariant. By default, it will read use all available cores. Feel free to change it.

## Regions
Here you can specify which chromosome(s) or regions to perform the variant calling. Here are examples of valid arguments (remember to use without parantheses):
"chr2" 
"chr2:100000-120000"
"chr1 chr2 chr3"
etc. 

Note, keep in mind that if your chromosome names are different in your indexed reference genome, you should use this naming convention instead. You can check in the index file. 

If there are any issues, please contact:
contact@lambconsulting.bio
