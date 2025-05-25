# QOD_KPSB (QOD-Korean Political Sentiment BERT)

**QOD_KPSB**는 한국어 정치 담론을 위한 감성 분류 모델입니다.  
본 모델은 KoELECTRA를 기반으로 파인튜닝 되었으며, 정치 기사, 댓글, 정당 보도자료 등에서 사용되는 주요 단어의 감성을 자동으로 예측하도록 설계되었습니다.

기존의 한국 정치학 연구에서는 범용 감성 사전 또는 범용 BERT 모델을 활용해 감성을 측정해 왔습니다. 하지만 정치학과 같은 특수 분야에서는 전문 용어, 사건/인물/이념과 관련된 신조어 및 속어가 많아, 일반 모델만으로는 이러한 맥락을 충분히 반영하기 어렵습니다. 이러한 한계를 극복하기 위해 본 프로젝트는 정치 담론에 특화된 감성 분류 모델을 개발하였습니다.

모델 학습에 사용된 단어는 정치 관련 코퍼스(기사, 댓글, 보도자료 등)에서 수집되었으며, 연세대학교 정치외교학과의 QOD(Qualities of Democracy) Lab 소속 학부생 및 대학원생들이 직접 감성 라벨링을 진행했습니다. 최종 데이터셋은 총 4,428개의 단어로 구성되어 있습니다.

전체 모델은 [Hugging Face](https://huggingface.co/JiyoungP/QOD-Korean-Political-Sentiment-BERT)에서 다운로드하실 수 있습니다.

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
## 주요 기능

- 한국 정치 문맥에 맞춘 감성 분류
- 5개 감성 클래스 지원: `very negative`, `negative`, `neutral`, `positive`, `very positive`
- 사전 학습된 KoELECTRA 모델 기반

---

## 모델 학습 정보

- **학습 기간**: 2024년 1월 6일 ~ 2024년 5월 25일
- **수집 기간**: 2023년 12월 1일 ~ 12월 31일
- **데이터 출처**: 뉴스 기사, 기사 댓글, 정당 보도 자료

### 형태소 분석기 비교

총 5개의 형태소 분석기(OKT, Komoran, Kkma, UDPipe, Mecab)를 비교하여 단어 빈도수 분석을 진행하였으며, 최종적으로 **Mecab**이 가장 적합하다는 판단 하에 사용하였습니다.

### 감성 점수 부여 방법

1. **단어 추출 기준**: 형용사, 부사, 명사, 일부 동사
2. **감성 부여 방식**:
   - 각 단어에 대해 세 명의 평가자가 `-2(부정)` ~ `+2(긍정)`로 감성 점수 부여
   - **세 명 모두 감정 일치 시** → 해당 점수를 최종 감성으로 채택
   - **불일치 시** → 토론을 통해 만장일치한 경우만 채택
   - **합의 실패 시** → 해당 단어는 학습 데이터에서 제외

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

