from .integration import NexusIntegration

class NexusBoot:
    def __init__(self):
        self.system = NexusIntegration()

    def start(self):
        status = self.system.status()
        print("🚀 VitaLumen Nexus is Booting...")
        print("🌐 System Status:", status)
        return status

# Launch command (simbolik – ndezje)
def launch():
    nexus = NexusBoot()
    return nexus.start()
