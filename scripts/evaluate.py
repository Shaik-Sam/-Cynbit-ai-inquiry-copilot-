import json

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score

from cynbit_copilot import config
from cynbit_copilot.pipeline import ensure_model


def main():
    df = pd.read_csv(config.DATA_DIR / "handwritten_eval.csv")
    clf = ensure_model()
    preds = [clf.predict(t)[0] for t in df["text"]]
    result = {
        "n": int(len(df)),
        "accuracy": float(accuracy_score(df["label"], preds)),
        "macro_f1": float(f1_score(df["label"], preds, average="macro")),
        "report": classification_report(df["label"], preds, output_dict=True, zero_division=0),
        "errors": [
            {"text": t, "expected": y, "predicted": p}
            for t, y, p in zip(df["text"], df["label"], preds)
            if y != p
        ],
    }
    config.REPORT_DIR.mkdir(parents=True, exist_ok=True)
    with open(config.REPORT_DIR / "handwritten_eval.json", "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2)
    print(f"n: {result['n']}")
    print(f"accuracy: {result['accuracy']:.4f}")
    print(f"macro_f1: {result['macro_f1']:.4f}")
    for err in result["errors"]:
        print(f"- {err['expected']} -> {err['predicted']}: {err['text']}")


if __name__ == "__main__":
    main()
