from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["svg.fonttype"] = "none"

ROOT = Path(__file__).resolve().parent
PLOTS = ROOT / "plots"
PLOTS.mkdir(parents=True, exist_ok=True)

def finish(fig, filename):
    fig.tight_layout()
    fig.savefig(PLOTS / filename, format="svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
