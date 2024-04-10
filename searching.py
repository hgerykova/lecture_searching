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


def pattern_search(sequence, pattern):
    # dna_string = set()
    # start_index = 0
    # for element in range(len(sequence)):
    #     dna_substring = sequence[element:element+3]
    #     if dna_substring != pattern:
    #         continue
    #     elif dna_substring == pattern:
    #         dna_string.add(sequence[start_index:element])
    #         start_index = + element + 2
    # return dna_string
    positions = set()
    sequence_index = 0
    n = len(sequence)
    m = len(pattern)
    while sequence_index < n - m:
        if sequence[sequence_index:sequence_index + m] == pattern:
            positions.add(sequence_index + m // 2)
        sequence_index = sequence_index + 1
    return positions



def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    dna_sequence = read_data("sequential.json", "dna_sequence")
    results = linear_search(unordered_numbers, 7)
    dna_string = pattern_search(dna_sequence, "ATA")
    print(results)
    print(dna_string)


if __name__ == '__main__':
    main()