---
name: add-leetcode-problem
description: Add a verified LeetCode problem and Python solution to the matching topic folder in this repository. Use when asked to create a solution from a LeetCode problem name, number, or link.
argument-hint: "<problem name> -n <problem number>"
disable-model-invocation: true
---

# Add a LeetCode problem

When invoked with a problem name and `-n` problem number (for example, `/add-leetcode-problem Kth Largest Element in an Array -n 215`), add one Python file for that problem to this repository.

## Verify the problem

1. Parse the supplied title and number. If either is missing, ask for it.
2. Find the problem on LeetCode's official site using its available browser, web search, or fetch tools. Verify that the official problem number and title agree with the request. If they do not, report the discrepancy and ask which problem to use.
3. Use the official page as the source for the canonical problem URL, a concise summary, and the sample input/output pairs. Do not invent missing details or use an unofficial mirror to fill gaps. If you cannot access or verify the official page, stop before writing a file and explain why.
4. Do not copy the full problem statement, constraints, or explanatory prose verbatim. Write a brief original summary in your own words. Sample input/output values may be recorded accurately and concisely.

## Choose the destination

1. Inspect the repository's existing topic folders and nearby Python solutions. Choose the most appropriate existing folder based on the problem's primary data structure or algorithm, following local naming conventions.
2. If no existing folder is a reasonable fit, ask before creating a new topic folder.
3. Name the file `<official problem title>.py`. Check for an existing file or solution for the same problem number before writing. Never overwrite or replace an existing solution without explicit permission.

## Create the solution

Follow the style of nearby files. Include:

- A comment header with the verified problem number, official title, canonical LeetCode URL, and a concise original problem summary.
- Each verified official sample as concise commented input and output lines; do not reproduce the sample explanations.
- A correct, idiomatic Python solution using the interface expected by LeetCode, with only necessary imports and comments.

Preserve sample values exactly. Do not claim a solution was tested unless you actually ran an appropriate check. After creating the file, report its path, the algorithm in one sentence, and any validation performed.
