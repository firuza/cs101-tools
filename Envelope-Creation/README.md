# Generate Envelopes for Quizzes/Exams (Groups)
An envelope is created for every group. The details on the envelope are the group number, quiz/exam title, date, etc., and a table containing a list of students and a facility to write marks and logistics for the crib session. 

* d3.csv / d4.csv: list of students of d3/d4 batch
* createLaTeX_env.py: python script to read in the csv files and generate LaTeX tables (one for each group and each group is typeset on a different page). This creates a file called studLaTeX.tex
* generateEnvelope.tex: LaTeX code that includes studLaTeX.tex file. Format the header, number of columns for the questions, and build and run to generate the pdf file.
