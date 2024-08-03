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

## Next Steps:
- Generating the preference dataset using PariRM
- Push Preference Dataset to HuggingFace
- Fine tuning Mistral-7B-Instruct-v2.0
- Iteratively following the above process for 3 iterations
- Evaluating performance of new model to base model on unseen data

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
