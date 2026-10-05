import csv

def load_data(filename):
    data = []

    with open(filename, "r") as file:
        file.readline()  # header skip

        for line_number, line in enumerate(file, start=2):
            line = line.strip()

            # 빈 줄
            if not line:
                print(f"Warning: line {line_number} is empty. Skipped.")
                continue

            values = line.split(",")

            # 값이 정확히 2개인지 확인
            if len(values) != 2:
                print(f"Warning: invalid format at line {line_number}. Skipped.")
                continue

            # 숫자로 변환 가능한지 확인
            try:
                mileage = int(values[0])
                price = int(values[1])
            except ValueError:
                print(f"Warning: invalid number at line {line_number}. Skipped.")
                continue

            # 음수 확인
            if mileage < 0 or price < 0:
                print(f"Warning: negative value at line {line_number}. Skipped.")
                continue

            data.append((mileage, price))

    return data