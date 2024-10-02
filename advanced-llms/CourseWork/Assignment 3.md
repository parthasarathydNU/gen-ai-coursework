# Assignment 3: Self Alignment with Instruction Backtranslation

**Total Points: 100**

## Overview

This assignment involves implementing the "Self Alignment with Instruction Backtranslation" paper using LoRA for fine-tuning. Due to memory constraints, full fine-tuning is not possible.

**Paper Link**: [Self Alignment with Instruction Backtranslation](https://arxiv.org/pdf/2308.06259.pdf)

**Note**: Due to Colab's GPU usage limitations, prototype and test on CPU first before training on GPU with the full dataset. If GPU access on Colab is unavailable, consider using PyTorch Lightning Studio or a Kaggle notebook.

## Tasks

### 1. Fine-tune Base Language Model (25 points)

- Use LLaMA 2 7B as the base model
- Fine-tune with (output, instruction) pairs {(yi, xi)} from the seed data
- Obtain a backward model Myx := p(x|y) that predicts instructions from outputs
- Use the OpenAssistant-Guanaco training set dataset
- Push the backward model to Hugging Face Hub
- **Deliverable**: Paste the Hugging Face Hub URL here: [Your URL]

### 2. Self-Augmentation (25 points)

- Randomly sample 150 examples from the LIMA dataset's completions
- Generate instructions using the backward model
- Filter out multi-turn examples
- **Deliverable**: Print 5 examples of generated instructions
  - Format: (generated instruction from backward model, response from LIMA)
  - Ensure examples are single-turn, e.g., (What is the capital of France?, Paris)

### 3. Self-Curation (25 points)

- Use few-shot prompting and the prompt from Table 1 in the paper
- Implement a quality selection process for examples
- Use an LLM (meta/llama-7b-chat-hf) to rate examples
- Prompt: "Evaluate the quality of the instruction/response pair [example]. Rate it from 1-5."
- **Deliverables**:
  - Print 5 high-quality examples and 5 low-quality examples
  - Push the curated dataset to Hugging Face Hub
  - Paste the Hugging Face Hub URL here: [Your URL]

### 4. Fine-tune Base Model on Curated Dataset (25 points)

- Use the dataset generated in step 3
- Fine-tune the base model
- **Deliverables**:
  - Print 5 example responses from the fine-tuned model
  - Push the instruction fine-tuned model to Hugging Face Hub
  - Paste the Hugging Face Hub URL here: [Your URL]

## Submission

Please include a link to your Colab notebook here: [Your Colab Notebook URL]
