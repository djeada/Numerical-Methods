from pathlib import Path
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.fonttype"] = "none"
import matplotlib.pyplot as plt

PLOTS = Path(__file__).resolve().parent / "plots"
PLOTS.mkdir(parents=True, exist_ok=True)

def finish(fig, filename):
    fig.tight_layout()
    fig.savefig(PLOTS / filename, format="svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
