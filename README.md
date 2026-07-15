# WebTests (Python)

Python port of the C# `PlaywrightTestExamples` project — the same UI automation
suite against http://uitestingplayground.com/, built with `pytest` and
`pytest-playwright`.

## How to launch

1. Create and activate a virtual environment (recommended):

   ```
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:

   ```
   playwright install
   ```

4. Run the tests:

   ```
   pytest
   ```

## Configuration

Runtime parameters mirror `live.runsettings` and can be supplied via
environment variables or command-line options (defaults shown):

| Env var          | CLI option          | Default                          |
|-------------------|---------------------|-----------------------------------|
| `ENVIRONMENT`     | -                    | `http://uitestingplayground.com/` |
| `LOGIN`           | `--login`            | `Viktor`                          |
| `PASSWORD`        | `--password`         | `pwd`                             |
| `WRONG_PASSWORD`  | `--wrong-password`   | `pwd123`                          |
| `HEADLESS`        | -                    | `false`                           |

Examples:

```
ENVIRONMENT=http://uitestingplayground.com/ pytest
pytest --login=Viktor --password=pwd --wrong-password=pwd123
HEADLESS=true pytest
```

## Project layout

- `pages/` — Page Object Model classes (mirrors the C# `Pages/` folder).
- `tests/` — Test modules (mirrors the C# `Tests/` folder).
- `conftest.py` — Root fixtures playing the role of the C# `BaseTest` class
  (`load_main_page`, `load_page`) plus the run parameters
  (`login`, `password`, `wrong_password`, `base_url`).
- `resources/` — Test data (`file.txt` used by the file upload test).
