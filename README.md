## LTO-dataset: An Dataset of Long Text Over-Refusal Benchmark for LLMs

<table style="width:100%; border-collapse: collapse;">
  <tr>
    <th style="border: 1px solid black;text-align:center;"><a href=https://huggingface.co/datasets/JACKSONSs/LTO-dataset>Dataset</a></th>
  </tr>
</table>

## LTO Workflow
This repository provides a workflow to generate, transform, filter, and assess prompts for evaluating LLMs over-refusal behavior. The process involves creating toxic seed prompts, rewriting them into potentially over-refusal-triggering harmless prompts, selecting prompts refused by multiple models, and verifying their harmlessness.
<img src="images/overall_workflow.png" alt="Image 1" style="width: 100%;"/>

## Get Started
First, download our repo
```
git clone https://github.com/sheerheart3-sketch/LTO-dataset
cd LTO-dataset
```

Next, install the required libraries
```
conda env create -f environment.yml
```

## Generate Prompts
### Set API Keys
In order to use a specifc model API, please set the environment such as OpenAI as following
```
export OPENAI_API_KEY="your_deepseek_api_key"
export export DMX_API_KEY="your_dmx_api_key"
```
### Generate Toxic Seeds
Generates initial toxic prompts categorized by sensitivity types
```
python generate_toxic.py
```

### Rewrite Toxic Seeds
Transforms toxic seeds into harmless prompts that may still trigger over-refusal in LLMs.
```
python rewrite.py
```

### Test Model Refusals
Evaluates which prompts are refused by specific models
```
python test.py --model Qwen3-8B
```
### Select Prompts Refused by ≥2 Models
Filters prompts that are refused by at least two models.
```
python vote.py
```

## Assess Harmfulness
Verifies if selected prompts are truly harmless using a classifier.
```
python access.py
```
<img src="images/overall_x_y_plot.png" alt="Image 1" style="width: 100%;"/>

## Reference
If you find our code useful for your research, please consider citing our paper.
```
@article{Liu2025LTO,
  title={LTO: A Benchmark for Over-Refusal in Long In-Context Large Language Models},
  author={Cui, Justin and Chiang, Wei-Lin and Stoica, Ion and Hsieh, Cho-Jui},
  year={2025}
}
```
