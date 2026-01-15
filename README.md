# pkoffee

**Analysis for the paper:** _Quantifying the Relationship Between Coffee Consumption and Developer Productivity: An Observational Study_ by Jean Dupont, 2025

**Project inspired by:** _Le Café - Oldelaf_ for the S3 School 2026.

[![Le Café - Oldelaf - on YouTube](http://img.youtube.com/vi/UGtKGX8B9hU/0.jpg)](http://www.youtube.com/watch?v=UGtKGX8B9hU "Le Café - Oldelaf")

---

## Overview

This project performs statistical analysis to quantify the relationship between coffee consumption and developer productivity. The analysis fits multiple mathematical models (quadratic, saturating, logistic, and peak models) to observational data and evaluates their goodness-of-fit using R² metrics.

---

## Requirements

### System Requirements
- **Operating System**: Linux (64-bit, ARM64), macOS (Intel, Apple Silicon), or Windows (64-bit)
- **Python**: 3.14.2 or higher (but < 3.15)
- **Pixi**: Package manager for environment management ([Install Pixi](https://pixi.sh/))

### Software Dependencies
All dependencies are managed automatically via Pixi. See [Dependencies](#dependencies) section for details.

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd pkoffee
```

### 2. Install Pixi (if not already installed)

**Linux/macOS:**
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows:**
```powershell
iwr https://pixi.sh/install.ps1 -useb | iex
```

### 3. Set Up the Environment

The project uses Pixi for dependency management. The `pixi.lock` file ensures exact reproducibility:

```bash
pixi install
```

This command will:
- Create an isolated environment
- Install all dependencies with exact versions specified in `pixi.lock`

### 4. Verify Installation

```bash
pixi run python --version
pixi run python -c "import numpy, pandas, matplotlib, scipy, seaborn; print('All dependencies installed successfully!')"
```

---

## Usage

### Running the Analysis

1. **Ensure data file is available**: Place `coffee_productivity.csv` in the `src/pkoffee/` directory (see [Data Requirements](#data-requirements))

2. **Run the main analysis script**:

```bash
cd src/pkoffee
pixi run python main.py
```

Or from the project root:

```bash
pixi run python src/pkoffee/main.py
```

### Expected Output

The script will:
- Load the coffee productivity data
- Fit five mathematical models to the data
- Generate a visualization (`fit_plot.png`) showing:
  - Violin plots of productivity distribution by coffee consumption
  - Overlaid model fits with R² values
- Display the plot interactively
- Save the plot to `src/pkoffee/fit_plot.png`

### Output File

- **`fit_plot.png`**: Visualization with violin plots and model fits (saved in `src/pkoffee/`)

---

## Reproducing Results

To reproduce the exact results from the publication:

1. **Clone the repository** (or download the tagged version):
   ```bash
   git clone <repository-url>
   cd pkoffee
   git checkout <publication-tag>  # Use the tag for the publication version
   ```

2. **Install exact dependencies**:
   ```bash
   pixi install
   ```
   The `pixi.lock` file ensures you get the exact same package versions.

3. **Obtain the data file**: Ensure `coffee_productivity.csv` is in `data/` directory

4. **Run the analysis**:
   ```bash
   cd src/pkoffee
   pixi run python main.py
   ```

5. **Verify output**: Compare the generated `fit_plot.png` with published results

---

## Project Structure

```
pkoffee/
├── README.md                 # This file
├── pixi.toml                # Dependency configuration
├── pixi.lock                # Exact dependency versions (CRITICAL for reproducibility)
├── .gitignore              # Git ignore rules
├── .gitattributes          # Git attributes
└── src/
    └── pkoffee/
        ├── __init__.py     # Package initialization
        ├── main.py         # Main analysis script
        └── fit_plot.png    # Generated output (not in version control)
```

---

## Dependencies

### Core Scientific Libraries

| Package | Version Range | Purpose |
|---------|---------------|---------|
| Python | >=3.14.2,<3.15 | Programming language |
| NumPy | >=2.4.1,<3 | Numerical computations |
| Pandas | >=2.3.3,<3 | Data manipulation and CSV reading |
| Matplotlib | >=3.10.8,<4 | Plotting and visualization |
| SciPy | >=1.17.0,<2 | Scientific computing (curve fitting) |
| Seaborn | >=0.13.2,<0.14 | Statistical visualization (violin plots) |

### Dependency Sources

- All packages are sourced from **conda-forge** channel
- Exact versions are locked in `pixi.lock` for reproducibility

### Viewing Dependencies

```bash
pixi info
```

---

## Platform Support

This project is tested and supported on:

- ✅ **Linux**: 64-bit (x86_64) and ARM64 (aarch64)
- ✅ **macOS**: Intel (x86_64) and Apple Silicon (ARM64)
- ✅ **Windows**: 64-bit

Platform-specific configurations are handled automatically by Pixi based on the `platforms` specification in `pixi.toml`.

---

## Data Requirements

### Input Data File

The analysis requires a CSV file named `coffee_productivity.csv` located in `data/` directory.

### Expected Data Format

The CSV file should contain at least two columns:
- **`cups`**: Number of coffee cups consumed (numeric)
- **`productivity`**: Developer productivity metric (numeric)

Example format:
```csv
cups,productivity
0,2.5
1,3.2
2,4.1
...
```