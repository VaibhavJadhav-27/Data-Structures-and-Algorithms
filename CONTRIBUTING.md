# 🤝 Contributing to Data Structures and Algorithms in Python

Thanks for your interest in contributing! This repository is a personal learning project focused on solving DSA problems in Python 🐍. Contributions are welcome to improve the quality, coverage, and clarity of the solutions.

---

## 🧠 What You Can Contribute

- ✅ New problems and solutions in an existing topic folder
- 📁 New topic folders when no existing topic fits
- 🧪 Corrections or alternative approaches to existing solutions
- 💬 Comments that clarify a non-obvious approach
- 📝 Documentation improvements

---

## 📦 Folder & File Naming Guidelines

- Choose the existing folder that best matches the problem’s primary data structure or algorithm.
- Before adding a solution, check for an existing file for the same problem to avoid duplicates.
- Use a descriptive filename based on the problem title, following the existing style (for example, `Two Sum.py`).
- Include the verified problem number, title, canonical LeetCode URL, a concise summary in your own words, and accurate sample input/output comments.
- Do not copy the full problem statement.
- Follow the method signature and return type required by LeetCode. Include only necessary imports and comments.
- If no existing topic folder fits, propose a new folder in your pull request.

---

## 🛠️ How to Contribute

1. **Fork** the repository.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/Data-Structures-and-Algorithms.git
   cd Data-Structures-and-Algorithms
   ```
3. **Create a branch:**
   ```bash
   git checkout -b add/problem-name
   ```
4. **Add or update** the solution or documentation.
5. **Check your change** against the official examples and useful edge cases using LeetCode or a local test harness. There is no repository-wide test runner.
6. **Commit and push** your branch:
   ```bash
   git add "Topic Folder/Problem Name.py"
   git commit -m "Add solution for Problem Name"
   git push origin add/problem-name
   ```
7. **Open a Pull Request** describing the problem, approach, and validation performed.

---

## 🤖 Use the LeetCode Problem Builder

In VS Code Copilot Chat, select **LeetCode Problem Builder** and run the workspace skill with a problem title and number:

```text
/add-leetcode-problem Top K Frequent Elements -n 347
```

The skill verifies the problem on LeetCode and will not overwrite an existing solution. Review and test generated code before submitting it. See [the skill instructions](./.github/skills/add-leetcode-problem/SKILL.md).

---

💡 **Tips for Great Contributions**

- Keep changes focused and avoid unrelated formatting updates.
- Explain the approach and add time/space complexity when useful.
- Mention the checks you ran in your pull request.
- Be respectful and collaborative.

---

📬 **Questions or Suggestions?**

Feel free to open an issue or reach out through GitHub.

---

⭐ If you find this project helpful, consider starring it and sharing it with others.
