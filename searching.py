import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None


    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode= "r") as json_file:
        data = json.load(json_file)
    return data[field]

def linear_search(numbers, my_number):
    results = {"positions":[], "count":0}
    for i in range(len(numbers)):
        if numbers[i] == my_number:
            results["positions"].append(i)
            results["count"] = results["count"] + 1
    return results


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)

if __name__ == '__main__':
    main()