# qod_kpsb/predictor.py
import torch
from transformers import ElectraTokenizer, ElectraForSequenceClassification

class QODKPSBPredictor:
    def __init__(self):
        self.label_map_inv = {
            0: "very negative",
            1: "negative",
            2: "neutral",
            3: "positive",
            4: "very positive"
        }

        model_path = f"{__package__}/model"
        self.tokenizer = ElectraTokenizer.from_pretrained(model_path)
        self.model = ElectraForSequenceClassification.from_pretrained(model_path)
        self.device = torch.device("mps" if torch.backends.mps.is_available() else
                                   "cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=16)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(**inputs)
            pred = torch.argmax(outputs.logits, dim=1).item()
        return self.label_map_inv[pred]
