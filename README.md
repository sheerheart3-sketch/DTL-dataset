A dataset of long text over-refusal benchmark with 470 harmless prompts and 210 toxic prompts.
Overview
This repository provides a workflow to generate, transform, filter, and assess prompts for evaluating large language models' (LLMs) over-refusal behavior. The process involves creating toxic seed prompts, rewriting them into potentially over-refusal-triggering harmless prompts, selecting prompts refused by multiple models, and verifying their harmlessness.
Workflow
1. Generate Toxic Seed Prompts
Script: generate_toxic.pyGenerates initial toxic prompts categorized by sensitivity types.
Input: None (uses predefined sensitivity categories)
Output: ./inputs/toxic_seed.json (contains toxic prompts with categories: selfharm, sexual harassment, internet-harassment, violence, deception, hate, privacy)
2. Rewrite to Harmless Prompts
Script: rewritter.pyTransforms toxic seeds into harmless prompts that may still trigger over-refusal in LLMs.
Input: ./inputs/toxic_seed.json
Output: ./inputs/PesHarmPromopt.json (harmless prompts with potential over-refusal triggers, each ≥300 words)
3. Test Model Refusals
Script: test.pyEvaluates which prompts are refused by specific models (configurable via arguments).
Input: ./inputs/PesHarmPromopt.json
Output:
./selection/{model}.json (prompts refused by the model)
./statistical_result/per_count_{model}.json (refusal counts per category)
4. Select Prompts Refused by ≥2 Models
Script: vote.pyFilters prompts that are refused by at least two models.
Input: Files in ./selection/ (model-specific refusal results)
Output: ./inputs/selected_prompts.json (prompts with consistent refusal across models)
5. Assess Harmfulness
Script: assess.pyVerifies if selected prompts are truly harmless using a classifier.
Input: ./inputs/selected_prompts.json
Output:
./safe_selection/{model}.json (confirmed harmless prompts)
result.txt (safety rate statistics)
Dependencies
Python 3.x
Required libraries:
bash
运行
pip install openai torch tqdm requests datasets
Environment Setup
Set required API keys as environment variables:
bash
运行
# For deepseek-reasoner (used in generate_toxic.py, rewritter.py, assess.py)
export OPENAI_API_KEY="your_deepseek_api_key"

# For model testing (used in test.py)
export DMX_API_KEY="your_dmx_api_key"
License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.# DTL-dataset
A dataset of long text over-refusal benchmark with 470 harmless prompts and 210 toxic prompts.
Overview
This repository provides a workflow to generate, transform, filter, and assess prompts for evaluating large language models' (LLMs) over-refusal behavior. The process involves creating toxic seed prompts, rewriting them into potentially over-refusal-triggering harmless prompts, selecting prompts refused by multiple models, and verifying their harmlessness.
Workflow
1. Generate Toxic Seed Prompts
Script: generate_toxic.pyGenerates initial toxic prompts categorized by sensitivity types.
Input: None (uses predefined sensitivity categories)
Output: ./inputs/toxic_seed.json (contains toxic prompts with categories: selfharm, sexual harassment, internet-harassment, violence, deception, hate, privacy)
2. Rewrite to Harmless Prompts
Script: rewritter.pyTransforms toxic seeds into harmless prompts that may still trigger over-refusal in LLMs.
Input: ./inputs/toxic_seed.json
Output: ./inputs/PesHarmPromopt.json (harmless prompts with potential over-refusal triggers, each ≥300 words)
3. Test Model Refusals
Script: test.pyEvaluates which prompts are refused by specific models (configurable via arguments).
Input: ./inputs/PesHarmPromopt.json
Output:
./selection/{model}.json (prompts refused by the model)
./statistical_result/per_count_{model}.json (refusal counts per category)
4. Select Prompts Refused by ≥2 Models
Script: vote.pyFilters prompts that are refused by at least two models.
Input: Files in ./selection/ (model-specific refusal results)
Output: ./inputs/selected_prompts.json (prompts with consistent refusal across models)
5. Assess Harmfulness
Script: assess.pyVerifies if selected prompts are truly harmless using a classifier.
Input: ./inputs/selected_prompts.json
Output:
./safe_selection/{model}.json (confirmed harmless prompts)
result.txt (safety rate statistics)
Dependencies
Python 3.x
Required libraries:
pip install openai torch tqdm requests datasets
Environment Setup
Set required API keys as environment variables:
# For deepseek-reasoner (used in generate_toxic.py, rewritter.py, assess.py)
export OPENAI_API_KEY="your_deepseek_api_key"

# For model testing (used in test.py)
export DMX_API_KEY="your_dmx_api_key"
