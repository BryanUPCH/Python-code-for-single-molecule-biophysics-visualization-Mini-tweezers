# Mini-tweezers: single-molecule data visualization (starter)

An initial, deliberately small proposal for documenting Python visualization of optical-tweezers traces. This repository is a starting point, not a claim that the example reproduces a validated instrument pipeline.

## What is included

- A minimal CSV-to-plot analysis for molecular extension versus time.
- A synthetic example trace so the script can be run without experimental files.
- Explicit notes distinguishing remembered workflow context from assumptions.

## Inferred context and assumptions

### Inferred from the project context

- The project concerns single-molecule force spectroscopy with optical tweezers.
- Relevant concepts include force–extension traces, extension changes (Δx), force ramps or constant-force measurements, and possible folding/unfolding transitions.
- Python is part of the user's scientific computing workflow.

### Assumptions made for this starter

- Input data can be represented as a CSV with columns `time_s` and `extension_nm`.
- The example treats extension as already calibrated and does not infer force from trap displacement.
- State assignment uses a user-specified threshold. This is a visualization demo, not validated event detection.
- The synthetic data and its numerical values are illustrative only, not experimental measurements or a claimed protein-specific Δx.
- Dependencies are limited to NumPy, pandas, and Matplotlib. No instrument SDK or proprietary file format is assumed.

Replace these assumptions when actual instrument exports, calibration conventions, and analysis decisions are available.

## Repository layout

```text
.
├── README.md
├── requirements.txt
├── data/
│   └── example_trace.csv
└── src/
    └── analyze_trace.py
```

## Requirements

Python 3.10 or newer is assumed. Install the small dependency set in a virtual environment:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the example

From the repository root:

```bash
python src/analyze_trace.py data/example_trace.csv --threshold-nm 20
```

The script plots extension versus time, marks the threshold, and prints the mean extension and the difference between samples below and above the threshold. That difference is only a simple two-bin summary; it is not a fitted transition size unless the threshold and states are independently justified.

For your own CSV:

```bash
python src/analyze_trace.py path/to/trace.csv --threshold-nm YOUR_THRESHOLD
```

Required columns: `time_s`, `extension_nm`. Units must be seconds and nanometres. Keep the original data and record any preprocessing separately.

## Scope and next steps

This starter does not perform bead/trap calibration, force reconstruction, drift correction, filtering, hidden-state inference, WLC fitting, force-dependent kinetics, or Jarzynski/Crooks analysis. Those require the actual instrument data format and documented experimental choices. A next version can add them one at a time with representative data and checks.

## License

No license has been selected yet. Add one before inviting reuse or redistribution.
