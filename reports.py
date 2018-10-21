from math import ceil

def count_games(file_name):
    total_games = 0
    with open(file_name) as file:
        for line in file.readlines():
            total_games+=1
    return total_games

def decide(file_name, year):
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            if int(line[2]) == int(year):
                return True
    return False

def get_latest(file_name):
    latest_game_year = 0
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            if int(line[2]) > latest_game_year:
                latest_game_year = int(line[2])
                latest_game_name = str(line[0])
    return latest_game_name
        
def count_by_genre(file_name, genre):
    how_many = 0
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            if line[3] == genre:
                how_many+= 1
    return how_many

def get_line_number_by_title(file_name, title):
    line_counter = 0
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            line_counter+= 1
            if line[0] == title:
                return line_counter
    raise ValueError()

def sort_abc(file_name):
    list_of_titles=[]
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            list_of_titles.append(line[0])
    list_of_titles.sort()
    return list_of_titles

def get_genres(file_name):
    list_of_genres = []
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            if line[3] not in list_of_genres:
                list_of_genres.append(line[3])
    list_of_genres.sort(key=lambda list_of_genres_letters: list_of_genres_letters.lower())
    return list_of_genres


def get_most_played(file_name):
    most_played = -1.0
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            if most_played < float(line[1]):
                most_played = float(line[1])
                most_played_title = line[0]
    return most_played_title

def sum_sold(file_name, get_selling_list = False):
    total_copies_sold = []
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            total_copies_sold.append(float(line[1]))
    if get_selling_list == True:
        return total_copies_sold
    return sum(total_copies_sold)

def get_selling_avg(file_name):
    total_copies_sold = sum_sold(file_name, True)
    selling_avg_rounded_up = sum(total_copies_sold)/len(total_copies_sold)
    return selling_avg_rounded_up

def count_longest_title(file_name):
    longest_title_length = 0
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            if longest_title_length < len(line[0]):
                longest_title_length = len(line[0])
    return longest_title_length

def get_date_avg(file_name):
    release_years = []
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            release_years.append(int(line[2]))
    release_years_avg_rounded_up = ceil(sum(release_years)/len(release_years))
    return release_years_avg_rounded_up

def get_game(file_name, title):
    with open(file_name) as file:
        for line in file.readlines():
            line=line.split("\t")
            if line[0]==title:
                list_of_properties = [ line[0], float(line[1]), int(line[2]), line[3], line[4][:-1]]
                return list_of_properties