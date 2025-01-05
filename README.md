# Convert Dataset

A tool to generate prompts for LLM to convert datasets between formats easily. The tool analyzes the source and target datasets and generates prompt which you can use with your favourite LLM to get a Python script that can perform the conversion.

---

## Features

- Analyzes source and target datasets to describe their formats.
- Generates a prompt for an LLM to produce a Python script for dataset conversion.
- Outputs the generated prompt in the terminal for easy usage.

---

## Installation

```bash
pip install convert-dataset
```

---

## Usage

Run the `convert-dataset` command from the terminal with the paths to the source and target datasets:

```bash
convert-dataset <source_dataset_path> <target_dataset_path>
```

This will output a prompt for your favorite LLM to generate a Python script for converting the datasets.
Just copy the prompt and paste it into your LLM's interface to get the conversion script.

* Please, pay attention on TODOs in the generated script to fill in the necessary information.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

