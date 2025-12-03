from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("./stutter_model")
model = T5ForConditionalGeneration.from_pretrained("./stutter_model")

text = "I-I w-want t-to g-go t-to school."
input_ids = tokenizer(text, return_tensors="pt").input_ids
output = model.generate(input_ids, max_length=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))
