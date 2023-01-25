#!/bin/bash

#SBATCH --partition=gpu_shared
#SBATCH --gres=gpu:0
#SBATCH --job-name=GOT_long_inst_new2
#SBATCH --ntasks=1
#SBATCH --gpus-per-task=1
#SBATCH --time=10:00:00
#SBATCH --mem=32000M
#SBATCH --output=output_generate_GOT_long_ist_new2
#SBATCH --mail-type=BEGIN,END,CANCELLED
#SBATCH --mail-user=<terryliberatore@gmail.com>

srun python -u generate_long.py 
