# parameter_gen

Utilities for generating LAMMPS/mDPD input settings and extracting simulation outputs.

## Workflow (recommended)

1. Create input LAMMPS scripts/settings with `createatoms.py`.
2. Run LAMMPS jobs with `lammps_day.sh`.
3. After runs finish, extract outputs with `logextract.py`, `paramextract.py` and `combine.sh`.

## Python scripts

- `createatoms.py`  
  Main input generator. Randomly creates system composition and writes `createatoms.settings` and `createbonds.settings`. It also calls `polydata.py` (for polymer data when needed) and `paramgen.py` (for force-field parameters).

- `paramgen.py`  
  Generates pair and bond coefficients and writes them to `parameters.settings`.

- `polydata.py`  
  Builds polymer bead coordinates/bonds and writes `polymer.data` used by `createatoms.py`.

- `logextract.py`  
  Parses per-run `log1.out` files (e.g., `run1901` to `run2300`) to compute normalized species concentrations and writes `Conc.txt` in each run directory.

- `paramextract.py`  
  Reads `parameters.settings`, extracts key interaction/bond/SRP parameters, and writes a feature row to `Xdata1.txt`.

- `DataExtract.py`  
  Aggregates valid rows from each run’s `Finaldata.txt` into `Batch9data.txt`.

