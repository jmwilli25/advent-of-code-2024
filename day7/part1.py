equations = []
operators = ["+", "*"]

with open("artifacts/day7.sample.txt", "r") as f:
    for row in f:
        # add results to a python map
        result, values = row.strip("\n").split(": ")
        values = [int(value) for value in values.split(" ")]
        equation_map = {"result": result, "values": values}
        equations.append(equation_map)


for equation in equations:
    values_array = equation["values"]

    # Calculate all the permutations of the operators based on the number of values in the equation
    # e.g. if the equation has 4 values, there are 3 operator positions and each operator can be either "+" or "*"
    # so the total number of permutations is number_of_operators**number_of_operator_positions,
    # or in our example 2**3 = 8
    number_of_values_in_equation = len(values_array)
    number_of_operator_positions = number_of_values_in_equation - 1
    total_combinations = len(operators) ** number_of_operator_positions

    operator_permutations = []
    for i in range(total_combinations):
        # ["+" if i & (1 << j) else "*" for j in range(number_of_operator_position)]
        # ["+" if i == 0 else "*" for i in list(f"{i:0{number_of_values_in_equation}b}")]

        operator_permutations_as_binary = list(f"{i:0{number_of_operator_positions}b}")
        for operator in operator_permutations_as_binary:
            match operator:
                case "0":
                    operator_permutations.append("+")
                case "1":
                    operator_permutations.append("*")

    for i in range(total_combinations - 1):
        result = 0
        for j in range(total_combinations):
            if total_combinations[j] == "+":
                result += values_array[i] + values_array[i + 1]
            elif total_combinations[j] == "*":
                result += values_array[i] * values_array[i + 1]
            print(values_array[i], operator_permutations[j], values_array[i + 1])
