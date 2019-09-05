import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("Resources", "Election Analysis")

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", o]
candidate_options = []
candidate_votes{}


with open(csvpath) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]

        if row["Candiate not in candiate_options"]:
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1

        else 

            candidate_votes[row["Candidate"]] = candidates_votes[row["Candidate"]] + 1

     print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

with open(pathout, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    #txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))