"""Plot a molecular-extension trace and summarize two threshold-defined groups.

This is a teaching example, not validated event detection or force calibration.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="CSV with time_s and extension_nm columns")
    parser.add_argument("--threshold-nm", type=float, required=True,
                        help="Illustrative threshold used to divide extension samples")
    args = parser.parse_args()

    data = pd.read_csv(args.csv)
    required = {"time_s", "extension_nm"}
    missing = required - set(data.columns)
    if missing:
        parser.error(f"CSV is missing required columns: {', '.join(sorted(missing))}")

    data = data.dropna(subset=["time_s", "extension_nm"]).sort_values("time_s")
    if data.empty:
        parser.error("CSV has no valid time_s/extension_nm rows")

    low = data.loc[data["extension_nm"] < args.threshold_nm, "extension_nm"]
    high = data.loc[data["extension_nm"] >= args.threshold_nm, "extension_nm"]
    print(f"Samples: {len(data)}")
    print(f"Mean extension: {data['extension_nm'].mean():.3f} nm")
    if low.empty or high.empty:
        print("Threshold summary: threshold did not divide samples into two non-empty groups")
    else:
        delta = high.mean() - low.mean()
        print(f"Difference of group means (high - low): {delta:.3f} nm")
        print("Caution: this is not a fitted molecular transition size.")

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(data["time_s"], data["extension_nm"], lw=0.8, color="#245b78")
    ax.axhline(args.threshold_nm, ls="--", lw=1, color="#c87932", label="Illustrative threshold")
    ax.set(xlabel="Time (s)", ylabel="Extension (nm)", title=args.csv.name)
    ax.legend(frameon=False)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
