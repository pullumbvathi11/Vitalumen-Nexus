from modules.core import VitaLumenCore

def run_platform():
    core = VitaLumenCore()
    print(core.status())

    sample_data = ["market signals", "social trends", "crypto flow"]
    results = core.feed(sample_data)

    opportunities = core.generate_opportunities()

    print("Analysis:", results)
    print("Opportunities:", opportunities)

if __name__ == "__main__":
    run_platform()
