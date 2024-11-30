---
title: Edit
long_title: Editing code and document
summary: This article describes how to edit code and documentation.
date: 2024-11-21
---

Thank you for your interest in contributing to Lantana.
To modify documentation, source code, or translations, fork the repository, edit it, and submit a Pull Request.

### 1.Fork Repository

1. Open [Lantana's repository](https://github.com/WSOFT-Project/lantana) and click “Fork”.
2. Review the form and click “Create Fork”.

### 2.Clone Repository
To modify code or documentation, you must clone the repository.
This synchronizes the Lantana code between your local machine and GitHub.

You can clone the repository by running the following command Where `<account-name>` is your account name (i.e., the name of the account you are forking to).

```sh
git clone https://github.com/<account-name>/lantana.git
```

### 3.Edit code and document
Modify the source code or documentation.
Documentation is located in the `docs` directory and themes are located in the `lantana` directory.

To see Lantana under development in real time while editing documentation or modifying a theme, execute the following command in the directory

```sh
script/serve
```

If the command is executed successfully, Lantana is running under development at `http://127.0.0.1:8000/`. You can exit the command by pressing ++ctrl+c++.

However, if you modify the Python code or if you modify the translation, you will need to exit the command and run it again.

### 4.Commit
When you are done revising, commit to save your work.
It is recommended that you commit your work in chunks.

You can commit with the following command

```sh
git commit <commit-message>
```

### 5.Submit Pull Request
Once you have completed your modifications, you will need to submit a Pull Request to the `WSOFT-Project/lantana` repository to reflect your work.

Please create a Pull Request in the `Pull Requests` tab in the repository you are forking. Make sure that the `base` is `WSOFT-Project/lantana`.

After the Pull Request is submitted, it will be reviewed by the person in charge within a few days.
Please make sure you are receiving GitHub notifications.
