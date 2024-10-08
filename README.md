# torchtune-does-math

Repo for finetuning DeepSeek 7B model on [NaturalProofs dataset](https://github.com/wellecks/naturalproofs).

## Setup

Download the four datasets:

```
wget https://zenodo.org/record/4902202/files/naturalproofs_trench.json?download=1 -O /data/users/ebs/naturalproofsdata/naturalproofs_trench.json
wget https://zenodo.org/record/4902202/files/naturalproofs_stacks.json?download=1 -O /data/users/ebs/naturalproofsdata/naturalproofs_stacks.json
wget https://zenodo.org/record/4902202/files/naturalproofs_proofwiki.json?download=1 -O /data/users/ebs/naturalproofsdata/naturalproofs_proofwiki.json
wget https://zenodo.org/record/4902289/files/naturalproofs_stein.py?download=1 -O /data/users/ebs/torchtune-does-math/torchtune-does-math/data/download_number_theory.py
python3 data/download_number_theory.py --outdir /data/users/ebs/naturalproofs/
```

Clean the datasets

```
python3 data/preproc.py
```

## Finetuning

LoRA finetuning:
```
tune run custom_lora_single_device --config custom_lora_single_device.yaml metric_logger.name=lora_v0
```

Full finetuning:
```
tune run custom_fft_single_device --config custom_fft_single_device.yaml metric_logger.name=fft_v0
```

QLoRA finetuning:

```
tune run custom_lora_single_device --config custom_lora_single_device.yaml metric_logger.name=qlora_v0 model.quantize_base=True
```

## Generation

On the base model:

```
tune run custom_generate --config custom_generation.yaml prompt="The integral of x^2 from 0 to 2 is"
...
<｜begin▁of▁sentence｜>The integral of x^2 from 0 to 2 is 8/3. ... What Is the Integral of X? ...
```

On the finetuned model:

```
tune run custom_generate --config custom_generation.yaml checkpointer.checkpoint_dir=/data/users/ebs/tuneathon-ckpts/base-model checkpointer.checkpoint_files=['hf_model_0001_0.pt','hf_model_0002_0.pt'] prompt="The square root of 2 is irrational."
```