import json
import csv


def convert_dict_to_csv(dict, public):
    csv_file = "students.csv"

    if public:
        csv_columns = ['id', 'lastTested', 'totalCommits', 'totalTestsRan', 'totalTestsPassed',
                       'totalDiagnosticErrors', 'differentSlugs', 'differentCourses', 'commitsStyleOK']
    else:
        csv_columns = ['id', 'uniid', 'lastTested', 'totalCommits', 'totalTestsRan', 'totalTestsPassed',
                       'totalDiagnosticErrors',
                       'differentSlugs', 'differentCourses', 'commitsStyleOK']

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=csv_columns)
            writer.writeheader()
            for data in reversed(dict):

                if public:
                    del data["uniid"]

                writer.writerow(data)
    except IOError:
        print("I/O error")


if __name__ == '__main__':
    with open('example.json') as f:
        dict_data = json.load(f)

    convert_dict_to_csv(dict_data, True)
