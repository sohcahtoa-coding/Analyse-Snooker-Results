
import pandas as pd
print("From which year would you like to start analysing?")
start_year = input()
full_data_set = pd.read_csv(r'/home/dave/PycharmProjects/Analyse-Snooker-Results/results.csv')
data_set_from_year = full_data_set[full_data_set['Year'] >= int(start_year)]
print(data_set_from_year.to_string())
data_set_length = len(data_set_from_year)
print("Data Set Length= ", data_set_length)
sorted_data_set_from_year = data_set_from_year.sort_values('Winner')
print(sorted_data_set_from_year.to_string())
# Generate list of player names
names_list = []
name_row_index = []
odds_total = []
names_list.append(sorted_data_set_from_year.iloc[0][0])
print(names_list)
name_row_index.append(0)
for i in range(0, data_set_length - 1):
    current_name = sorted_data_set_from_year.iloc[i][0]
    next_name = sorted_data_set_from_year.iloc[i+1][0]
    if current_name != next_name:
        names_list.append(sorted_data_set_from_year.iloc[i+1][0])
        name_row_index.append(i+1)

print("Names List = ", names_list)
print("Length of names_list =", len(names_list))
for i in range(0, len(names_list)):
    print("Name: ", names_list[i])
    print("Index entry = ", name_row_index[i])
df = pd.DataFrame({'Name': [], 'Games Won': [], 'Games Lost': [], 'Profit': [], 'Profit/Game': []})
for i in range(0, len(names_list)):
# Variable pwh = player historic win count and plh = player historic loss count
    pwh = sorted_data_set_from_year[sorted_data_set_from_year['Winner'].str.contains(names_list[i])]
    plh = sorted_data_set_from_year[sorted_data_set_from_year['Loser'].str.contains(names_list[i])]
    total = pwh['W-odds'].sum()
    total2 = len(plh)
    profit = round(total - len(plh), 2)
    profit_per_game = round((total - len(plh))/(len(pwh)+len(plh)), 2)
# Don't bother listing if player less than 20 games total
    if len(pwh)+len(plh) > 20:
        print("Name: ", names_list[i], "Games Won: ", len(pwh), "Games Lost", len(plh), "Profit = ", profit, "Profit/Game =", profit_per_game)
        df2 = pd.DataFrame({'Name': [names_list[i]], 'Games Won': [len(pwh)], 'Games Lost': [len(plh)], 'Profit': [profit], 'Profit/Game': [profit_per_game]})
        data = [df, df2]
        df = pd.concat(data)
result = df.sort_values('Profit/Game', ascending=False)
result = result.reset_index(drop=True)
print(result.to_string())
