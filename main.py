import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from flask import Flask, request, jsonify

import torch
from transformers import AutoTokenizer, pipeline

model_path = "models/transformers/"

model = pipeline(
    model="h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3",
    tokenizer=AutoTokenizer.from_pretrained(
        "h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3",
        use_fast=False,
        padding_side="left",
        trust_remote_code=True),
    torch_dtype=torch.float16,
    trust_remote_code=True,
    use_fast=False,
    device_map={"": "cuda:0"},
)
model.save_pretrained(model_path)


def answer_text(text):
    res = model(
        text,
        min_new_tokens=2,
        max_new_tokens=1024,
        do_sample=False,
        num_beams=1,
        temperature=float(0.3),
        repetition_penalty=float(1.2),
        renormalize_logits=True
    )
    return res[0]["generated_text"]


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.files.get('text')
        if text is None:
            return jsonify({"error": "text"})
        try:
            data = {"answer": answer_text(text)}
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
