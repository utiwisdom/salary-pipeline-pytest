# Salary Data Pipeline: Automated Quality Gates with pytest

## Project Overview

This project builds an automated test suite around a small pandas pipeline that
summarises data science salaries by year. The suite acts as a quality gate: the
pipeline should only be deployed if every test passes.

Four test layers are used, each catching a different kind of failure:
- **Integration** - can the pipeline read its data from the file system?
- **Unit** - is the smallest calculation correct and free of nulls?
- **Feature** - does the user get a sensible final answer?
- **Performance** - is the pipeline fast enough?

### Business Question
> Before this pipeline goes live, can we prove that it loads real data, produces
> clean statistics, returns a sensible answer, and runs fast enough?

### Why This Matters
HR teams and analysts use salary benchmarks to set pay bands and make job
offers. A missing file, null statistics or a silent slowdown can produce wrong
numbers without anyone noticing. Automated tests turn those risks into checks
that run in seconds every time the code changes.

---

## Dataset

- **File:** `data/salaries.csv`
- **Source:** [Data Science Job Salaries (Kaggle, ruchi798)](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)
- **Key columns used:** `work_year`, `salary`

---

## Tools Used

- **Python 3.8** and **pandas** - the pipeline
- **pytest** - test framework
- **pytest-benchmark** - performance measurement
- **WSL (Ubuntu)**, **VS Code**, **Git/GitHub**

---

## The Pipeline

`src/pipeline.py` has two functions:
- `read_data()` loads the CSV into a DataFrame.
- `get_grouped()` groups salaries by `work_year` and returns summary statistics
  (count, mean, std, min, quartiles, max) for each year.

Run `python3 -m src.pipeline` to print the yearly summary and the 2022 median.

---

## What Is Tested

| Layer | What it checks | Why it matters |
|---|---|---|
| Integration | The CSV loads into a DataFrame that has rows | Catches missing or empty source files |
| Unit | The yearly salary summary contains no nulls | Stops bad statistics reaching reports |
| Feature | The 2022 median salary is a float greater than 0 | Confirms users get a sensible answer |
| Performance | Benchmarks the grouping step | Gives a speed baseline so slowdowns become visible |

---

## Results

    4 passed

Benchmark on my machine (WSL2, Ubuntu 20.04): about **12.8 ms** mean per run,
roughly **78 runs per second**. Numbers vary by machine and between runs, so
treat them as a baseline to compare against, not a fixed target.

---

## Key Takeaways

- Each layer catches a different failure type, so one passing test does not
  replace the others.
- The benchmark gives a measured baseline. Without one, "it feels slower" cannot
  be proven.
- **Limitation 1:** by default `pytest-benchmark` only reports speed, it does not
  fail on a slowdown. A next step is to save this run as a baseline and fail the
  build if the mean gets more than 20% slower, using
  `--benchmark-autosave` and `--benchmark-compare-fail=mean:20%`.
- **Limitation 2:** the `salary` column mixes currencies (for example EUR and
  USD), so a median over it is not directly comparable across rows. A production
  version should summarise `salary_in_usd` instead, and add a test that
  enforces a single currency.

---

## How to Run This Project

1. Clone the repository
2. Create and activate an environment, then install the requirements
3. Run the tests

        git clone https://github.com/utiwisdom/salary-pipeline-pytest.git
        cd salary-pipeline-pytest
        python3 -m venv .venv && source .venv/bin/activate
        pip install -r requirements.txt
        pytest -v

---

## Repository Structure

    salary-pipeline-pytest/
    ├── data/
    │   └── salaries.csv
    ├── src/
    │   └── pipeline.py
    ├── tests/
    │   ├── conftest.py
    │   ├── test_integration.py
    │   ├── test_unit.py
    │   ├── test_feature.py
    │   └── test_performance.py
    ├── pytest.ini
    ├── requirements.txt
    └── README.md

---

## Author

**Wisdom Uti**
ALX Data Engineering Graduate | Data Science Volunteer Mentor
[LinkedIn](https://linkedin.com/in/uti-wisdom-286602228/) · [GitHub](https://github.com/utiwisdom)