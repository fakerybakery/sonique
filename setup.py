from setuptools import setup, find_packages

setup(
    name='stable-audio-tools',
    version='0.0.9',
    url='https://github.com/Stability-AI/stable-audio-tools.git',
    author='Stability AI',
    description='Training and inference tools for generative audio models from Stability AI',
    packages=find_packages(),  
    install_requires=[
        'audiocraft==1.0.0',
        'aeiou==0.0.20',
        'alias-free-torch==0.0.6',
        'auraloss==0.4.0',
        'descript-audio-codec==1.0.0',
        'einops==0.7.0',
        'einops-exts==0.0.4',
        'ema-pytorch==0.2.3',
        'encodec==0.1.1',
        'gradio==3.42.0',
        'huggingface_hub',
        'importlib-resources==5.12.0',
        'k-diffusion==0.1.1',
        'laion-clap==1.1.4',
        'local-attention==1.8.6',
        'pandas==2.0.2',
        'pedalboard==0.7.4',
        'prefigure==0.0.9',
        'pytorch_lightning==2.1.0', 
        'PyWavelets==1.4.1',
        'safetensors',
        'sentencepiece==0.1.99',
        's3fs',
        'torch>=2.0.1',
        'torchaudio>=2.0.2',
        'torchmetrics==0.11.4',
        'tqdm',
        'transformers==4.38.1',
        'v-diffusion-pytorch==0.0.2',
        'vector-quantize-pytorch==1.9.14',
        'wandb==0.15.4',
        'webdataset==0.2.48',
        'x-transformers>=1.25.15'
    ],
)