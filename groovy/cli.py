import sys

from groovy.flow import Flow


def run_default_flow(prompt: str) -> None:
    flow = Flow(prompt, _run_immediately=True)
    flow.launch()


def main():
    if len(sys.argv) < 2:
        print("Usage: groovy <command>")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    result = run_default_flow(prompt)
    print(result)


if __name__ == "__main__":
    main()
