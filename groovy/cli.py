import sys

from groovy.flow import Flow


def run_default_flow(task: str) -> None:
    flow = Flow(task)
    flow.launch(run_immediately=True)


def main():
    if len(sys.argv) < 2:
        print("Usage: groovy <task>")
        sys.exit(1)

    task = " ".join(sys.argv[1:])
    result = run_default_flow(task)
    print(result)


if __name__ == "__main__":
    main()
