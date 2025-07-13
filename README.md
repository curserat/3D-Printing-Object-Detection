# 3D-Printing-Object-Detection

For development of the ML model.

## Setup
Install [Docker](https://www.docker.com/) (Docker Desktop on Windows)*\
*For Windows, install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) and enable WSL integration (enabled by default) in Docker Desktop

## Dev
**Please work on a test branch before pushing to main.**\
\
We'll be working with .py files for model training and testing. 
If additional packages/libraries need to be imported, please add them to the requirements.txt file and rebuild your docker image.\
**NOTE**: You must use the ```tensorflow[and-cuda]``` package for GPU utilization. If you are not using an NVIDA GPU, use the ```tensorflow``` package in requirements.txt. 


## Training with a GPU
Epoch time will depend on the local machine hardware specs. Using a dedicated GPU will speed up the rate an epoch is finished.
If using Docker Desktop, we need to use GPU integration for WSL which will require an NVIDIA GPU. Please follow the documentation for [Docker GPU support](https://docs.docker.com/desktop/features/gpu/).\
\
**For a quick run down:**\
1.) Update your drivers (NVIDIA Only)\
2.) Install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) with Ubuntu\
3.) Enter ```sudo apt-key del 7fa2af80``` into WSL\
4.) Install the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0) (Follow the instructions for the Linux x86, Ubuntu WSL package)

## Docker
To build the image for the training session:\
```docker build -t [image name] .```\
\
Then, run the image:\
```docker run [image name]```\
\
For GPU utilization:\
```docker run --gpus all [image name]```

For Jupyter Lab w/o GPU utilization:\
```docker run -p 8888:8888 [image name]```

For Jupyter Lab with GPU utilization:\
```docker run --gpus all -p 8888:8888 [image name]```
