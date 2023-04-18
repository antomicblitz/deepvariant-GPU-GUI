# google-deepvariant-GUI 
This application is a work in progress, but will generate a user-friendly GUI for setting up and running a GPU version of Google's DeepVariant with GPU capabilities in a Docker container.
For further information, check here: Refer to https://github.com/google/deepvariant 
# Requirements
In windows, you need to install Docker and WSL2, and Ubuntu for WSL2

From Ubuntu, you need to run the following in a BASH terminal to install all dependencies:
apt-get install python pip tkinter tqdm samtools

once these are installed, download this folder directly (or use the git command "git pull google-deepvariant-GUI) to download the folder.
# Running the GUI

Once it is downloaded, use the cd command to enter into the google-deep-variant-GUI folder (cd google-deep-variant-GUI folder)

run the GUI using this command from the Ubuntu Bash Terminal: python deep_variant_GUI.py

**This has only been tested on Windows 11. You will need the following installed: Docker for Windows and Windows Subsystem for Linux 2 (WSL2).
Be aware that the uncompressed reference genome file (in this case hg38.fa) and index file (hg38.fai) should be in the Index_Files folder within the working directory. If you don't have them already, the tool has the option to download them from UCSC, but you should make sure that they are same version you used for your alignment. If not, you can use "samtools faidx [yourfasta.fa]" to make your index file. If you used a different reference file, you need to make your own index or the script will fail. Just make sure they are both in the Index_Files directory.**

# Input
Before you start running, you need to have the following input files:

A reference genome in FASTA format and its corresponding index file (.fai).

An aligned reads file in BAM format and its corresponding index file (.bai). You get this by aligning the reads from a sequencing instrument, using an aligner like BWA for example.

# Outputs
VCF and gVCF variant calling file ready for filtering and downstream processing. You can specify the output directory.

# Settings:
The GUI allows you to change important settings, like which model to use for variant calling, how many processors to use, and which region of the chromosome to perform the variant calling for the BAM file. 
Refer to the readme file from Google Deepvariant for more information: https://github.com/google/deepvariant

## Model Type
The tool lets you specify the Model Type used based on the sequencing . **Replace this string with exactly one of the following [WGS,WES,PACBIO,ONT_R104,HYBRID_PACBIO_ILLUMINA]**

DeepVariant is trained on different datasets for different sequencing technologies to optimize variant calling performance. Here's a brief explanation of each option:

**WGS**: Whole Genome Sequencing - This option is for data generated from sequencing an entire genome. The model is trained on datasets that contain reads from the entire genome.

**WES**: Whole Exome Sequencing - This option is for data generated from sequencing only the exome (protein-coding regions) of a genome. The model is trained on datasets that contain reads from targeted exome capture.

**PACBIO**: Pacific Biosciences - This option is for data generated using the Pacific Biosciences (PacBio) sequencing platform, which is known for its long-read sequencing technology. The model is trained on datasets that contain long reads from the PacBio platform.

**ONT_R104**: Oxford Nanopore Technologies - This option is for data generated using the Oxford Nanopore Technologies (ONT) sequencing platform, another long-read sequencing technology. The model is trained on datasets that contain long reads from the ONT platform.

**HYBRID_PACBIO_ILLUMINA**: Hybrid PacBio-Illumina - This option is for data generated using a combination of both PacBio and Illumina sequencing platforms. The model is trained on datasets that contain a mix of long reads from PacBio and short reads from Illumina.

## Number of Shards
This setting specifies the number of CPUs to use for DeepVariant. By default, it will read ncores and use all available cores. Feel free to change it.

## Regions
Here you can specify which chromosome(s) or regions to use. Here are examples of valid arguments (without parantheses):
"chr2" 
"chr2:100,000-120,000"

If there are any issues, please contact:
contact@lambconsulting.bio
