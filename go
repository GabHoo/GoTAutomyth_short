#!/bin/bash

#SBATCH --partition=gpu_shared
#SBATCH --gres=gpu:0
#SBATCH --job-name=DWIE_instances
#SBATCH --ntasks=1
#SBATCH --gpus-per-task=1
#SBATCH --time=10:00:00
#SBATCH --mem=32000M
#SBATCH --output=DWIE_instances
#SBATCH --mail-type=BEGIN,END,CANCELLED
#SBATCH --mail-user=<terryliberatore@gmail.com>

srun python -u generate_transformer_DWIE.py Instances Instances
