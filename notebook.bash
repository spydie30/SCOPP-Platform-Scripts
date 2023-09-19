#!/bin/bash

eval "$(conda shell.bash hook)"
conda activate base
cd .
jupyter notebook
