import argparse
import json

from cynbit_copilot import CopilotPipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    parser.add_argument("--name", default=None)
    args = parser.parse_args()
    result = CopilotPipeline().analyze(args.text, args.name)
    print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
