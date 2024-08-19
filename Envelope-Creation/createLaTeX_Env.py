import csv

def createLaTex(myfile):
    filename = open(myfile, 'r')
    
    # creating dictreader object
    file = csv.DictReader(filename)
    str = ""
    row = 1

    for col in file:
        RollNo = col['Roll']
        Name = col['Name']
        groupNo = col['Group']
        if(groupNo != ""):
            if(row == 1):
                str += "\n\n\\begin{tabular}{|l|p{12cm}|p{2cm}|p{2cm}|p{2cm}|p{3cm}|} \hline \\bfseries Roll & \\bfseries Name & \\bfseries Marks & \\bfseries Given & \\bfseries Cribs? & \\bfseries Sign \\\\ \hline \n"
            else:
                str += "\end{tabular} \n\pagebreak \n\n\\begin{tabular}{|l|p{12cm}|p{2cm}|p{2cm}|p{2cm}|p{3cm}|} \hline \\bfseries Roll & \\bfseries Name & \\bfseries Marks & \\bfseries Given & \\bfseries Cribs? & \\bfseries Sign \\\\ \hline \n"
        str += RollNo + " & " + Name + " & & & & \\\\ \hline \n"
        row = row + 1

    str += "\end{tabular}\n\pagebreak\n"
    with open("studLatex.tex", "a") as text_file:
        text_file.write("%s" % str)

with open('studLatex.tex', 'w') as fp:
    pass
createLaTex('d4.csv')
createLaTex('d3.csv')