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



class Root:

    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)


def preOrder(root):
    if root:
        print(root.val)
        inOrder(root.left)
        inOrder(root.right)


def postOrder(root):
    if root:
        inOrder(root.left)
        inOrder(root.right)
        print(root.val)


def compexity(n):
    a = 0

    for i in range(n): # n
        BinaryTree.insert(n) # log(n)

    for i in range(n):
        for j in range(n):
            a += 1


if __name__ == '__main__':
    root = Root(Root(Root(None, None, 1), Root(Root(None, None, 4), Root(None, None, 7), 6), 3), Root(None, Root(Root(None, None, 13), None, 14), 10), 8)
    inOrder(root)
    print()
    preOrder(root)
    print()
    postOrder(root)
