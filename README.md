# GitHub Actions — Lesson 1

<!-- STEP 6: paste your status badge on the line below -->

This repository is a hands-on introduction to **GitHub Actions**: GitHub's built-in tool for running tasks automatically when something happens in your repository.

The "app" here is a tiny Python calculator (`app/calculator.py`) with a few tests (`tests/test_calculator.py`). The code is simple on purpose. Today's lesson is about the **automation around the code**.

---

## The big idea

> Every time you commit a change, GitHub borrows a fresh computer, downloads your code onto it, runs the commands you wrote, and shows you a ✅ or a ❌.

You describe *what to run* and *when to run it* in a YAML file inside `.github/workflows/`.

## Six words to remember

| Word | What it means | In the YAML |
|---|---|---|
| **Workflow** | An automated process. One YAML file = one workflow. | the whole file in `.github/workflows/` |
| **Event** | What *starts* the workflow (a push, a pull request, a button click…). | `on:` |
| **Job** | A group of steps that run together on one machine. | `jobs:` |
| **Runner** | The machine that runs a job. GitHub gives you a fresh one every time. | `runs-on:` |
| **Step** | One task inside a job — a shell command or an action. | `steps:` |
| **Action** | A ready-made, reusable step that someone else wrote. | `uses:` |

## Anatomy of a workflow

```
Workflow  (.github/workflows/ci.yml)
│
├── on: push                     ← EVENT: when to run
│
└── jobs:
    └── test:                    ← JOB
        ├── runs-on: ubuntu-latest   ← RUNNER: where to run
        └── steps:                   ← STEPS: what to run, in order
            ├── uses: actions/checkout@v7      ← an ACTION
            ├── uses: actions/setup-python@v7  ← an ACTION
            ├── run: pip install -r requirements.txt
            └── run: pytest -v                 ← a shell command
```

---

## The lesson, step by step

All workflow files are ready in the `lesson-steps/` folder. Each step copies one of them into `.github/workflows/` and commits it. Everything happens on github.com — no terminal needed.

| Step | What you learn | File | Copy to |
|---|---|---|---|
| 1 | Your first workflow | `01_hello.yml` | `.github/workflows/hello.yml` |
| 2 | Contexts, many steps, a "Run workflow" button — and an empty runner! | `02_hello_explore.yml` | `.github/workflows/hello.yml` (replace) |
| 3 | Real CI: check out code and run tests | `03_ci.yml` | `.github/workflows/ci.yml` |
| 4 | Break the build on purpose ❌ | *(edit `app/calculator.py`)* | — |
| 5 | Fix the build ✅ | *(edit `app/calculator.py`)* | — |
| 6 | Add a status badge to this README | *(edit `README.md`)* | — |
| 7 ⭐ | Bonus: test on 6 setups at once with a matrix | `07_ci_matrix.yml` | `.github/workflows/ci.yml` (replace) |
| 8 ⭐ | Bonus: manual workflow with a form, and two jobs | `08_greet.yml` | `.github/workflows/greet.yml` |

### Two moves you will repeat

- **Copy a lesson file:** open the `lesson-steps` folder, click the file, then click the **Copy raw file** button (the copy icon at the top right of the file view).
- **Commit:** click the green **Commit changes…** button, keep **Commit directly to the main branch** selected, and click **Commit changes**. Every commit triggers the `push` event.

### Step 1 — Your first workflow

1. Copy `lesson-steps/01_hello.yml`.
2. Click the **Actions** tab, then **set up a workflow yourself**.
3. Change the file name from `main.yml` to `hello.yml`.
4. Delete anything already in the editor, paste, and commit.
5. Open the **Actions** tab and click the new run → the `say-hello` job → the **Say hello** step.

### Step 2 — Explore the runner

1. Copy `lesson-steps/02_hello_explore.yml`.
2. Open `.github/workflows/hello.yml` and click the ✏️ pencil icon (**Edit this file**).
3. Select all (Ctrl+A, or Cmd+A on a Mac), paste over it, and commit.
4. Open the run and expand every step. What does **Where is my code?** show?
5. Try the button: **Actions → Hello World → Run workflow → Run workflow**.

### Step 3 — Run the tests automatically

1. Copy `lesson-steps/03_ci.yml`.
2. On the **Code** tab, click **Add file → Create new file**.
3. Type `.github/workflows/ci.yml` as the name (each `/` creates a folder), paste, and commit.
4. In the **Actions** tab, open the **CI** run and expand **Run the tests**.

### Step 4 — Break the build

In the browser, open `app/calculator.py`, click the ✏️ pencil icon, and change the `add` function:

```python
return a + b      # before
return a - b      # after (a bug!)
```

Commit. Open the **Actions** tab and watch the **CI** run turn red ❌. Click into it and find the failing test in the log.

### Step 5 — Fix it

Change it back to `return a + b` and commit. The next run turns green ✅.

### Step 6 — Add a badge

Go to **Actions → CI → ⋯ (top right) → Create status badge**, copy the Markdown, and paste it at the top of this README. Or write it yourself:

```markdown
![CI](https://github.com/YOUR-USERNAME/YOUR-REPO/actions/workflows/ci.yml/badge.svg)
```

### Bonus Step 7 — Matrix

Copy `lesson-steps/07_ci_matrix.yml`, open `.github/workflows/ci.yml`, click the ✏️ pencil icon, select all, paste, and commit. Watch six jobs run at once.

### Bonus Step 8 — Manual workflow with a form

Copy `lesson-steps/08_greet.yml`, click **Add file → Create new file**, name it `.github/workflows/greet.yml`, paste, and commit. Then go to **Actions → Greet the class → Run workflow**, type your name, and run it.

---

## Following along with your own copy?

Click **Use this template → Create a new repository** at the top of this repository's page (if your instructor turned that on), or **Fork** it.

If you **fork**, GitHub turns Actions **off** in the fork for safety. Open the **Actions** tab and click **"I understand my workflows, go ahead and enable them."**

## Practice at home

1. Add a `power(a, b)` function to `app/calculator.py` and a test for it in `tests/test_calculator.py`. Commit. Is it green?
2. Write a test that you *know* will fail. Commit. Read the log. Then fix it.
3. Add a step to `hello.yml` that prints your favourite quote.
4. Change `on: push` in `hello.yml` so it runs only on the `main` branch. (Hint: `branches:`.)

## Learn more

- GitHub Docs — Understanding GitHub Actions: https://docs.github.com/en/actions/get-started/understand-github-actions
- GitHub Docs — Workflow syntax: https://docs.github.com/actions/writing-workflows/workflow-syntax-for-github-actions
- GitHub Marketplace (ready-made actions): https://github.com/marketplace?type=actions
