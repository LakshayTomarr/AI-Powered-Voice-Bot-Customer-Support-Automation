import torch
from transformers import BertTokenizer, BertForSequenceClassification
from app.config import settings

class IntentService:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(settings.INTENT_MODEL_PATH)
        self.model = BertForSequenceClassification.from_pretrained(settings.INTENT_MODEL_PATH)
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)
        confidence, predicted_class = torch.max(probs, dim=1)

        return predicted_class.item(), confidence.item()
