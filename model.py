
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
import pandas as pd
from datasets import Dataset
df = pd.read_csv("stutter_text_dataset.csv")
dataset = Dataset.from_pandas(df)
dataset = dataset.train_test_split(test_size=0.2)
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
def preprocess_data(examples):
    inputs = [ex for ex in examples["stuttered_text"]]
    targets = [ex for ex in examples["normal_text"]]
    model_inputs = tokenizer(inputs, padding="max_length", truncation=True, max_length=128)
    labels = tokenizer(targets, padding="max_length", truncation=True, max_length=128).input_ids
    model_inputs["labels"] = labels
    return model_inputs

tokenized_datasets = dataset.map(preprocess_data, batched=True)
training_args = TrainingArguments(
    output_dir="./stutter_model",
    eval_strategy="epoch",
    learning_rate=3e-4,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=5,
    weight_decay=0.01,
    save_total_limit=1,
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

trainer.train()
trainer.save_model("./stutter_model")
tokenizer.save_pretrained("./stutter_model")
