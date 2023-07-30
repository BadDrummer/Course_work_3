from utils import get_all_operations, filter_data_by_executed, formatted_data


def main():
    data = get_all_operations()
    filtered_data = filter_data_by_executed(data)
    sorted_data = sorted(filtered_data, key=lambda x: x['date'], reverse=True)

    for item in sorted_data[:5]:
        print(formatted_data(item))


if __name__ == '__main__':
    main()
