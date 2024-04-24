def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }
game_dict()
def num_points_per_game(player_name):       
  #  my_players-names=[]
    match_points=0
    all_player_names=[]
    all_players_points=[]
    list_player_names1=game_dict()["home"]["players"]
    list_player_names2=game_dict()["away"]["players"]
    list_player_points1=game_dict()["home"]["players"]
    list_player_point2=game_dict()["away"]["players"]
    for a in range(0,len(list_player_names1)):
        all_player_names.append(list_player_names1[a]["name"])
        all_player_names.append(list_player_names2[a]["name"])
        all_players_points.append(list_player_points1[a]["points_per_game"])
        all_players_points.append(list_player_point2[a]["points_per_game"])
    for b in range(0,len(all_player_names)):
       if all_player_names[b]==player_name:
        match_points+= all_players_points[b]
       # print(match_points)
    return match_points
result=num_points_per_game("Rui Hachimura")

def player_age(player_name):
   match_age=0
   all_players_name=[]
   all_playres_ages=[]
   list_all_players1=game_dict()["home"]["players"]
   list_all_players2=game_dict()["away"]["players"]
   list_all_ages1=game_dict()["home"]["players"]
   list_all_ages2=game_dict()["away"]["players"]
   for c in range(0,len(list_all_players1)):
      all_players_name.append(list_all_players1[c]["name"])
      all_players_name.append(list_all_players2[c]["name"])
      all_playres_ages.append(list_all_ages1[c]["age"])
      all_playres_ages.append(list_all_ages2[c]["age"])
      
   for d in range(0,len(all_playres_ages)):
      if all_players_name[d]==player_name:
         match_age+=all_playres_ages[d]
       #  print(all_playres_ages[d])
   return match_age
player_age("Cleveland Cavaliers")
def team_colors(team_name):
   all_new_colors=[]
   all_names=[]
   all_colors1=[]
   all_colors=game_dict()["home"]["colors"]#an array of colors for the home
   all_colors2=game_dict()["away"]["colors"]#an array of colors for the away
   all_colors1.append(all_colors)
   all_colors1.append(all_colors2) #An array of all the colors
   all_team_names=game_dict()["home"]["team_name"]
   all_team_names2=game_dict()["away"]["team_name"]  
   all_names.append(all_team_names)
   all_names.append(all_team_names2) 
   for c in range(0,len(all_names)):    
      if all_names[c]==team_name:
         for u in range(0,len(all_colors1[c])):
          all_new_colors.append(all_colors1[c][u])
         #print(all_new_colors)
   return all_new_colors
result=team_colors("Washington Wizards")
def team_names():
   all_teams=[]
   team_name1=game_dict()["home"]["team_name"]
   team_name2=game_dict()["away"]["team_name"]
   all_teams.append(team_name1)
   all_teams.append(team_name2)
   return all_teams
team_names()
def player_numbers(a_team):
   match_points=[] 
   all_teams=[] 
   all_the_teams=[]
   list_players1=game_dict()["home"]["players"]
   list_players2=game_dict()["away"]["players"]
   all_players=game_dict()["home"]["team_name"]
   player_stats2=game_dict()["away"]["team_name"]
   all_the_teams.append(all_players)
   all_the_teams.append(player_stats2)
   all_teams.append(list_players1)
   all_teams.append(list_players2)
   for t in range(0,len(all_the_teams)):
      if all_the_teams[t]==a_team:
         for u in range(0,len(list_players1)):
          match_points.append( all_teams[t][u]["number"])
#print(match_points)
   return match_points  
my_result=player_numbers("Washington Wizards")
def  player_stats(player_name): 
    matchingPlayer_stats={}   
    total_players=[]
    player_names1=game_dict()["home"]["players"]
    player_name2=game_dict()["away"]["players"]
    
    for f in range(0,len(player_names1)):
       total_players.append(player_names1[f])
       total_players.append(player_name2[f])
    for g in range(0,len(total_players)):
       if total_players[g]["name"]==player_name:
         # print(total_players[g])
          matchingPlayer_stats.update(total_players[g])
         # print(matchingPlayer_stats)
    return matchingPlayer_stats
result3=player_stats("Darius Garland")


def average_rebounds_by_shoe_brand():
    players=[]
    all_players=[]
    all_players1=game_dict()["home"]["players"]
    all_players2=game_dict()["away"]["players"]
    all_players.append(all_players1)
    all_players.append(all_players2)
    for a in range(len(all_players)):         
        for b in range(len(all_players[a])):
           players.append(all_players[a][b])
          # print(players)
    shoe_brand_rebounds = {}
    shoe_brand_count = {}
    for c in range(len(players)):
    #for player in players:
        shoe_brand = players[c]["shoe_brand"]
        rebounds = players[c]["rebounds_per_game"]
       # print(shoe_brand)
       # print(rebounds)

        if shoe_brand in shoe_brand_rebounds:
            shoe_brand_rebounds[shoe_brand] += rebounds
            shoe_brand_count[shoe_brand] += 1
        else:
            shoe_brand_rebounds[shoe_brand] = rebounds
            shoe_brand_count[shoe_brand] = 1

    for brand, rebounds in shoe_brand_rebounds.items():
        count = shoe_brand_count[brand]
        average_rebounds = rebounds / count
        print(f"{brand}: {average_rebounds:>5.2f}")

# def average_rebounds_by_shoe_brand():
#     brands=[] #hold all the brands
#     all_data={}
#     total_nike=0
#     total_puma=0
#     total_jordan=0
#     total_adidas=0
#     matching_brands=[]
#     total_matching_lists=[] #holds the all the nfo of all the players
#     total_matching_lists2=[]   
#     all_home_players=game_dict()["home"]["players"]
#     all_away_players=game_dict()["away"]["players"]
#     total_matching_lists2.append(all_home_players)
#     total_matching_lists2.append(all_away_players)
#     total_brands=[]
#     for a in range(0,len(all_home_players)):
#         total_brands.append(all_home_players[a]["shoe_brand"])
#         total_brands.append(all_away_players[a]["shoe_brand"])
#         total_matching_lists.append(all_away_players[a])
#         total_matching_lists.append(all_home_players[a])
#         #print(total_matching_lists)
#     for b in range(0,len(total_brands)-1):
#            new_brands=[]  
#            new_brands.append(game_dict()["home"]) 
#            new_brands.append(game_dict()['away'])    
#           # print(new_brands)
#            if total_brands[b]  in total_brands[b+1]:
#               continue
#            elif total_brands[b] not in total_brands[b+1] :
#               brands.append(total_brands[b+1])
#               print(brands)
#     # for i in range(len(brands)):
      
#     #          for e in range(len(new_brands)):
#     #             for f in range(len(new_brands[e]["players"])):
#     #               # for g in range(len(new_brands[e]["players"][f])):
#     #                 all_data[brands[i]]=[new_brands[e][f]['rebounds_per_game']] #if new_brands[e]["players"][f]["shoe_brand"]==brands[i] else None]
#     #                 print(all_data)
#     #         #  if brands[i]==total_matching_lists2[c][d]:
#             #     print(total_matching_lists2[c][d]["name"])
#  #   print(total_brands)
              
   
# #     elif total_brands[b] not in brands[e]:          
#     #        brands.append(total_brands[b+1])
#     #     # for c in range(len(total_brands)-1,-1,-1):
#     #    for e in range(0,len(brands)):
#     #     if total_brands[b] in total_brands[b+1]:
#     #      continue
#            # print(brands)
#     # for c in range(0,len(brands)):
#     #     for d in range(0,len(total_matching_lists)):
#     #      if brands[c]==total_matching_lists[d]["shoe_brand"]:
#     #        # print(total_matching_lists[d]["name"]) 
#     #         pass
#         # brands[c].append(total_matching_lists[d]["shoe_brand"])
#             # matching_brands[c].append(total_matching_lists[d]["shoe_brand"]) 
#             #print(brands)          
# #  all_new_brands=[]
# #    all_brands=game_dict()["home"]["players"] 
# #    all_brands2=game_dict()["away"]["players"]
# #    total_nike_bounds=[]
# #    total_Adidas_bounds=[]
# #    total_jordan=[]
# #    total_puma=[]
# #   
# #    
# #       if the_brands2[l]=="Adidas":
# #              print( game_dict()["home"]["players"][l])
# #              total_Adidas_bounds.append(all_rebounds2[l])
# #       elif the_brands=="Nike":
# #              total_nike_bounds.append(all_rebounds2[l])
# #              print(total_nike_bounds)
# #              print(total_Adidas_bounds)
# #       elif the_brands=="Jordan":
# #              total_jordan.append(all_rebounds2[l])
# #             # print(total_jordan)
# #       elif the_brands=="Puma":
# #              total_puma.append(all_rebounds2[l])
# #              print(total_jordan)
# #        # else:break
all_result=average_rebounds_by_shoe_brand()
#print(all_result)