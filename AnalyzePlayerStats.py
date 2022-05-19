import csv
import math
import pandas as pd
import json

dataList = []

with open('PlayerStats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    reader = csv.DictReader(csv_file)
    writer = csv.writer(csv_file, delimiter=',', quotechar='"',)
    line_count = 0
    op = open("NewPlayerRanks.csv", "w", newline='')
    headers = ['FantasyPoints','Player','Position','Points','Rebounds','Assists','Blocks', 'Turnovers']
    data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
        
    for row in reader:
        Player = row['Player']
        Position = row['Pos']
        FieldGoalsMade = row['FG']
        FieldGoalsAttempted = row['FGA']
        FieldGoalPercentage = row['FG%']
        FreeThrowsMade = row['FT']
        FreeThrowsAttempted = row['FTA']
        FreeThrowPercentage = row['FT%']
        ThreePointersMade = row['3P']
        OffensiveRebounds = row['ORB']
        DefensiveRebounds = row['DRB']
        Assists = row['AST']
        Steals = row['STL']
        Blocks = row['BLK']
        Turnovers = row['TOV']
        Points = row['PTS']

        DoubleDouble = 0
        if float(Points) > 10 and (float(DefensiveRebounds)+float(OffensiveRebounds)) > 10:
            DoubleDouble=3
        elif float(Points) > 10 and float(Assists) > 10:
            DoubleDouble=3
        elif float(Assists) > 10 and float(float(DefensiveRebounds)+float(OffensiveRebounds)) > 10:
            DoubleDouble = 3

        FantasyPoints = str(round((2*float(FieldGoalsMade)) + (-1*float(FieldGoalsAttempted)) + (-1*float(FreeThrowsAttempted)) + (float(FreeThrowsMade)) + (float(ThreePointersMade)) + (0.5*float(OffensiveRebounds)) + (float(DefensiveRebounds)) + (2*float(Assists)) + (3*float(Steals)) + (3*float(Blocks)) + (-2*float(Turnovers)) + (float(Points)) + DoubleDouble)) + "," + Player
        line_count += 1
        data.writerow({'FantasyPoints': FantasyPoints, 'Position': Position, 'Points': Points, 'Rebounds': round(float(DefensiveRebounds)+float(OffensiveRebounds)), 'Assists': Assists, 'Blocks': Blocks, 'Turnovers': Turnovers})
  
op.close()

csv_file.close()