"""
This module contains the functions to merge the suggestion and the validated
graphs from the JSON file. Plus change the style of the edges in the graph.
"""
import argparse
import json


def merge_json(file, sec, param, value):
    """
    Merge the JSON file with additional relationships.

    Args:
        file (dict): The JSON file with the validated relationships.
        sec (dict): The JSON file with the suggestion relationships
          for the non-valid relations.
        param (str): The property name.
        value (str): The value of the param.

    Returns:
        dict: The merged JSON file.
    """
    style_prop = {
        "basicPropertyValues": [
          {
            "pred": f"https://w3id.org/kgviz/{param}",
            "val": f"{value}"
          }
        ]
      }
    if sec["graphs"][0].get("edges"):
        for f_edge in file["graphs"][0]["edges"]:
            for s_edge in sec["graphs"][0]["edges"]:
                if f_edge["sub"] == s_edge["sub"]\
                  and f_edge["pred"] == s_edge["pred"]\
                  and f_edge["obj"] == s_edge["obj"]:
                    f_edge["meta"] = style_prop

    return file


def main(args_params):
    """
    Main function to merge JSON files.

    Args:
        args (argparse.Namespace): Command-line arguments.

    Returns:
        None
    """
    with open(args_params.input, encoding="utf-8") as f:
        file = json.load(f)

    with open(args_params.sec, encoding="utf-8") as f:
        sec = json.load(f)

    output = merge_json(file, sec, args_params.param, args_params.value)

    with open(args_params.output, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input json file")
    parser.add_argument("sec", help="json with additional relationships")
    parser.add_argument("output", help="output file")
    parser.add_argument("param", help="property name")
    parser.add_argument("value", help="value of the param")

    args = parser.parse_args()
    main(args)
