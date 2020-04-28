student.csv description:

Author: Enrico Vompa
Date: 2020.03.20

Data is collected from Arete. (TalTech's automated testing service)

Dataset contains no NULL fields.

Nr of lines: 153

Nr of attributes: 8

Headers:

- totalCommits (integer) - Total number of commits from the student
- totalTestsRan (integer) - Total number of tests ran for the student
- totalTestsPassed (integer) - Total number of tests passed from the tests ran
- totalDiagnosticErrors (integer) - Total number of diagnostic errors. Diagnostic error = style error in code. Eslint for example.
- differentSlugs (integer) - Number of different exercises the given student has attempted
- differentCourses (integer) - Number of different courses the given student has attempted
- commitsStyleOK (integer) - Number of test jobs ran with no diagnostic errors
- averageGrade (float) - students' average score




students_extra.csv description:

Author: Enrico Vompa
Date: 2020.04.11

Data is collected from Arete. (TalTech's automated testing service)

Dataset contains no NULL fields.

Nr of lines: 153
Nr of attributes: 11

Headers:
 - totalDiagnosticErrors_per_totalCommits (float) - totalDiagnosticErrors divided by totalCommits
 - totalTestsPassed_per_totalTestsRan (float) - totalTestsPassed divided by totalTestsRan
 - commitsStyleOK_per_totalCommits (float) - commitsStyleOK divided by totalCommits
 - totalCommits (integer) - Total number of commits from the student
 - totalTestsRan (integer) - Total number of tests ran for the student
 - totalTestsPassed (integer) - Total number of tests passed from the tests ran
 - totalDiagnosticErrors (integer) - Total number of diagnostic errors. Diagnostic error = style error in code. Eslint for example.
 - differentSlugs (integer) - Number of different exercises the given student has attempted
 - differentCourses (integer) - Number of different courses the given student has attempted
 - commitsStyleOK (integer) - Number of test jobs ran with no diagnostic errors
 - averageGrade (float) - students' average score
 
 
 
 students_extra_only.csv description:

Author: Enrico Vompa
Date: 2020.04.11

Data is collected from Arete. (TalTech's automated testing service)

Dataset contains no NULL fields.

Nr of lines: 153
Nr of attributes: 4

Headers:
 - totalDiagnosticErrors_per_totalCommits (float) - totalDiagnosticErrors divided by totalCommits
 - totalTestsPassed_per_totalTestsRan (float) - totalTestsPassed divided by totalTestsRan
 - differentSlugs (integer) - Number of different exercises the given student has attempted
 - averageGrade (float) - students' average score