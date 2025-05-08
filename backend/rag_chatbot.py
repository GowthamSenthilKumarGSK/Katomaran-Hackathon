from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

class RAGChatbot:
    def __init__(self):
        self.tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
        self.retriever = RagRetriever.from_pretrained("facebook/rag-token-nq")
        self.model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq")

    def chat(self, query):
        input_ids = self.tokenizer(query, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids=input_ids, num_beams=4, min_length=50, max_length=150)
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer
