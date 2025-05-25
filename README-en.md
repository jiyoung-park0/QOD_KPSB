# QOD_KPSB (QOD-Korean Political Sentiment BERT)

QOD_KPSB is a sentiment classification model tailored for Korean political discourse.
Fine-tuned from the KoELECTRA architecture, this model is designed to automatically predict the sentiment of key political terms found in news articles, comments, and official party statements.

In many Korean political science studies, general-purpose sentiment lexicons or BERT models have traditionally been used to measure sentiment. However, such tools often fall short when applied to political texts, which frequently include domain-specific terminology, references to particular events or ideologies, slang, and neologisms unique to political contexts. To address these limitations, we developed a sentiment classifier specialized for political content.

The vocabulary used to train the model was extracted from a political text corpus comprising news articles, online comments, and party statements. Sentiment labels were manually annotated by undergraduate and graduate researchers affiliated with the QOD (Qualities of Democracy) Lab in the Department of Political Science and International Studies at Yonsei University. The final dataset includes 4,428 labeled words.

You can download the full model from [Hugging Face](https://huggingface.co/JiyoungP/QOD-Korean-Political-Sentiment-BERT).

## Authors

- Jiyoung Park (jypark0@utexas.edu)
- Sanghyun Park (shpark03@yonsei.ac.kr)    
- Eunmi Cho (eunmicho@yonsei.ac.kr)
- Minkyoung Jung (mk2561@gmail.com)
- Joohyun Jung (wjdwngus654@naver.com)
- Sinjae Kang (sinjae@yonsei.ac.kr)  
- Sunwoo Kwak (sunwookwak@gmail.com)  
- Jaewoo Lim (dlawodn10@yonsei.ac.kr)  

---
## Key Features

- Sentiment classification specialized for Korean political contexts

- Five sentiment classes: very negative, negative, neutral, positive, very positive

- Built on a pre-trained KoELECTRA backbone

---

## Training Details

- Data Collection Period: December 1, 2023 – December 31, 2023

- Data Sources: News articles, online comments, and official political party statements
  

### Morphological Analyzer Comparison

We evaluated five Korean morphological analyzers (OKT, Komoran, Kkma, UDPipe, Mecab) by analyzing word frequency distributions. Mecab was ultimately selected based on its superior performance for our use case.


### Sentiment Annotation Protocol

1. **Word Selection Criteria**: Adjectives, adverbs, nouns, and selected verbs

2. **Annotation Process**:
   - Each word was labeled by three independent annotators on a scale from -2 (strongly negative) to +2 (strongly positive)

   - If all three annotators agreed on the score → that score was finalized

   - If there was disagreement → the annotators discussed and included the word only upon reaching unanimous consensus

   - If no agreement was reached → the word was excluded from the training dataset

---

## Model Performance

| Metric     | Score   |
|------------|---------|
| Accuracy   | 0.7946  |
| Precision  | 0.5991  |
| Recall     | 0.5802  |
| F1 Score   | 0.5888  |

---

## Training Hyperparameters

- **Model**: `monologg/koelectra-base-v3-discriminator`  
- **Epochs**: 10  
- **Batch Size**: 8 (train & eval)  
- **Learning Rate**: 2e-5  
- **Weight Decay**: 0.01  
- **Max Length**: 16  
- **Evaluation Strategy**: per epoch  
- **Save Strategy**: per epoch  
- **Best Model Selection**: Enabled (`load_best_model_at_end=True`)  
- **Tokenizer**: KoELECTRA Tokenizer

---
## Usage

```python
from qod_kpsb import QODKPSBPredictor

predictor = QODKPSBPredictor()
print(predictor.predict("개검독재"))  # → very negative
```

---
## Citation
If you use this code or data in your work, please cite:

Jiyoung Park, Sanghyun Park, Cho, Eunmi, Minkyoung Jung, Joohyun Jung, Sinjae Kang, Sunwoo Kwak and Jaewoo Lim

"QOD_KPSB: Korean Political Sentiment BERT."
GitHub repository: https://github.com/jiyoung-park0/QOD_KPSB
