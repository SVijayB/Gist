import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import re


def title_generation(data):
    print("[!] Server logs: Title generation has started")
    try:
       text = data["article"]
    except KeyError as k:
        text = data['text']
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = T5ForConditionalGeneration.from_pretrained(
        "Michau/t5-base-en-generate-headline"
    )
    tokenizer = T5Tokenizer.from_pretrained("Michau/t5-base-en-generate-headline")
    model = model.to(device)
    encoding = tokenizer.encode_plus(text, return_tensors="pt")
    input_ids = encoding["input_ids"].to(device)
    attention_masks = encoding["attention_mask"].to(device)

    beam_outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_masks,
        max_length=64,
        num_beams=3,
        early_stopping=True,
    )

    result = tokenizer.decode(beam_outputs[0])
    print("[!] Server logs: Title generation completed")

    regex_pattern = r"(?<=<pad> )(.*)(?=</s>)"
    result = re.search(regex_pattern, result).group(0)
    data["title"] = result
    return data
