from lib import arg_path_or_default

dominant_phenotype_chances = [1, 1, 1, 0.75, 0.5, 0]
test_couples = [1, 0, 0, 1, 0, 1]

def expected_dominant_offspring(couples):
    expected_val = 0
    for i in range(len(couples)):
        expected_val += couples[i] * dominant_phenotype_chances[i]
    return expected_val * 2 # Each couple has 2 offspring

if __name__ == "__main__":
    actual_couples = [18793, 16720, 19492, 16568, 17067, 16250]
    print(expected_dominant_offspring(actual_couples))
