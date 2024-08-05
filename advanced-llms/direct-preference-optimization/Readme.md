# Direct Preference Optimization for LLM Fine-tuning

## Overview
This project implements the technique described in the "Direct Preference Optimization" paper to fine-tune large language models (LLMs) to better understand and align with human preferences. The goal is to enhance the LLM's ability to generate responses that are not only accurate but also align with human values and preferences.

## Objective
The main objective of this project is to apply direct preference optimization techniques to improve the alignment of LLM outputs with human evaluative standards. This involves training models on a dataset annotated according to human preferences, thereby enabling the models to generate more user-aligned content.

## How It Works
- **Data Collection**: Collecting data samples which represent varied human preferences.
- **Annotation**: Annotating these samples with preferences using a method aligned with the one proposed in the paper.
- **Model Training**: Fine-tuning a pre-trained LLM using the annotated dataset with a focus on optimizing for these preferences.
- **Evaluation**: Assessing the performance of the fine-tuned model using both automated metrics and human evaluations to measure alignment with human preferences.

## Status Update
- **Generated data samples for annotation using Mistral-7B-Instruct-v2.0** : [DPODataSetGeneration.ipynb](./DPODataSetGeneration.ipynb)
- **Generated Data Samples** : [generated_responses_DPO.json](./generated_responses_DPO.json)
- **Generated Preference Dataset and Pushed to Hugging Face** [DhruvParth/Mistral-7B-Instruct-v2.0-PairRM-DPO-Dataset](https://huggingface.co/datasets/DhruvParth/Mistral-7B-Instruct-v2.0-PairRM-DPO-Dataset)
- **Fine tunined Mistral-7B-Instruct-v2.0 for one iteration** [dpomistralfinetuning.ipynb](./dpomistralfinetuning.ipynb)


## Next Steps:
- Figure out how to evaluate model performance [Reference Article](https://ritikjain51.medium.com/llms-fine-tuning-and-evaluation-f019515b1c67)
- Iteratively following the above process for 3 iterations and evaluate model performance

## Contributing
Contributions to this project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) file for details.

## Acknowledgements
- Inspired by the techniques proposed in the "Direct Preference Optimization" paper.
- Thanks to all contributors who have helped in refining the approach and expanding the dataset.

## Contact
For any queries or discussions regarding the project, please open an issue in the GitHub repository, reach out to me via [LinkedIn](https://www.linkedin.com/in/parthadhruv/)  or contact me directly at parthasarathy.d@northeastern.edu.

## Citation
```
@inproceedings{
    rafailov2023direct,
    title={Direct Preference Optimization: Your Language Model is Secretly a Reward Model},
    author={Rafael Rafailov and Archit Sharma and Eric Mitchell and Christopher D Manning and Stefano Ermon and Chelsea Finn},
    booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
    year={2023},
    url={https://arxiv.org/abs/2305.18290}
}
```

## References used
- [Fine Tuned Model: snorkelai/Snorkel-Mistral-PairRM-DPO](https://huggingface.co/snorkelai/Snorkel-Mistral-PairRM-DPO)
- [Dataset: snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset](https://huggingface.co/datasets/snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset)
- [Fine-tune Llama 2 with DPO: HuggingFace Blog](https://huggingface.co/blog/dpo-trl)
- [Article: DPO-Fine-Tuning for Enhanced Language Model Performance](https://medium.com/@mauryaanoop3/dpo-fine-tuning-for-enhanced-language-model-performance-466fec349a5e)
- [PairRM Model](https://huggingface.co/llm-blender/PairRM)
- [GitHub DPO Implementation](https://github.com/eric-mitchell/direct-preference-optimization)
- [YouTube Video - Mistra-7B Inference](https://www.youtube.com/watch?v=eovBbABk3hw&ab_channel=Rohan-Paul-AI)
- [Inferencing Mistral-7B](https://github.com/rohan-paul/LLM-FineTuning-Large-Language-Models/blob/main/Mistral-7B-Inferencing.ipynb)
