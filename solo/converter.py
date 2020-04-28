import json
import csv


def convert_dict_to_csv(dict):
    csv_file = "students"

    csv_columns = ['id', 'uniid', 'lastTested', 'totalCommits', 'totalTestsRan', 'totalTestsPassed',
                   'totalDiagnosticErrors', 'differentSlugs', 'differentCourses', 'commitsStyleOK', 'averageGrade',
                   'medianGrade']

    csv_columns_percent = ['totalDiagnosticErrors_per_totalCommits', 'totalTestsPassed_per_totalTestsRan',
                           'commitsStyleOK_per_totalCommits']

    to_drop = ['id', 'uniid', 'lastTested', 'medianGrade']
    to_drop_extra_only = ['totalCommits', 'totalTestsRan', 'differentCourses', 'totalTestsPassed',
                          'totalDiagnosticErrors', 'commitsStyleOK', 'commitsStyleOK_per_totalCommits', 'differentSlugs']

    try:

        # dict_bool = {}
        for i in range(3):
            with open(csv_file + ("_extra.csv" if i == 1 else ".csv" if not i else "_extra_only.csv"), 'w') as csvfile:
                if i == 1:
                    csv_columns = csv_columns_percent + csv_columns

                if i == 2:
                    csv_columns = [x for x in csv_columns if x not in to_drop_extra_only]
                    # csv_columns.append("isTalTechStudent")

                csv_columns = [x for x in csv_columns if x not in to_drop]

                writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=csv_columns)

                # if i == 2:
                #     csvfile.write(f"{len(dict)},{len(csv_columns) - 1}\n")
                #     # -2 because the last field is the one being predicted
                # else:
                csvfile.write(f"{len(dict)},{len(csv_columns) - 1}\n")
                # -1 because the last field is the one being predicted

                writer.writeheader()

                for j, data in enumerate(reversed(dict)):
                    if not i:
                        # dict_bool[j] = 1 if "@" not in data["uniid"] else 0

                        for drop in to_drop:
                            del data[drop]

                    # data["isTalTechStudent"] = dict_bool[j]

                    if i:
                        for extra in csv_columns_percent:
                            left, right = extra.split("_per_")

                            if not data[right]:
                                data[extra] = 0
                            else:
                                data[extra] = data[left] / data[right]

                        if i == 2:
                            for drop in to_drop_extra_only:
                                del data[drop]

                    writer.writerow(data)
    except IOError:
        print("I/O error")


if __name__ == '__main__':
    with open('example.json') as f:
        dict_data = json.load(f)

    convert_dict_to_csv(dict_data)
