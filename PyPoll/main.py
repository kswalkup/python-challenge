import os
import csv

votesCast = []
Khan = []
Correy = []
Li = []
O_Tooley = []

electionData_csv = os.path.join("Resources","election_data.csv")

with open(electionData_csv, 'r') as csvfile:
    next(csvfile)
    
    csvreader = csv.reader(csvfile, delimiter=',')
   
    for row in csvreader:
        votesCast.append(row[2])
        
        #tally Kahn votes
        if str(row[2]) == "Khan":
            Khan.append(row[2])
        #tally Correy votes    
        if str(row[2]) == "Correy":
            Correy.append(row[2])        
        #tally Li votes 
        if str(row[2]) == "Li":
            Li.append(row[2])
        #tally O'Toole votes
        if str(row[2]) == "O'Tooley":
            O_Tooley.append(row[2])    
 
    #count the total number of votes cast
    totalVotes = len(votesCast)
 
    #calculate Kahn's vote precentage
    totalKhan = len(Khan) 
    KhanPer = round(((totalKhan) / (totalVotes) *100))
    
    #calculate Correy's vote precentage
    totalCorrey = len(Correy)
    CorreyPer = round(((totalCorrey) / (totalVotes) *100))
    
    #calculate Li's vote precentage
    totalLi = len(Li)
    LiPer = round(((totalLi) / (totalVotes) *100))
    
    #calculate O'Tooley's vote precentage
    totalO_Tooley = len(O_Tooley) 
    O_TooleyPer = round(((totalO_Tooley) / (totalVotes) *100))
    
    #calculate popular vote winner
    if (totalKhan) > (totalCorrey) and (totalLi) and (totalO_Tooley):
        winner = "Khan"
    elif (totalCorrey) > (totalKhan) and (totalLi) and (totalO_Tooley):
        winner = "Correy"
    elif (totalLi) > (totalKhan) and (totalCorrey) and (totalO_Tooley):
        winner = "Li"
    else:
        winner = "O'Tooley" 

    #print to terminal
    print("Election Results")
    print("-------------------------")    
    print(f'Total Votes: {totalVotes}')
    print("-------------------------")       
    print(f'Khan: {KhanPer}% ({totalKhan})')
    print(f'Correy: {CorreyPer}% ({totalCorrey})')    
    print(f'Li: {LiPer}% ({totalLi})')    
    print(f"O'Tooley: {O_TooleyPer}% ({totalO_Tooley})")
    print("-------------------------")
    print(f'Winner: {winner}') 
    print("-------------------------")
    
    #print to file
    f = open ("Election_Results.txt", "a")
    print("Election Results", file=f)
    print("-------------------------", file=f)    
    print(f'Total Votes: {totalVotes}', file=f)
    print("-------------------------", file=f)       
    print(f'Khan: {KhanPer}% ({totalKhan})', file=f)
    print(f'Correy: {CorreyPer}% ({totalCorrey})', file=f)    
    print(f'Li: {LiPer}% ({totalLi})', file=f)    
    print(f"O'Tooley: {O_TooleyPer}% ({totalO_Tooley})", file=f)
    print("-------------------------", file=f)
    print(f'Winner: {winner}', file=f) 
    print("-------------------------", file=f)
    f.close() 
  