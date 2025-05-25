# QOD_KPSB (QOD-Korean Political Sentiment BERT)

QOD_KPSB is a sentiment classification model tailored for Korean political discourse.
Fine-tuned from the KoELECTRA architecture, this model is designed to automatically predict the sentiment of key political terms found in news articles, comments, and official party statements.

In many Korean political science studies, general-purpose sentiment lexicons or BERT models have traditionally been used to measure sentiment. However, such tools often fall short when applied to political texts, which frequently include domain-specific terminology, references to particular events or ideologies, slang, and neologisms unique to political contexts. To address these limitations, we developed a sentiment classifier specialized for political content.

The vocabulary used to train the model was extracted from a political text corpus comprising news articles, online comments, and party statements. Sentiment labels were manually annotated by undergraduate and graduate researchers affiliated with the QOD (Qualities of Democracy) Lab in the Department of Political Science and International Studies at Yonsei University. The final dataset includes 4,428 labeled words.

## Key Features

- Sentiment classification specialized for Korean political contexts

- Five sentiment classes: very negative, negative, neutral, positive, very positive

- Built on a pre-trained KoELECTRA backbone

---

## Training Details

- Training Period: January 6, 2024 – May 25, 2024

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

