# 🔐 Password Tool

> Generate strong random passwords, and find out how strong any password really is, all from your terminal.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Randomness-secrets%20module-2EA44F)
![Status](https://img.shields.io/badge/Status-Working-2EA44F)

---

## ✨ What it does

| Feature | What happens |
|---|---|
| 🎲 **Generate** | Creates a random password of the length you choose, using letters, numbers and symbols |
| 💪 **Check strength** | Rates any password as Weak 🔴, Medium 🟡 or Strong 🟢 |
| 💡 **Tips** | Tells you exactly what to add to make a password stronger |
| 🚫 **Common password alert** | Flags passwords attackers always try first, such as `password` or `qwerty` |
| 🛡️ **Safe input** | Typing words instead of a number never crashes the program |

---

## 🎬 See it in action

```text
---Password Tool---
1. Generate a password
2. Check your password
3. Quit
Choose a section: 1
How long should your password be?10
Your password is  k#8Tz!qP2@

Choose a section: 2
Type in your password: abc
Strength:  Weak 🔴
- Add a number
- Add a capital letter
- Add a symbol e.g %
```

> The password above is just an example. Yours will be different every time.

---

## 🚀 Run it

You need [Python 3](https://www.python.org/downloads/). No extra packages.

```bash
git clone https://github.com/Eyconic-stack/Password-Tool.git
cd Password-Tool
python password_tool.py
```

> 💡 On Windows, if `python` is not recognised, try `py password_tool.py`.

---

## 🧠 How it works

**Generating**
- The program builds a "bag" of characters: letters, digits and symbols from Python's `string` module
- A loop pulls one random character out of the bag at a time and adds it to the password
- It uses the **`secrets`** module instead of `random`, because `secrets` is designed for security, so the result can't be predicted

**Checking**
- A loop looks at each character and ticks four checkboxes: capital letter, small letter, number and symbol
- A score is built up: one point for 8 or more characters, one for 12 or more, and one for each checkbox ticked (6 points in total)
- The score becomes a rating: 0 to 2 is Weak, 3 to 4 is Medium, and 5 to 6 is Strong
- Passwords found in a list of very common passwords are marked Weak straight away, even if they would otherwise score well

**Staying safe**
- `try / except ValueError` stops the program crashing when someone types words instead of a number
- The length is checked before use, so a password that is too short is refused

---

## 🗂️ Project structure

```text
Password-Tool/
├── password_tool.py
└── README.md
```

---

## 📚 What I learned building this

- Building text with a loop, one character at a time
- Why `secrets` is the right tool for anything that protects something
- Returning **two values** from one function
- Validating user input before trusting it
- Why counting character types is not enough to judge a password

---

## 🔭 Ideas for next time

- [ ] Hide typing with `getpass` when checking a password
- [ ] Check against a much bigger list of common passwords
- [ ] Add a passphrase generator (several random words)
- [ ] Let the user choose which character types to include
- [ ] Save generated passwords safely

---

> ⚠️ This tool is for learning. Never share your real passwords, and use a trusted password manager for the ones that matter.

👤 **Godfrey Godwin Osagie** · Lagos, Nigeria
🔗 [GitHub](https://github.com/Eyconic-stack) · [LinkedIn](https://linkedin.com/in/godwin-godfrey-289428355)
