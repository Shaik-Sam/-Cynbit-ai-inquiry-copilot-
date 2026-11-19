import json

from cynbit_copilot import config
from cynbit_copilot.classifier import train_and_evaluate
from cynbit_copilot.data_gen import write_dataset


def main():
    df = write_dataset()
    clf, metrics = train_and_evaluate(df)
    clf.save()
    config.REPORT_DIR.mkdir(parents=True, exist_ok=True)
    with open(config.METRICS_PATH, "w", encoding="utf-8") as handle:
        json.dump(metrics, handle, indent=2)
    print(f"samples: {len(df)}")
    print(f"accuracy: {metrics['accuracy']:.4f}")
    print(f"macro_f1: {metrics['macro_f1']:.4f}")
    print(f"model saved to {config.MODEL_PATH}")


if __name__ == "__main__":
    main()
