import argparse

from describe_dataset import describe_dataset


def generate_prompt(source_dataset: str, target_dataset: str) -> str:
    source_description = describe_dataset(source_dataset)
    target_description = describe_dataset(target_dataset)

    prompt = f"""
    I have a dataset I want to convert. This dataset can be described as follows:
    {source_description}
    The dataset I want to convert it to can be described as follows:
    {target_description}
    Please generate me a python script which takes the source dataset path as the first argument named 'source_dataset' 
    and the output path as the second argument named 'output' and converts the source dataset to the output path. You can 
    use any libraries you want. If you are not sure about something, add comment with 'TODO' in the generated code.
    """
    return prompt


def main():
    parser = argparse.ArgumentParser(description="Generate a prompt for converting a dataset.")
    parser.add_argument("source_dataset", type=str, help="The path to the source dataset.")
    parser.add_argument("target_dataset", type=str, help="The path to the target dataset.")
    args = parser.parse_args()

    prompt = generate_prompt(args.source_dataset, args.target_dataset)
    print(prompt)
