# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

Installed on Windows 11 as the global npm package `@github/copilot`, which reports the non-sensitive version string `GitHub Copilot CLI 1.0.83`. Authentication through the official GitHub browser login flow has not been completed yet, so nothing derived from a credential appears in this repository.

### Antigravity CLI

Installed on Windows 11 through winget as the package `Google.AntigravityCLI`, exposed as the command `agy`, which reports version `1.1.27`. Authentication through the official Google sign-in flow has not been completed yet, and no credential material is recorded anywhere in this journal.

## Shared task

### Shared prompt

```text
Write a Python function count_vowels(text: str) -> int that counts the vowels a, e, i, o, and u in text, ignoring case. Do not count the letter y. Return 0 for an empty string.
```

### Copilot CLI observations

This section is not complete yet, and I am recording that honestly rather than inventing a result. The tool is installed and its version is verified above, but I have not authenticated it, so the shared prompt has not been submitted to it. Once I sign in, I will record the approach it suggests, whether it iterates over characters or uses a membership test, what it assumes about case handling, and anything I would want to verify myself.

### Antigravity CLI observations

This section is likewise incomplete and stated honestly. Antigravity CLI is installed and its version is verified above, but authentication is still outstanding, so the shared prompt has not been submitted to it either. After signing in I will record its suggested approach for the same function, note any assumptions it makes about empty strings or non-alphabetic characters, and identify the parts of its answer that I would independently check.

### Comparison

I cannot yet compare two real responses, because neither command line agent has been authenticated and neither has received the shared prompt. Writing a fabricated comparison would defeat the purpose of this lab, which is to evaluate two tools against the same task and use evidence rather than trust to decide what enters the repository. What I can state is the standard I intend to apply when I do run the comparison. I will check correctness first, especially case insensitivity and the explicit exclusion of the letter y, since that is the requirement most likely to be handled incorrectly. I will then compare clarity, preferring an implementation a classmate could read without explanation. I will note unstated assumptions, such as behavior on digits, punctuation, or accented characters. Finally I will decide whether to take one answer, combine both, or reject both in favor of my own implementation, and I will record that decision here with the reasoning behind it.

## Test-guided implementation

The implementation in `week02/lab02.py` was checked against the provided grader rather than accepted on inspection alone. Running `uv run --directory week02 python -m pytest tests/ -v` executed the nine behavioral tests in `tests/test_lab02.py`, and all nine passed on the first attempt, so no revision was required. The tests that mattered most were the ones covering edge cases I might otherwise have missed. `make_greeting("")` must return `Hello, !`, which an f-string produces naturally without any guard against empty input. `is_even` must return `True` for both zero and negative even numbers, which the modulo comparison handles correctly because `-4 % 2` evaluates to zero in Python. `count_vowels("OpenAI")` must return four, confirming that lowercasing the text before testing membership is what makes the count case insensitive. `count_vowels("rhythms")` must return zero, which is the test that proves the letter y is genuinely excluded, since only the five vowels appear in the membership string.

## Preferred tool combination

A browser chat is where I go for open ended questions, because I can describe a problem loosely and read a longer explanation without touching my files. GitHub Copilot in VS Code fits a different moment: it suggests the next line while I am already typing, which is useful for repetitive code but easy to accept without reading carefully. Copilot CLI and Antigravity CLI sit closer to the repository itself, since launching them from the project directory lets them see real files and propose concrete edits, which is more powerful and therefore more important to review line by line before accepting anything. For the work in this course my current preference is VS Code as the editor with a browser chat alongside it for explanation, because I am still learning Python and I want to understand code before it reaches my repository. What would change that choice is scale. Once a task spans several files at once, retyping context into a browser window becomes the slow part, and a command line agent that already has repository access becomes clearly worth the extra care that reviewing its diffs requires.
