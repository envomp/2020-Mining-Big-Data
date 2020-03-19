Author: Enrico Vompa
Date: 2020.03.20

Data is collected from Arete. (TalTech's automated testing service)

Dataset contains no NULL fields.

Nr of lines: 134
Nr of attributes: 9

Headers:
 - id (integer) - Unique identifier for the student
 - lastTested (long) - Epoch time of last testing
 - totalCommits (integer) - Total number of commits from the student
 - totalTestsRan (integer) - Total number of tests ran for the student
 - totalTestsPassed (integer) - Total number of tests passed from the tests ran
 - totalDiagnosticErrors (integer) - Total number of diagnostic errors. Diagnostic error = style error in code. Eslint for example.
 - differentSlugs (integer) - Number of different exercises the given student has attempted
 - differentCourses (integer) - Number of different courses the given student has attempted
 - commitsStyleOK (integer) - Number of test jobs ran with no diagnostic errors
