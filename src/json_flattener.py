import re

def flatten_dict(d, parent_key='', sep='_'):
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            yield from flatten_dict(v, new_key, sep)
        elif isinstance(v, list):
            for i, item in enumerate(v):
                yield from flatten_dict({str(i)+sep: item}, new_key, sep=sep)
        else:
            yield (new_key, v)

def flatten_data_structure(data_structure):
    for item in data_structure:
        flattened_dict = flatten_dict(item)
        yield dict(flattened_dict)

def find_data(flattened_data, search_term, sep='_'):
    results = []
    for item in flattened_data:
        found_items = {}
        for key, value in item.items():
            pattern = rf'(^|\{sep}){search_term}($|\{sep})'
            if re.search(pattern, key):
                found_items[key] = value
        if found_items:
            results.append(found_items)
    return results


if __name__=="__main__":
  data_structure = [
    {
        "1": "a",
        "2": {
            "Adam": "3",
            "Bob": "4"
        }
    },
    {
        "3": "b",
        "4": [
            {
                "Andover": "South",
                "Basingstoke": {
                    "20": "abc",
                    "21": "def"
                }
            },
            {
                "a": "1",
                "b": "2"
            }
        ]
    }
]

  flattened_data_generator = flatten_data_structure(data_structure)
  flattened_data_structure = list(flattened_data_generator)
  print(flattened_data_structure)