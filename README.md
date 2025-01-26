https://adventofcode.com/

# CLI setup

Generate a virtual environment

```
python3 -m venv .venv
```

Activate the virtual environment

```
source .venv/bin/activate
```

Install requirements

```
pip install -r requirements.txt
```

# Workflow

Each language has a `template` directory that contains a `cookiecutter` template to generate new projects for each day.

All of the following need to have the virtual environment from above active.

```
source .venv/bin/activate
```

Start by generating a new project for the day

```bash
./../../cli.py gen-day -d 1
```

Enter the created project

```bash
cd day01
```

Generate the `input.txt`

```bash
./../../../cli.py gen-input -s "YOUR_AOC_SESSION"
```

Generate the `README.md`

```bash
./../../../cli.py gen-input -s "YOUR_AOC_SESSION"
```

This will generate the README from what you can see on the AOC site. You will need to call this again once you solve the first part to update the README file with the part 2 text.
