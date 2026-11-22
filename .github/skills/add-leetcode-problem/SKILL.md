---
name: add-leetcode-problem
description: Add a verified, comment-only LeetCode problem reference file to the matching topic folder in this repository. Use when asked to create a problem file from a LeetCode problem name, number, or link.
argument-hint: "<problem name> -n <problem number>"
disable-model-invocation: true
---

# Add a LeetCode problem

When invoked with a problem name and `-n` problem number (for example, `/add-leetcode-problem Kth Largest Element in an Array -n 215`), add one Python reference file for that problem to this repository. The file records problem details and examples only; it must not contain a solution, answer code, algorithm, or executable Python.

## Verify the problem

1. Parse the supplied title and number. If either is missing, ask for it.
2. Find the problem on LeetCode's official site using its available browser, web search, or fetch tools. Verify that the official problem number and title agree with the request. If they do not, report the discrepancy and ask which problem to use.
3. Use the official page as the source for the canonical problem URL, the introductory context before Example 1, and all sample input/output pairs. Include the meaningful introductory context in the problem description as a concise, faithful paraphrase; do not omit details needed to understand what is given, what is requested, or how terms are defined. Do not invent missing details or use an unofficial mirror to fill gaps. If you cannot access or verify the official page, stop before writing a file and explain why.
4. Do not copy the full problem statement, constraints, or explanatory prose verbatim. Paraphrase the introductory context in your own words, with each complete sentence on its own comment line. Put each next sentence on a new line after the previous sentence's full stop. Record each sample's input and output exactly. If LeetCode provides an explanation for a sample, add a concise paraphrase of that explanation below the output; omit the explanation when none is provided.

## Choose the destination

1. Inspect the repository's existing topic folders and nearby Python solutions. Choose the most appropriate existing folder based on the problem's primary data structure or algorithm, following local naming conventions.
2. If no existing folder is a reasonable fit, ask before creating a new topic folder.
3. Name the file `<official problem title>.py`. Check for an existing file or reference for the same problem number before writing. Never overwrite or replace an existing problem file without explicit permission.

## Create the reference file

Follow the style of nearby files. The file must contain comments only, with:

- A comment header with the verified problem number, official title, canonical LeetCode URL, and a concise, original paraphrase of the meaningful introductory context before Example 1.
- In the problem description, put each complete sentence on a separate comment line; start the next sentence on a new line after each full stop.
- Each verified official sample as concise commented input and output lines.
- A concise, paraphrased explanation under a sample's output when LeetCode provides one; omit it otherwise.

Preserve sample values exactly. Do not add imports, a `Solution` class, executable statements, an algorithm, or implementation code. Do not solve the problem or provide a solution in the chat response. After creating the file, report only its path and confirm that the verified problem details and examples were recorded.
