import sys
from groovy.agent import agent_runner
from groovy.flow import Flow


def run_default_flow(prompt: str) -> None:
    flow = Flow(prompt)
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