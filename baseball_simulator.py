from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("500x400")

root.title("A player contribution simulator")

# Database for 2024
conn_1 = sqlite3.connect("2024_stats.db")
c_1 = conn_1.cursor()
c_1.execute("""CREATE TABLE if NOT EXISTS stats_a (
       Player_name text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer,
       injury_period integer
       )""")
stat_2024 = [
    ["Munetaka Murakami", 345, 81, 0.235, 21, 83, 0],
    ["Tetsuto Yamada", 211, 45, 0.213, 9, 26, 25],
    ["Domingo Santana", 270, 86, 0.319, 11, 42, 0],
    ["Jose Osuna", 376, 99, 0.263, 13, 50, 0],
    ["Nori Aoki", 104, 20, 0.192, 0, 9, 0],
    ["Yasutaka Shiomi", 101, 27, 0.267, 3, 8, 64],
    ["Yuhei Nakamura", 226, 54, 0.239, 0, 21, 5],
    ["Hideki Nagaoka", 300, 83, 0.277, 3, 31, 0],
]

c_1.execute("SELECT * from stats_a")
if c_1.fetchall() == []:
    for player_1 in stat_2024:
        c_1.execute(
            "INSERT INTO stats_a VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI,:injury_period)",
            {
                "player_name": player_1[0],
                "at_bat": player_1[1],
                "number_of_hits": player_1[2],
                "batting_average": player_1[3],
                "homeruns": player_1[4],
                "RBI": player_1[5],
                "injury_period": player_1[6],
            },
        )
conn_1.commit()
conn_1.close()

# Database for 2023
conn_2 = sqlite3.connect("2023_stats.db")
c_2 = conn_2.cursor()
c_2.execute("""CREATE TABLE if NOT EXISTS stats_b (
       Player_name text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer,
       injury_period integer
       )""")
stat_2023 = [
    ["Munetaka Murakami", 496, 127, 0.256, 31, 84, 0],
    ["Tetsuto Yamada", 376, 87, 0.231, 14, 40, 30],
    ["Domingo Santana", 467, 140, 0.300, 18, 66, 0],
    ["Jose Osuna", 501, 127, 0.253, 23, 71, 10],
    ["Nori Aoki", 217, 55, 0.253, 3, 19, 0],
    ["Yasutaka Shiomi", 186, 56, 0.301, 8, 31, 91],
    ["Yuhei Nakamura", 310, 70, 0.226, 4, 33, 7],
    ["Hideki Nagaoka", 445, 101, 0.227, 3, 35, 0],
]

c_2.execute("SELECT * from stats_b")
if c_2.fetchall() == []:
    for player_2 in stat_2023:
        c_2.execute(
            "INSERT INTO stats_b VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI,:injury_period)",
            {
                "player_name": player_2[0],
                "at_bat": player_2[1],
                "number_of_hits": player_2[2],
                "batting_average": player_2[3],
                "homeruns": player_2[4],
                "RBI": player_2[5],
                "injury_period": player_2[6],
            },
        )

conn_2.commit()
conn_2.close()

# Database for 2022
conn_3 = sqlite3.connect("2022_stats.db")

c_3 = conn_3.cursor()

c_3.execute("""CREATE TABLE if NOT EXISTS stats_c (
       Player_name text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_2022 = [
    ["Munetaka Murakami", 487, 155, 0.318, 56, 134],
    ["Tetsuto Yamada", 469, 114, 0.243, 23, 65],
    ["Domingo Santana", 189, 52, 0.275, 15, 35],
    ["Jose Osuna", 496, 135, 0.272, 20, 74],
    ["Nori Aoki", 222, 55, 0.248, 5, 22],
    ["Yasutaka Shiomi", 508, 140, 0.276, 16, 54],
    ["Yuhei Nakamura", 266, 70, 0.263, 5, 28],
    ["Hideki Nagaoka", 511, 123, 0.241, 9, 48],
]

c_3.execute("SELECT * from stats_c")
if c_3.fetchall() == []:
    for player_3 in stat_2022:
        c_3.execute(
            "INSERT INTO stats_c VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": player_3[0],
                "at_bat": player_3[1],
                "number_of_hits": player_3[2],
                "batting_average": player_3[3],
                "homeruns": player_3[4],
                "RBI": player_3[5],
            },
        )

conn_3.commit()

conn_3.close()

# Database for 2021
conn_4 = sqlite3.connect("2021_stats.db")

c_4 = conn_4.cursor()

c_4.execute("""CREATE TABLE if NOT EXISTS stats_d (
       Player_name text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")

stat_2021 = [
    ["Munetaka Murakami", 500, 139, 0.278, 39, 112],
    ["Tetsuto Yamada", 493, 134, 0.272, 34, 101],
    ["Domingo Santana", 372, 108, 0.290, 19, 62],
    ["Jose Osuna", 469, 121, 0.258, 13, 60],
    ["Nori Aoki", 446, 115, 0.258, 9, 56],
    ["Yasutaka Shiomi", 474, 132, 0.278, 14, 59],
    ["Yuhei Nakamura", 377, 105, 0.279, 2, 36],
]

c_4.execute("SELECT * from stats_d")
if c_4.fetchall() == []:
    for player_4 in stat_2021:
        c_4.execute(
            "INSERT INTO stats_d VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": player_4[0],
                "at_bat": player_4[1],
                "number_of_hits": player_4[2],
                "batting_average": player_4[3],
                "homeruns": player_4[4],
                "RBI": player_4[5],
            },
        )

conn_4.commit()

conn_4.close()


# Database for 2020
conn_5 = sqlite3.connect("2020_stats.db")

c_5 = conn_5.cursor()

c_5.execute("""CREATE TABLE if NOT EXISTS stats_e (
       Player_name text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")

stat_2020 = [
    ["Munetaka Murakami", 424, 130, 0.307, 28, 86],
    ["Tetsuto Yamada", 344, 85, 0.254, 12, 52],
    ["Nori Aoki", 357, 113, 0.317, 18, 51],
    ["Yasutaka Shiomi", 154, 43, 0.279, 8, 21],
    ["Yuhei Nakamura", 80, 14, 0.175, 0, 3],
]

c_5.execute("SELECT * from stats_e")
if c_5.fetchall() == []:
    for player_5 in stat_2020:
        c_5.execute(
            "INSERT INTO stats_e VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": player_5[0],
                "at_bat": player_5[1],
                "number_of_hits": player_5[2],
                "batting_average": player_5[3],
                "homeruns": player_5[4],
                "RBI": player_5[5],
            },
        )
conn_5.commit()

conn_5.close()

# Database for performance of Murakami by different teams
conn_6 = sqlite3.connect("Murakami_stats_by_team.db")
c_6 = conn_6.cursor()
c_6.execute("""CREATE TABLE if NOT EXISTS stats_one (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Murakami = [
    ["DeNA 2024", 52, 20, 0.385, 4, 12],
    ["Chunichi 2024", 43, 12, 0.279, 4, 9],
    ["Hanshin 2024", 43, 10, 0.233, 2, 5],
    ["Hirosima 2024", 32, 5, 0.156, 1, 2],
    ["Yomiuri 2024", 46, 8, 0.174, 2, 6],
    ["DeNA 2023", 88, 26, 0.295, 8, 21],
    ["Chunichi 2023", 76, 22, 0.289, 6, 17],
    ["Hanshin 2023", 90, 22, 0.244, 4, 11],
    ["Hirosima 2023", 87, 24, 0.276, 8, 18],
    ["Yomiuri 2023", 94, 16, 0.170, 3, 10],
    ["DeNA 2022", 84, 28, 0.333, 9, 24],
    ["Chunichi 2022", 88, 32, 0.364, 13, 26],
    ["Hanshin 2022", 77, 20, 0.260, 7, 17],
    ["Hirosima 2022", 94, 32, 0.340, 13, 26],
    ["Yomiuri 2022", 87, 23, 0.264, 8, 28],
    ["DeNA 2021", 85, 26, 0.306, 6, 17],
    ["Chunichi 2021", 91, 25, 0.275, 8, 20],
    ["Hanshin 2021", 88, 25, 0.284, 6, 17],
    ["Hirosima 2021", 92, 20, 0.217, 4, 19],
    ["Yomiuri 2021", 89, 31, 0.348, 8, 25],
    ["DeNA 2020", 84, 27, 0.321, 6, 15],
    ["Chunichi 2020", 85, 21, 0.247, 4, 15],
    ["Hanshin 2020", 87, 32, 0.368, 5, 19],
    ["Hirosima 2020", 81, 24, 0.296, 8, 25],
    ["Yomiuri 2020", 87, 26, 0.299, 5, 12],
]
c_6.execute("SELECT * from stats_one")
if c_6.fetchall() == []:
    for team_year_1 in stat_Murakami:
        c_6.execute(
            "INSERT INTO stats_one VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_1[0],
                "at_bat": team_year_1[1],
                "number_of_hits": team_year_1[2],
                "batting_average": team_year_1[3],
                "homeruns": team_year_1[4],
                "RBI": team_year_1[5],
            },
        )
conn_6.commit()
conn_6.close()

# Database for performance of Yamada by different teams
conn_7 = sqlite3.connect("Yamada_stats_by_team.db")
c_7 = conn_7.cursor()

c_7.execute("""CREATE TABLE if NOT EXISTS stats_two (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Yamada = [
    ["DeNA 2024", 22, 3, 0.136, 0, 1],
    ["Chunichi 2024", 16, 4, 0.250, 0, 0],
    ["Hanshin 2024", 20, 4, 0.250, 0, 3],
    ["Hirosima 2024", 13, 1, 0.077, 0, 1],
    ["Yomiuri 2024", 33, 7, 0.212, 0, 0],
    ["DeNA 2023", 56, 18, 0.321, 2, 5],
    ["Chunichi 2023", 60, 9, 0.150, 1, 6],
    ["Hanshin 2023", 73, 15, 0.205, 4, 9],
    ["Hirosima 2023", 54, 16, 0.296, 2, 5],
    ["Yomiuri 2023", 64, 17, 0.266, 3, 7],
    ["DeNA 2022", 86, 25, 0.291, 4, 9],
    ["Chunichi 2022", 87, 17, 0.195, 2, 13],
    ["Hanshin 2022", 71, 17, 0.239, 3, 7],
    ["Hirosima 2022", 76, 23, 0.303, 5, 13],
    ["Yomiuri 2022", 90, 23, 0.256, 4, 16],
    ["DeNA 2021", 84, 24, 0.286, 6, 21],
    ["Chunichi 2021", 94, 28, 0.298, 7, 19],
    ["Hanshin 2021", 86, 21, 0.244, 7, 20],
    ["Hirosima 2021", 82, 20, 0.244, 1, 7],
    ["Yomiuri 2021", 78, 21, 0.269, 6, 16],
    ["DeNA 2020", 73, 18, 0.247, 1, 15],
    ["Chunichi 2020", 64, 18, 0.281, 4, 15],
    ["Hanshin 2020", 56, 10, 0.179, 0, 2],
    ["Hirosima 2020", 69, 20, 0.290, 3, 6],
    ["Yomiuri 2020", 72, 19, 0.264, 4, 14],
]

c_7.execute("SELECT * from stats_two")
if c_7.fetchall() == []:
    for team_year_2 in stat_Yamada:
        c_7.execute(
            "INSERT INTO stats_two VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_2[0],
                "at_bat": team_year_2[1],
                "number_of_hits": team_year_2[2],
                "batting_average": team_year_2[3],
                "homeruns": team_year_2[4],
                "RBI": team_year_2[5],
            },
        )

conn_7.commit()

conn_7.close()

# Database for performance of Santana by different teams
conn_8 = sqlite3.connect("Santana_stats_by_team.db")

c_8 = conn_8.cursor()
c_8.execute("""CREATE TABLE if NOT EXISTS stats_three (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Santana = [
    ["DeNA 2024", 48, 19, 0.396, 4, 9],
    ["Chunichi 2024", 38, 9, 0.237, 0, 5],
    ["Hanshin 2024", 35, 11, 0.314, 0, 9],
    ["Hirosima 2024", 35, 11, 0.314, 1, 2],
    ["Yomiuri 2024", 41, 14, 0.341, 2, 7],
    ["DeNA 2023", 86, 31, 0.360, 5, 14],
    ["Chunichi 2023", 81, 21, 0.259, 3, 6],
    ["Hanshin 2023", 81, 23, 0.284, 3, 6],
    ["Hirosima 2023", 71, 20, 0.282, 3, 18],
    ["Yomiuri 2023", 81, 27, 0.333, 2, 10],
    ["DeNA 2022", 33, 6, 0.182, 1, 2],
    ["Chunichi 2022", 46, 13, 0.283, 3, 10],
    ["Hanshin 2022", 42, 11, 0.262, 3, 8],
    ["Hirosima 2022", 33, 10, 0.303, 2, 3],
    ["Yomiuri 2022", 35, 12, 0.343, 6, 12],
    ["DeNA 2021", 54, 16, 0.296, 3, 10],
    ["Chunichi 2021", 68, 19, 0.279, 3, 8],
    ["Hanshin 2021", 64, 21, 0.328, 1, 12],
    ["Hirosima 2021", 56, 12, 0.214, 3, 8],
    ["Yomiuri 2021", 71, 22, 0.310, 8, 19],
]

c_8.execute("SELECT * from stats_three")
if c_8.fetchall() == []:
    for team_year_3 in stat_Santana:
        c_8.execute(
            "INSERT INTO stats_three VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_3[0],
                "at_bat": team_year_3[1],
                "number_of_hits": team_year_3[2],
                "batting_average": team_year_3[3],
                "homeruns": team_year_3[4],
                "RBI": team_year_3[5],
            },
        )

conn_8.commit()

conn_8.close()

# Database for performance of Osuna by different teams
conn_9 = sqlite3.connect("Osuna_stats_by_team.db")

c_9 = conn_9.cursor()

c_9.execute("""CREATE TABLE if NOT EXISTS stats_four (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Osuna = [
    ["DeNA 2024", 55, 12, 0.218, 1, 6],
    ["Chunichi 2024", 52, 15, 0.288, 2, 10],
    ["Hanshin 2024", 50, 9, 0.180, 2, 6],
    ["Hirosima 2024", 35, 9, 0.257, 1, 4],
    ["Yomiuri 2024", 52, 15, 0.288, 1, 6],
    ["DeNA 2023", 100, 30, 0.300, 3, 12],
    ["Chunichi 2023", 85, 18, 0.212, 2, 9],
    ["Hanshin 2023", 79, 13, 0.165, 1, 5],
    ["Hirosima 2023", 83, 21, 0.253, 5, 13],
    ["Yomiuri 2023", 88, 29, 0.330, 8, 20],
    ["DeNA 2022", 82, 27, 0.329, 6, 16],
    ["Chunichi 2022", 90, 21, 0.233, 2, 11],
    ["Hanshin 2022", 82, 16, 0.195, 1, 8],
    ["Hirosima 2022", 80, 23, 0.288, 4, 12],
    ["Yomiuri 2022", 100, 30, 0.300, 5, 20],
    ["DeNA 2021", 70, 14, 0.200, 4, 10],
    ["Chunichi 2021", 88, 26, 0.295, 2, 10],
    ["Hanshin 2021", 81, 19, 0.235, 0, 8],
    ["Hirosima 2021", 71, 21, 0.296, 2, 8],
    ["Yomiuri 2021", 89, 20, 0.225, 4, 17],
]

c_9.execute("SELECT * from stats_four")
if c_9.fetchall() == []:
    for team_year_4 in stat_Osuna:
        c_9.execute(
            "INSERT INTO stats_four VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_4[0],
                "at_bat": team_year_4[1],
                "number_of_hits": team_year_4[2],
                "batting_average": team_year_4[3],
                "homeruns": team_year_4[4],
                "RBI": team_year_4[5],
            },
        )

conn_9.commit()

conn_9.close()

# Database for performance of Aoki by different teams
conn_10 = sqlite3.connect("Aoki_stats_by_team.db")

c_10 = conn_10.cursor()

c_10.execute("""CREATE TABLE if NOT EXISTS stats_five (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Aoki = [
    ["DeNA 2024", 23, 3, 0.130, 0, 3],
    ["Chunichi 2024", 11, 2, 0.182, 0, 1],
    ["Hanshin 2024", 8, 4, 0.500, 0, 1],
    ["Hirosima 2024", 10, 2, 0.200, 0, 0],
    ["Yomiuri 2024", 13, 0, 0.000, 0, 1],
    ["DeNA 2023", 24, 5, 0.208, 1, 5],
    ["Chunichi 2023", 29, 5, 0.172, 0, 1],
    ["Hanshin 2023", 31, 6, 0.194, 0, 2],
    ["Hirosima 2023", 34, 7, 0.206, 0, 2],
    ["Yomiuri 2023", 42, 17, 0.405, 0, 2],
    ["DeNA 2022", 36, 9, 0.250, 1, 4],
    ["Chunichi 2022", 36, 8, 0.222, 0, 1],
    ["Hanshin 2022", 58, 14, 0.241, 2, 5],
    ["Hirosima 2022", 36, 8, 0.222, 1, 4],
    ["Yomiuri 2022", 49, 13, 0.265, 1, 7],
    ["DeNA 2021", 68, 12, 0.176, 1, 9],
    ["Chunichi 2021", 78, 13, 0.167, 0, 9],
    ["Hanshin 2021", 92, 23, 0.250, 1, 7],
    ["Hirosima 2021", 73, 28, 0.384, 2, 11],
    ["Yomiuri 2021", 74, 18, 0.243, 2, 8],
    ["DeNA 2020", 81, 27, 0.333, 4, 14],
    ["Chunichi 2020", 69, 16, 0.232, 3, 4],
    ["Hanshin 2020", 77, 27, 0.351, 2, 6],
    ["Hirosima 2020", 60, 21, 0.350, 3, 12],
    ["Yomiuri 2020", 70, 22, 0.314, 6, 15],
]

c_10.execute("SELECT * from stats_five")
if c_10.fetchall() == []:
    for team_year_5 in stat_Aoki:
        c_10.execute(
            "INSERT INTO stats_five VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_5[0],
                "at_bat": team_year_5[1],
                "number_of_hits": team_year_5[2],
                "batting_average": team_year_5[3],
                "homeruns": team_year_5[4],
                "RBI": team_year_5[5],
            },
        )

conn_10.commit()

conn_10.close()

# Database for performance of Shiomi by different teams
conn_11 = sqlite3.connect("Shiomi_stats_by_team.db")

c_11 = conn_11.cursor()

c_11.execute("""CREATE TABLE if NOT EXISTS stats_six (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Shiomi = [
    ["DeNA 2024", 28, 6, 0.214, 0, 3],
    ["Chunichi 2024", 31, 9, 0.290, 2, 3],
    ["Hanshin 2024", 12, 3, 0.250, 1, 1],
    ["Hirosima 2024", 16, 4, 0.250, 0, 1],
    ["Yomiuri 2024", 14, 5, 0.357, 0, 0],
    ["DeNA 2023", 49, 16, 0.327, 2, 4],
    ["Chunichi 2023", 24, 9, 0.375, 1, 7],
    ["Hanshin 2023", 47, 10, 0.213, 2, 6],
    ["Hirosima 2023", 28, 11, 0.393, 0, 7],
    ["Yomiuri 2023", 38, 10, 0.263, 3, 7],
    ["DeNA 2022", 85, 22, 0.259, 3, 11],
    ["Chunichi 2022", 91, 21, 0.231, 0, 3],
    ["Hanshin 2022", 81, 17, 0.210, 1, 6],
    ["Hirosima 2022", 90, 31, 0.344, 3, 16],
    ["Yomiuri 2022", 86, 26, 0.302, 4, 7],
    ["DeNA 2021", 92, 25, 0.272, 3, 16],
    ["Chunichi 2021", 73, 21, 0.288, 1, 5],
    ["Hanshin 2021", 63, 18, 0.286, 1, 9],
    ["Hirosima 2021", 80, 19, 0.238, 2, 9],
    ["Yomiuri 2021", 91, 26, 0.286, 3, 13],
    ["DeNA 2020", 10, 4, 0.400, 1, 2],
    ["Chunichi 2020", 44, 13, 0.295, 4, 9],
    ["Hanshin 2020", 34, 7, 0.206, 2, 6],
    ["Hirosima 2020", 35, 11, 0.314, 0, 2],
    ["Yomiuri 2020", 31, 8, 0.258, 1, 2],
]

c_11.execute("SELECT * from stats_six")
if c_11.fetchall() == []:
    for team_year_6 in stat_Shiomi:
        c_11.execute(
            "INSERT INTO stats_six VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_6[0],
                "at_bat": team_year_6[1],
                "number_of_hits": team_year_6[2],
                "batting_average": team_year_6[3],
                "homeruns": team_year_6[4],
                "RBI": team_year_6[5],
            },
        )

conn_11.commit()

conn_11.close()

# Database for performance of Nakamura by different teams
conn_12 = sqlite3.connect("Nakamura_stats_by_team.db")

c_12 = conn_12.cursor()

c_12.execute("""CREATE TABLE if NOT EXISTS stats_seven (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Nakamura = [
    ["DeNA 2024", 26, 7, 0.269, 0, 2],
    ["Chunichi 2024", 34, 10, 0.294, 0, 5],
    ["Hanshin 2024", 34, 5, 0.147, 0, 2],
    ["Hirosima 2024", 21, 2, 0.095, 0, 1],
    ["Yomiuri 2024", 36, 7, 0.194, 0, 3],
    ["DeNA 2023", 62, 16, 0.258, 2, 10],
    ["Chunichi 2023", 40, 11, 0.275, 0, 4],
    ["Hanshin 2023", 48, 8, 0.167, 0, 1],
    ["Hirosima 2023", 63, 12, 0.190, 0, 6],
    ["Yomiuri 2023", 52, 13, 0.250, 2, 9],
    ["DeNA 2022", 40, 9, 0.225, 3, 6],
    ["Chunichi 2022", 45, 9, 0.200, 0, 5],
    ["Hanshin 2022", 45, 14, 0.311, 0, 2],
    ["Hirosima 2022", 45, 11, 0.244, 0, 3],
    ["Yomiuri 2022", 44, 15, 0.341, 2, 8],
    ["DeNA 2021", 61, 15, 0.246, 1, 12],
    ["Chunichi 2021", 56, 17, 0.304, 1, 4],
    ["Hanshin 2021", 76, 21, 0.276, 0, 8],
    ["Hirosima 2021", 63, 19, 0.302, 0, 5],
    ["Yomiuri 2021", 78, 21, 0.269, 0, 3],
    ["DeNA 2020", 11, 0, 0.000, 0, 0],
    ["Chunichi 2020", 25, 5, 0.200, 0, 2],
    ["Hanshin 2020", 21, 4, 0.190, 0, 0],
    ["Hirosima 2020", 8, 3, 0.375, 0, 0],
    ["Yomiuri 2020", 15, 2, 0.133, 0, 1],
]

c_12.execute("SELECT * from stats_seven")
if c_12.fetchall() == []:
    for team_year_7 in stat_Nakamura:
        c_12.execute(
            "INSERT INTO stats_seven VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_7[0],
                "at_bat": team_year_7[1],
                "number_of_hits": team_year_7[2],
                "batting_average": team_year_7[3],
                "homeruns": team_year_7[4],
                "RBI": team_year_7[5],
            },
        )

conn_12.commit()

conn_12.close()

# Database for performance of Nagaoka by different teams
conn_13 = sqlite3.connect("Nagaoka_stats_by_team.db")

c_13 = conn_13.cursor()

c_13.execute("""CREATE TABLE if NOT EXISTS stats_eight (
       Team_against_year text,
       At_bat integer,
       Number_of_hits integer,
       Batting_average real,
       Number_of_homeruns integer,
       RBI integer
       )""")
stat_Nagaoka = [
    ["DeNA 2024", 52, 13, 0.250, 0, 4],
    ["Chunichi 2024", 43, 6, 0.140, 0, 0],
    ["Hanshin 2024", 47, 16, 0.340, 1, 7],
    ["Hirosima 2024", 35, 10, 0.286, 0, 4],
    ["Yomiuri 2024", 49, 19, 0.388, 1, 6],
    ["DeNA 2023", 78, 15, 0.192, 1, 5],
    ["Chunichi 2023", 82, 22, 0.268, 1, 9],
    ["Hanshin 2023", 77, 16, 0.208, 0, 2],
    ["Hirosima 2023", 76, 14, 0.184, 0, 9],
    ["Yomiuri 2023", 84, 20, 0.238, 1, 6],
    ["DeNA 2022", 81, 24, 0.296, 2, 4],
    ["Chunichi 2022", 85, 17, 0.200, 0, 3],
    ["Hanshin 2022", 91, 23, 0.253, 0, 6],
    ["Hirosima 2022", 98, 23, 0.235, 3, 10],
    ["Yomiuri 2022", 94, 21, 0.223, 4, 15],
]

c_13.execute("SELECT * from stats_eight")
if c_13.fetchall() == []:
    for team_year_8 in stat_Nagaoka:
        c_13.execute(
            "INSERT INTO stats_eight VALUES (:player_name, :at_bat,:number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                "player_name": team_year_8[0],
                "at_bat": team_year_8[1],
                "number_of_hits": team_year_8[2],
                "batting_average": team_year_8[3],
                "homeruns": team_year_8[4],
                "RBI": team_year_8[5],
            },
        )

conn_13.commit()

conn_13.close()

# Database for opponent win-lose performance
conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
c_14 = conn_14.cursor()

c_14.execute("""CREATE TABLE if NOT EXISTS stats_win_lose (
       Team_against_year text,
       Win_number integer,
       Lose_number integer
       )""")
stat_win_lose = [
    ["All 2024", 34, 46],
    ["DeNA 2024", 5, 10],
    ["Chunichi 2024", 7, 5],
    ["Hanshin 2024", 5, 8],
    ["Hirosima 2024", 2, 9],
    ["Yomiuri 2024", 6, 8],
    ["All 2023", 57, 83],
    ["DeNA 2023", 10, 14],
    ["Chunichi 2023", 14, 11],
    ["Hanshin 2023", 7, 17],
    ["Hirosima 2023", 11, 13],
    ["Yomiuri 2023", 8, 17],
    ["All 2022", 80, 59],
    ["DeNA 2022", 16, 9],
    ["Chunichi 2022", 10, 14],
    ["Hanshin 2022", 13, 11],
    ["Hirosima 2022", 16, 8],
    ["Yomiuri 2022", 11, 13],
    ["All 2021", 73, 52],
    ["DeNA 2021", 17, 6],
    ["Chunichi 2021", 13, 6],
    ["Hanshin 2021", 8, 13],
    ["Hirosima 2021", 14, 8],
    ["Yomiuri 2021", 14, 11],
    ["All 2020", 41, 69],
    ["DeNA 2020", 11, 12],
    ["Chunichi 2020", 7, 15],
    ["Hanshin 2020", 10, 13],
    ["Hirosima 2020", 7, 14],
    ["Yomiuri 2020", 6, 15],
]
c_14.execute("SELECT * from stats_win_lose")
if c_14.fetchall() == []:
    for lose_win in stat_win_lose:
        c_14.execute(
            "INSERT INTO stats_win_lose VALUES (:Team_against_year,:Win_number, :Lose_number)",
            {
                "Team_against_year": lose_win[0],
                "Win_number": lose_win[1],
                "Lose_number": lose_win[2],
            },
        )

conn_14.commit()

conn_14.close()

# Database for opponent pitcher and fielding performace
conn_15 = sqlite3.connect("pitcher_fielder_by_opponent.db")
c_15 = conn_15.cursor()

c_15.execute("""CREATE TABLE if NOT EXISTS stats_oppoenent_pitcher_and_fielding
(
       Team_against_year text,
       Earned_run integer,
       Innings_pitched integer,
       ERA real,
       Number_of_errors integer
       )""")

stat_pitch_field = [
    ["DeNA 2024", 63, 161.33, 3.51, 11],
    ["Chunichi 2024", 48, 157, 2.75, 7],
    ["Hanshin 2024", 49, 136.67, 3.23, 5],
    ["Hirosima 2024", 33, 125, 2.38, 10],
    ["Yomiuri 2024", 48, 152, 2.84, 5],
    ["DeNA 2023", 109, 227, 4.32, 12],
    ["Chunichi 2023", 74, 220, 3.03, 23],
    ["Hanshin 2023", 81, 225.33, 3.24, 15],
    ["Hirosima 2023", 90, 217, 3.73, 16],
    ["Yomiuri 2023", 100, 220.33, 4.08, 10],
    ["DeNA 2022", 83, 222.33, 3.36, 6],
    ["Chunichi 2022", 88, 222.67, 3.56, 13],
    ["Hanshin 2022", 84, 228.67, 3.31, 15],
    ["Hirosima 2022", 86, 229, 3.38, 15],
    ["Yomiuri 2022", 120, 229, 4.72, 15],
    ["DeNA 2021", 78, 223, 3.15, 11],
    ["Chunichi 2021", 54, 221, 2.20, 10],
    ["Hanshin 2021", 95, 219, 3.90, 14],
    ["Hirosima 2021", 74, 223, 2.99, 13],
    ["Yomiuri 2021", 117, 220.33, 4.78, 11],
    ["DeNA 2020", 107, 212, 4.54, 13],
    ["Chunichi 2020", 105, 215, 4.40, 8],
    ["Hanshin 2020", 97, 211.33, 4.13, 18],
    ["Hirosima 2020", 121, 213, 5.11, 14],
    ["Yomiuri 2020", 115, 211.67, 4.89, 7],
]

c_15.execute("SELECT * from stats_oppoenent_pitcher_and_fielding")
if c_15.fetchall() == []:
    for pitch_field in stat_pitch_field:
        c_15.execute(
            "INSERT INTO stats_oppoenent_pitcher_and_fielding VALUES (:Team_against_year, :Earned_run, :Innings_pitched, :ERA,:Number_of_errors)",
            {
                "Team_against_year": pitch_field[0],
                "Earned_run": pitch_field[1],
                "Innings_pitched": pitch_field[2],
                "ERA": pitch_field[3],
                "Number_of_errors": pitch_field[4],
            },
        )

conn_15.commit()

conn_15.close()

# Pages for the applications
start_page = Frame(root)
choosing_player_page = Frame(root)
choosing_year_page = Frame(root)
instruction_page = Frame(root)
Results_page = Frame(root)
Results_1_page = Frame(root)
Results_2_page = Frame(root)
Results_3_page = Frame(root)
Results_4_page = Frame(root)
Results_5_page = Frame(root)
Results_6_page = Frame(root)
confirmation_page = Frame(root)


frames = [
    start_page,
    choosing_player_page,
    choosing_year_page,
    Results_page,
    Results_1_page,
    Results_2_page,
    Results_3_page,
    Results_4_page,
    Results_5_page,
    Results_6_page,
    instruction_page,
    confirmation_page,
]

start_page.tkraise()

for page in frames:
    page.grid(row=0, column=0, sticky="nsew")

    # Creating the start page
    start_btn = Button(
        start_page, text="Start", command=lambda: choosing_player_page.tkraise()
    )
start_btn.pack()

instruction_btn = Button(
    start_page, text="Instruction", command=lambda: instruction_page.tkraise()
)
instruction_btn.pack()

start_page.config(bg="green")


# Updating the result page of the application based on the parameters put by the user
def input(player_name, year):
    conn_15 = sqlite3.connect("pitcher_fielder_by_opponent.db")
    c_15 = conn_15.cursor()
    c_15.execute("SELECT * from stats_oppoenent_pitcher_and_fielding")
    player_to_player = {
        "Munetaka Murakami No.55 Infielder": "player 1",
        "Tetsuto Yamada No.1 Infielder": "player 2",
        "Domingo Santana No.25 Outfielder": "player 3",
        "Jose Osuna No.13 Infielder": "player 4",
        "Nori Aoki No.23 Outfielder": "player 5",
        "Yasutaka Shiomi No.9 Outfielder": "player 6",
        "Yuhei Nakamura No.27 Catcher": "player 7",
        "Hideki Nagaoka No.7 Infielder": "player 8",
    }
    player = player_to_player[player_name]

    # Gathering results from the player function
    all_result_1 = calculation(player, year)
    if player == "player 1":
        all_result_2 = Murakami(year)
    elif player == "player 2":
        all_result_2 = Yamada(year)
    elif player == "player 3":
        all_result_2 = Santana(year)
    elif player == "player 4":
        all_result_2 = Osuna(year)
    elif player == "player 5":
        all_result_2 = Aoki(year)
    elif player == "player 6":
        all_result_2 = Shiomi(year)
    elif player == "player 7":
        all_result_2 = Nakamura(year)
    elif player == "player 8":
        all_result_2 = Nagaoka()

        # Updating the text on the results page
    Result_1.config(text=f"Predicted batting average: {all_result_1[0]}")
    Result_2.config(text=f"Predicted number of homeruns: {all_result_1[1]}")
    Result_3.config(text=f"Predicted RBI: {all_result_1[2]}")
    Result_4.config(text=f"Predicted number of hits: {all_result_1[3]}")
    Result_5.config(
        text=f"Predicted team's winning percentage:{round(all_result_1[4]* 100,3)}%"
    )
    Result_6.config(
        text=f"Predicted percentage of 4-0 per game:{round(all_result_1[5] * 100,3)}%"
    )
    Result_7.config(
        text=f"Predicted percentage of 4-1 per game:{round(all_result_1[6]* 100,3)}%"
    )
    Result_8.config(
        text=f"Predicted percentage of 4-2 per game:{round(all_result_1[7]* 100,3)}%"
    )
    Result_9.config(
        text=f"Predicted percentage of 4-3 per game:{round(all_result_1[8]* 100,3)}%"
    )
    Result_10.config(
        text=f"Predicted percentage of 4-4 per game:{round(all_result_1[9]* 100,3)}%"
    )
    Result_11.config(
        text=f"Number of games the player will contribute to the team out of 143 games: {all_result_1[10]}"
    )
    Result_12.config(
        text=f"Number of games the player will contribute to the team's victory out of 143 games: {all_result_1[11]}"
    )

    Result_1_DB.config(text=f"Predicted batting average: {all_result_2[0][0]}")
    Result_2_DB.config(text=f"Predicted number of homeruns:{all_result_2[0][1]}")
    Result_3_DB.config(text=f"Predicted RBI: {all_result_2[0][2]}")
    Result_4_DB.config(text=f"Predicted number of hits: {all_result_2[0][3]}")
    Result_5_DB.config(
        text=f"Predicted team's winning percentage:{round(all_result_2[0][4]* 100, 3)}%"
    )
    Result_6_DB.config(
        text=f"Predicted percentage of 4-0 per game:{round(all_result_2[0][5]* 100, 3)}%"
    )
    Result_7_DB.config(
        text=f"Predicted percentage of 4-1 per game:{round(all_result_2[0][6]* 100, 3)}%"
    )
    Result_8_DB.config(
        text=f"Predicted percentage of 4-2 per game:{round(all_result_2[0][7]* 100, 3)}%"
    )
    Result_9_DB.config(
        text=f"Predicted percentage of 4-3 per game:{round(all_result_2[0][8]* 100, 3)}%"
    )
    Result_10_DB.config(
        text=f"Predicted percentage of 4-4 per game:{round(all_result_2[0][9]* 100, 3)}%"
    )
    Result_11_DB.config(
        text=f"Number of games the player will contribute to the team out of 22 games: {all_result_2[0][10]}"
    )
    Result_12_DB.config(
        text=f"Number of games the player will contribute to the team's victory out of 22 games: {all_result_2[0][11]}"
    )

    Result_1_D.config(text=f"Predicted batting average: {all_result_2[1][0]}")
    Result_2_D.config(text=f"Predicted number of homeruns:{all_result_2[1][1]}")
    Result_3_D.config(text=f"Predicted RBI: {all_result_2[1][2]}")
    Result_4_D.config(text=f"Predicted number of hits: {all_result_2[1][3]}")
    Result_5_D.config(
        text=f"Predicted team's winning percentage:{round(all_result_2[1][4]* 100, 3)}%"
    )
    Result_6_D.config(
        text=f"Predicted percentage of 4-0 per game:{round(all_result_2[1][5]* 100, 3)}%"
    )
    Result_7_D.config(
        text=f"Predicted percentage of 4-1 per game:{round(all_result_2[1][6]* 100, 3)}%"
    )
    Result_8_D.config(
        text=f"Predicted percentage of 4-2 per game:{round(all_result_2[1][7]* 100, 3)}%"
    )
    Result_9_D.config(
        text=f"Predicted percentage of 4-3 per game:{round(all_result_2[1][8]* 100, 3)}%"
    )
    Result_10_D.config(
        text=f"Predicted percentage of 4-4 per game:{round(all_result_2[1][9]* 100, 3)}%"
    )
    Result_11_D.config(
        text=f"Number of games the player will contribute to the team out of 22 games: {all_result_2[1][10]}"
    )
    Result_12_D.config(
        text=f"Number of games the player will contribute to the team's victory out of 22 games: {all_result_2[1][11]}"
    )

    Result_1_T.config(text=f"Predicted batting average: {all_result_2[2][0]}")
    Result_2_T.config(text=f"Predicted number of homeruns:{all_result_2[2][1]}")
    Result_3_T.config(text=f"Predicted RBI: {all_result_2[2][2]}")
    Result_4_T.config(text=f"Predicted number of hits: {all_result_2[2][3]}")
    Result_5_T.config(
        text=f"Predicted team's winning percentage:{round(all_result_2[2][4]* 100, 3)}%"
    )
    Result_6_T.config(
        text=f"Predicted percentage of 4-0 per game:{round(all_result_2[2][5]* 100, 3)}%"
    )
    Result_7_T.config(
        text=f"Predicted percentage of 4-1 per game:{round(all_result_2[2][6]* 100, 3)}%"
    )
    Result_8_T.config(
        text=f"Predicted percentage of 4-2 per game:{round(all_result_2[2][7]* 100, 3)}%"
    )
    Result_9_T.config(
        text=f"Predicted percentage of 4-3 per game:{round(all_result_2[2][8]* 100, 3)}%"
    )
    Result_10_T.config(
        text=f"Predicted percentage of 4-4 per game:{round(all_result_2[2][9]* 100, 3)}%"
    )
    Result_11_T.config(
        text=f"Number of games the player will contribute to the team out of 22 games: {all_result_2[2][10]}"
    )
    Result_12_T.config(
        text=f"Number of games the player will contribute to the team's victory out of 22 games: {all_result_2[2][11]}"
    )

    Result_1_C.config(text=f"Predicted batting average: {all_result_2[3][0]}")
    Result_2_C.config(text=f"Predicted number of homeruns:{all_result_2[3][1]}")
    Result_3_C.config(text=f"Predicted RBI: {all_result_2[3][2]}")
    Result_4_C.config(text=f"Predicted number of hits: {all_result_2[3][3]}")
    Result_5_C.config(
        text=f"Predicted team's winning percentage:{round(all_result_2[3][4]* 100, 3)}%"
    )
    Result_6_C.config(
        text=f"Predicted percentage of 4-0 per game:{round(all_result_2[3][5]* 100, 3)}%"
    )
    Result_7_C.config(
        text=f"Predicted percentage of 4-1 per game:{round(all_result_2[3][6]* 100, 3)}%"
    )
    Result_8_C.config(
        text=f"Predicted percentage of 4-2 per game:{round(all_result_2[3][7]* 100, 3)}%"
    )
    Result_9_C.config(
        text=f"Predicted percentage of 4-3 per game:{round(all_result_2[3][8]* 100, 3)}%"
    )
    Result_10_C.config(
        text=f"Predicted percentage of 4-4 per game:{round(all_result_2[3][9]* 100, 3)}%"
    )
    Result_11_C.config(
        text=f"Number of games the player will contribute to the team out of 22 games: {all_result_2[3][10]}"
    )
    Result_12_C.config(
        text=f"Number of games the player will contribute to the team's victory out of 22 games: {all_result_2[3][11]}"
    )

    Result_1_G.config(text=f"Predicted batting average: {all_result_2[4][0]}")
    Result_2_G.config(text=f"Predicted number of homeruns:{all_result_2[4][1]}")
    Result_3_G.config(text=f"Predicted RBI: {all_result_2[4][2]}")
    Result_4_G.config(text=f"Predicted number of hits: {all_result_2[4][3]}")
    Result_5_G.config(
        text=f"Predicted team's winning percentage:{round(all_result_2[4][4]* 100, 3)}%"
    )
    Result_6_G.config(
        text=f"Predicted percentage of 4-0 per game:{round(all_result_2[4][5]* 100, 3)}%"
    )
    Result_7_G.config(
        text=f"Predicted percentage of 4-1 per game:{round(all_result_2[4][6]* 100, 3)}%"
    )
    Result_8_G.config(
        text=f"Predicted percentage of 4-2 per game:{round(all_result_2[4][7]* 100, 3)}%"
    )
    Result_9_G.config(
        text=f"Predicted percentage of 4-3 per game:{round(all_result_2[4][8]* 100, 3)}%"
    )
    Result_10_G.config(
        text=f"Predicted percentage of 4-4 per game:{round(all_result_2[4][9]* 100, 3)}%"
    )
    Result_11_G.config(
        text=f"Number of games the player will contribute to the team out of 22 games: {all_result_2[4][10]}"
    )
    Result_12_G.config(
        text=f"Number of games the player will contribute to the team's victory out of 22 games: {all_result_2[4][11]}"
    )

    # Finding the average ERA and the fielding performance for each of the teams

    data_pitch_field = c_15.fetchall()

    DeNA_average_ERA_5 = (
        (
            data_pitch_field[0][1]
            + data_pitch_field[5][1]
            + data_pitch_field[10][1]
            + data_pitch_field[15][1]
            + data_pitch_field[20][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[0][2]
            + data_pitch_field[5][2]
            + data_pitch_field[10][2]
            + data_pitch_field[15][2]
            + data_pitch_field[20][2]
        )
    )
    Chunichi_average_ERA_5 = (
        (
            data_pitch_field[1][1]
            + data_pitch_field[6][1]
            + data_pitch_field[11][1]
            + data_pitch_field[16][1]
            + data_pitch_field[21][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[1][2]
            + data_pitch_field[6][2]
            + data_pitch_field[11][2]
            + data_pitch_field[16][2]
            + data_pitch_field[21][2]
        )
    )
    Hanshin_average_ERA_5 = (
        (
            data_pitch_field[2][1]
            + data_pitch_field[7][1]
            + data_pitch_field[12][1]
            + data_pitch_field[17][1]
            + data_pitch_field[22][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[2][2]
            + data_pitch_field[7][2]
            + data_pitch_field[12][2]
            + data_pitch_field[17][2]
            + data_pitch_field[22][2]
        )
    )
    Hiroshima_average_ERA_5 = (
        (
            data_pitch_field[3][1]
            + data_pitch_field[8][1]
            + data_pitch_field[13][1]
            + data_pitch_field[18][1]
            + data_pitch_field[23][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[3][2]
            + data_pitch_field[8][2]
            + data_pitch_field[13][2]
            + data_pitch_field[18][2]
            + data_pitch_field[23][2]
        )
    )
    Yomiuri_average_ERA_5 = (
        (
            data_pitch_field[4][1]
            + data_pitch_field[9][1]
            + data_pitch_field[14][1]
            + data_pitch_field[19][1]
            + data_pitch_field[24][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[4][2]
            + data_pitch_field[9][2]
            + data_pitch_field[14][2]
            + data_pitch_field[19][2]
            + data_pitch_field[24][2]
        )
    )

    DeNA_average_ERA_4 = (
        (
            data_pitch_field[0][1]
            + data_pitch_field[5][1]
            + data_pitch_field[10][1]
            + data_pitch_field[15][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[0][2]
            + data_pitch_field[5][2]
            + data_pitch_field[10][2]
            + data_pitch_field[15][2]
        )
    )
    Chunichi_average_ERA_4 = (
        (
            data_pitch_field[1][1]
            + data_pitch_field[6][1]
            + data_pitch_field[11][1]
            + data_pitch_field[16][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[1][2]
            + data_pitch_field[6][2]
            + data_pitch_field[11][2]
            + data_pitch_field[16][2]
        )
    )
    Hanshin_average_ERA_4 = (
        (
            data_pitch_field[2][1]
            + data_pitch_field[7][1]
            + data_pitch_field[12][1]
            + data_pitch_field[17][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[2][2]
            + data_pitch_field[7][2]
            + data_pitch_field[12][2]
            + data_pitch_field[17][2]
        )
    )
    Hiroshima_average_ERA_4 = (
        (
            data_pitch_field[3][1]
            + data_pitch_field[8][1]
            + data_pitch_field[13][1]
            + data_pitch_field[18][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[3][2]
            + data_pitch_field[8][2]
            + data_pitch_field[13][2]
            + data_pitch_field[18][2]
        )
    )
    Yomiuri_average_ERA_4 = (
        (
            data_pitch_field[4][1]
            + data_pitch_field[9][1]
            + data_pitch_field[14][1]
            + data_pitch_field[19][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[4][2]
            + data_pitch_field[9][2]
            + data_pitch_field[14][2]
            + data_pitch_field[19][2]
        )
    )

    DeNA_average_ERA_3 = (
        (data_pitch_field[0][1] + data_pitch_field[5][1] + data_pitch_field[10][1]) * 9
    ) / ((data_pitch_field[0][2] + data_pitch_field[5][2] + data_pitch_field[10][2]))
    Chunichi_average_ERA_3 = (
        (
            data_pitch_field[1][1]
            + data_pitch_field[6][1]
            + data_pitch_field[11][1]
            + data_pitch_field[16][1]
            + data_pitch_field[21][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[1][2]
            + data_pitch_field[6][2]
            + data_pitch_field[11][2]
            + data_pitch_field[16][2]
            + data_pitch_field[21][2]
        )
    )
    Hanshin_average_ERA_3 = (
        (
            data_pitch_field[2][1]
            + data_pitch_field[7][1]
            + data_pitch_field[12][1]
            + data_pitch_field[17][1]
            + data_pitch_field[22][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[2][2]
            + data_pitch_field[7][2]
            + data_pitch_field[12][2]
            + data_pitch_field[17][2]
            + data_pitch_field[22][2]
        )
    )
    Hiroshima_average_ERA_3 = (
        (
            data_pitch_field[3][1]
            + data_pitch_field[8][1]
            + data_pitch_field[13][1]
            + data_pitch_field[18][1]
            + data_pitch_field[23][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[3][2]
            + data_pitch_field[8][2]
            + data_pitch_field[13][2]
            + data_pitch_field[18][2]
            + data_pitch_field[23][2]
        )
    )
    Yomiuri_average_ERA_3 = (
        (
            data_pitch_field[4][1]
            + data_pitch_field[9][1]
            + data_pitch_field[14][1]
            + data_pitch_field[19][1]
            + data_pitch_field[24][1]
        )
        * 9
    ) / (
        (
            data_pitch_field[4][2]
            + data_pitch_field[9][2]
            + data_pitch_field[14][2]
            + data_pitch_field[19][2]
            + data_pitch_field[24][2]
        )
    )

    DeNA_fielding_5 = (
        data_pitch_field[0][4]
        + data_pitch_field[5][4]
        + data_pitch_field[10][4]
        + data_pitch_field[15][4]
        + data_pitch_field[20][4]
    ) / 5
    Chunichi_fielding_5 = (
        data_pitch_field[1][4]
        + data_pitch_field[6][4]
        + data_pitch_field[11][4]
        + data_pitch_field[16][4]
        + data_pitch_field[21][4]
    ) / 5
    Hanshin_fielding_5 = (
        data_pitch_field[2][4]
        + data_pitch_field[7][4]
        + data_pitch_field[12][4]
        + data_pitch_field[17][4]
        + data_pitch_field[22][4]
    ) / 5
    Hiroshima_fielding_5 = (
        data_pitch_field[3][4]
        + data_pitch_field[8][4]
        + data_pitch_field[13][4]
        + data_pitch_field[18][4]
        + data_pitch_field[23][4]
    ) / 5
    Yomiuri_fielding_5 = (
        data_pitch_field[4][4]
        + data_pitch_field[9][4]
        + data_pitch_field[14][4]
        + data_pitch_field[19][4]
        + data_pitch_field[24][4]
    ) / 5
    DeNA_fielding_4 = (
        data_pitch_field[0][4]
        + data_pitch_field[5][4]
        + data_pitch_field[10][4]
        + data_pitch_field[15][4]
    ) / 4
    Chunichi_fielding_4 = (
        data_pitch_field[1][4]
        + data_pitch_field[6][4]
        + data_pitch_field[11][4]
        + data_pitch_field[16][4]
    ) / 4
    Hanshin_fielding_4 = (
        data_pitch_field[2][4]
        + data_pitch_field[7][4]
        + data_pitch_field[12][4]
        + data_pitch_field[17][4]
    ) / 4
    Hiroshima_fielding_4 = (
        data_pitch_field[3][4]
        + data_pitch_field[8][4]
        + data_pitch_field[13][4]
        + data_pitch_field[18][4]
    ) / 4
    Yomiuri_fielding_4 = (
        data_pitch_field[4][4]
        + data_pitch_field[9][4]
        + data_pitch_field[14][4]
        + data_pitch_field[19][4]
    ) / 4

    DeNA_fielding_3 = (
        data_pitch_field[0][4] + data_pitch_field[5][4] + data_pitch_field[10][4]
    ) / 3
    Chunichi_fielding_3 = (
        data_pitch_field[1][4] + data_pitch_field[6][4] + data_pitch_field[11][4]
    ) / 3
    Hanshin_fielding_3 = (
        data_pitch_field[2][4] + data_pitch_field[7][4] + data_pitch_field[12][4]
    ) / 3
    Hiroshima_fielding_3 = (
        data_pitch_field[3][4] + data_pitch_field[8][4] + data_pitch_field[13][4]
    ) / 3
    Yomiuri_fielding_3 = (
        data_pitch_field[4][4] + data_pitch_field[9][4] + data_pitch_field[14][4]
    ) / 3

    if year == 3 or player == "player 7":
        list_of_ERA = [
            DeNA_average_ERA_3,
            Chunichi_average_ERA_3,
            Hanshin_average_ERA_3,
            Hiroshima_average_ERA_3,
            Yomiuri_average_ERA_3,
        ]
        list_of_field = [
            DeNA_fielding_3,
            Chunichi_fielding_3,
            Hanshin_fielding_3,
            Hiroshima_fielding_3,
            Yomiuri_fielding_3,
        ]

    elif year == 4 or player == "player 3" or player == "player 4":
        list_of_ERA = [
            DeNA_average_ERA_4,
            Chunichi_average_ERA_4,
            Hanshin_average_ERA_4,
            Hiroshima_average_ERA_4,
            Yomiuri_average_ERA_4,
        ]
        list_of_field = [
            DeNA_fielding_4,
            Chunichi_fielding_4,
            Hanshin_fielding_4,
            Hiroshima_fielding_4,
            Yomiuri_fielding_4,
        ]

    elif year == 5:
        list_of_ERA = [
            DeNA_average_ERA_5,
            Chunichi_average_ERA_5,
            Hanshin_average_ERA_5,
            Hiroshima_average_ERA_5,
            Yomiuri_average_ERA_5,
        ]
        list_of_field = [
            DeNA_fielding_5,
            Chunichi_fielding_5,
            Hanshin_fielding_5,
            Hiroshima_fielding_5,
            Yomiuri_fielding_5,
        ]

    ERA_Ranking = []
    Field_Ranking = []

    for data in list_of_ERA:
        if data <= 2.5:
            ERA_Ranking.append("S")
        elif data <= 3 and data > 2.5:
            ERA_Ranking.append("A")
        elif data <= 3.25 and data > 3:
            ERA_Ranking.append("B")
        elif data <= 3.5 and data > 3.25:
            ERA_Ranking.append("C")
        elif data <= 4 and data > 3.5:
            ERA_Ranking.append("D")
        else:
            ERA_Ranking.append("E")

    for data_field in list_of_field:
        if data_field <= 5:
            Field_Ranking.append("S")
        elif data_field >= 5 and data_field < 7:
            Field_Ranking.append("A")
        elif data_field >= 7 and data_field < 10:
            Field_Ranking.append("B")
        elif data_field >= 10 and data_field < 15:
            Field_Ranking.append("C")
        elif data_field >= 15 and data_field < 20:
            Field_Ranking.append("D")
        else:
            Field_Ranking.append("E")

    DeNA_ERA.config(
        text=f"DeNA ERA: {round(list_of_ERA[0],2)} DeNA ERA Ranking: {ERA_Ranking[0]}"
    )
    DeNA_field.config(
        text=f"DeNA fielding errors: {int(list_of_field[0])} DeNA fielding Ranking: {Field_Ranking[0]}"
    )
    DeNA_information.config(
        text=f"{player_name} will contribute{round((all_result_2[0][11]/25)*100,3)}% of games against DeNA"
    )
    Chunichi_ERA.config(
        text=f"Chunichi ERA: {round(list_of_ERA[1],2)} Chunichi ERA Ranking: {ERA_Ranking[1]}"
    )
    Chunichi_field.config(
        text=f"Chunichi fielding errors:{int(list_of_field[1])} Chunichi fielding Ranking: {Field_Ranking[1]}"
    )
    Chunichi_information.config(
        text=f"{player_name} will contribute{round((all_result_2[1][11]/25)*100,3)}% of games against Chunichi: "
    )
    Hanshin_ERA.config(
        text=f"Hanshin ERA: {round(list_of_ERA[2],2)} Hanshin ERA Ranking: {ERA_Ranking[2]} "
    )
    Hanshin_field.config(
        text=f"Hanshin fielding errors: {int(list_of_field[2])}Hanshin fielding Ranking: {Field_Ranking[2]}"
    )
    Hanshin_information.config(
        text=f"{player_name} will contribute{round((all_result_2[2][11]/25)*100,3)}% of games against Hanshin: "
    )
    Hiroshima_ERA.config(
        text=f"Hiroshima ERA: {round(list_of_ERA[3],2)}Hiroshima ERA Ranking: {ERA_Ranking[3]}"
    )
    Hiroshima_field.config(
        text=f"Hiroshima fielding errors:{int(list_of_field[3])} Hiroshima fielding Ranking: {Field_Ranking[3]}"
    )
    Hiroshima_information.config(
        text=f"{player_name} will contribute{round((all_result_2[3][11]/25)*100,3)}% of games against Hiroshima: "
    )
    Yomiuri_ERA.config(
        text=f"Yomiuri ERA: {round(list_of_ERA[4],2)} Yomiuri ERA Ranking: {ERA_Ranking[4]}"
    )
    Yomiuri_field.config(
        text=f"Yomiuri fielding errors: {int(list_of_field[4])}Yomiuri fielding Ranking: {Field_Ranking[4]}"
    )
    Yomiuri_information.config(
        text=f"{player_name} will contribute{round((all_result_2[4][11]/25)*100,3)}% of games against Yomiuri: "
    )

    # Inputting the player's name into the system


def clicked():
    """Evaluating whether the input is valid or not when choosing the player
    for prediction.
       If valid, the system will proceed, otherwise a message box will come up
    """
    player_name = Entrys.get()
    player_name = player_name.lower()
    if (
        player_name == "player 1"
        or player_name == "player 2"
        or player_name == "player 3"
        or player_name == "player 4"
        or player_name == "player 5"
        or player_name == "player 6"
        or player_name == "player 7"
        or player_name == "player 8"
    ):
        Entrys.delete(0, END)
        player_number_name = {
            "player 1": "Munetaka Murakami No.55 Infielder",
            "player 2": "Tetsuto Yamada No.1 Infielder",
            "player 3": "Domingo Santana No.25 Outfielder",
            "player 4": "Jose Osuna No.13 Infielder",
            "player 5": "Nori Aoki No.23 Outfielder",
            "player 6": "Yasutaka Shiomi No.9 Outfielder",
            "player 7": "Yuhei Nakamura No.27 Catcher",
            "player 8": "Hideki Nagaoka No.7 Infielder",
        }
        confirms_2.config(text=player_number_name[player_name])
    elif (
        player_name == "munetaka murakami"
        or player_name == "tetsuto yamada"
        or player_name == "domingo santana"
        or player_name == "jose osuna"
        or player_name == "nori aoki"
        or player_name == "yasutaka shiomi"
        or player_name == "yuhei nakamura"
        or player_name == "hideki nagaoka"
    ):
        Entrys.delete(0, END)
        player_number_name = {
            "munetaka murakami": "Munetaka Murakami No.55 Infielder",
            "tetsuto Yamada": "Tetsuto Yamada No.1 Infielder",
            "domingo santana": "Domingo Santana No.25 Outfielder",
            "jose osuna": "Jose Osuna No.13 Infielder",
            "nori aoki": "Nori Aoki No.23 Outfielder",
            "yasutaka shiomi": "Yasutaka Shiomi No.9 Outfielder",
            "yuhei nakamura": "Yuhei Nakamura No.27 Catcher",
            "hideki nagaoka": "Hideki Nagaoka No.7 Infielder",
        }
        confirms_2.config(text=player_number_name[player_name])
    else:
        messagebox.showwarning(
            "Type in error",
            "Please type in the correct input from player 1 to player 8 or the full name of the player",
        )

        # Setting up the choosing the player page


choosing_player_page.config(bg="#0F1350")
choose_player_lbl = Label(
    choosing_player_page,
    text="Pick a player that you want to predict its future performance.",
    fg="white",
    bg="#0F1350",
)
choose_player_lbl.pack()

information = [
    "Player 1: Munetaka Murakami No.55 Infielder",
    "Player 2:Tetsuto Yamada No.1 Infielder",
    "Player 3: Domingo Santana No.25 Outfielder",
    "Player 4: Jose Osuna No.13 Infielder",
    "Player 5: Nori Aoki No.23 Outfielder",
    "Player 6: Yasutaka Shiomi No.9 Outfielder",
    "Player 7: Yuhei Nakamura No.27 Catcher",
    "Player 8: Hideki Nagaoka No.7 Infielder",
]

for name in information:
    player = Label(choosing_player_page, text=name, fg="#E6002D", bg="#0F1350")
    player.pack()

    # Instructions on choosing the player page
    Instruction = Label(
        choosing_player_page,
        text="Type in the entry below one of the player above. "
        "Type in player and the number or the full name of the player..",
        fg="white",
        bg="#0F1350",
    )
Instruction.pack()

Instruction_2 = Label(
    choosing_player_page,
    text="If you want to pick Munetaka Murakami, type full name or Player 1.",
    fg="white",
    bg="#0F1350",
)
Instruction_2.pack()

Blank = Label(choosing_player_page, text="", fg="white", bg="#0F1350")
Blank.pack()

Entrys = Entry(choosing_player_page, width=50)
Entrys.pack()

# Buttons on the choosing the player page
submit_btn = Button(choosing_player_page, text="Submit", command=clicked)
submit_btn.pack()

back_btn = Button(
    choosing_player_page, text="Back", command=lambda: start_page.tkraise()
)
back_btn.pack()

next_btn = Button(
    choosing_player_page, text="Next", command=lambda: choosing_year_page.tkraise()
)
next_btn.pack()


# Inputting the number of years
def clicked():
    """Evaluating whether the input is valid or not when choosing the number of
    years of past data used for prediction.
           If valid, the system will proceed, otherwise a message box will come up
    """
    years = date_scale_month.get()
    try:
        years = int(years)
        if years >= 3 and years <= 5:
            date_scale_month.delete(0, END)
            confirms_4.config(text=years)
        else:
            messagebox.showwarning(
                "Type in error", "Please type in the number of years between 3 to 5"
            )
    except:
        messagebox.showwarning(
            "Type in error", "Please type in the number of years between 3 to 5"
        )

        # Creating the choosing year page


year = Label(
    choosing_year_page,
    text="How many numbers of years of data do you want the system to use to",
    fg="white",
    bg="#0F1350",
)
year.pack()

date_scale_month = Entry(choosing_year_page, width=10)
date_scale_month.pack()

submit_btn = Button(choosing_year_page, text="Submit", command=clicked)
submit_btn.pack()

back_btn = Button(
    choosing_year_page, text="Back", command=lambda: choosing_player_page.tkraise()
)
back_btn.pack()

next_btn = Button(
    choosing_year_page, text="Next", command=lambda: confirmation_page.tkraise()
)
next_btn.pack()

choosing_year_page.config(bg="#0F1350")

# Creating the confirmation page
confirm = Label(
    confirmation_page,
    text="Please confirm the information below is correct",
    bg="#E6002D",
    fg="white",
)
confirm.pack()
confirms_1 = Label(
    confirmation_page,
    text="The selected player for the simulator is",
    bg="#E6002D",
    fg="white",
)
confirms_1.pack()
confirms_2 = Label(confirmation_page, bg="#E6002D", fg="#0F1350")
confirms_2.pack()
blank = Label(confirmation_page, text="", bg="#E6002D")
blank.pack()
confirms_3 = Label(
    confirmation_page,
    text="The number of years of past data that will be used in the simulator is",
    bg="#E6002D",
    fg="white",
)
confirms_3.pack()
confirms_4 = Label(confirmation_page, bg="#E6002D", fg="#0F1350")
confirms_4.pack()
Click_input = Label(
    confirmation_page,
    text="Click the input button to see the results on the next page",
    bg="#E6002D",
    fg="white",
)
Click_input.pack()
input_btn = Button(
    confirmation_page,
    text="Input",
    command=lambda: input(confirms_2.cget("text"), confirms_4.cget("text")),
)
input_btn.pack()
back_btn = Button(
    confirmation_page, text="Back", command=lambda: choosing_year_page.tkraise()
)
back_btn.pack()
next_btn = Button(
    confirmation_page, text="Next", command=lambda: Results_page.tkraise()
)
next_btn.pack()
confirmation_page.config(bg="#E6002D")

# Creating the results page for the overall performance
Title_result = Label(Results_page, text="Overall result", bg="#00A051", fg="white")
Title_result.pack()
Result_1 = Label(
    Results_page, text="Predicted batting average: ", bg="#00A051", fg="#0F1350"
)
Result_1.pack()
Result_2 = Label(
    Results_page, text="Predicted number of homeruns: ", bg="#00A051", fg="#0F1350"
)
Result_2.pack()
Result_3 = Label(Results_page, text="Predicted RBI: ", bg="#00A051", fg="#0F1350")
Result_3.pack()
Result_4 = Label(
    Results_page, text="Predicted number of hits: ", bg="#00A051", fg="#0F1350"
)
Result_4.pack()
Result_5 = Label(
    Results_page,
    text="Predicted team's winning percentage: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_5.pack()
Result_6 = Label(
    Results_page,
    text="Predicted percentage of 4-0 per game: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_6.pack()
Result_7 = Label(
    Results_page,
    text="Predicted percentage of 4-1 per game: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_7.pack()
Result_8 = Label(
    Results_page,
    text="Predicted percentage of 4-2 per game: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_8.pack()
Result_9 = Label(
    Results_page,
    text="Predicted percentage of 4-3 per game: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_9.pack()
Result_10 = Label(
    Results_page,
    text="Predicted percentage of 4-4 per game: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_10.pack()
Result_11 = Label(
    Results_page,
    text="Number of games the player will contribute to the team out of 143 games: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_11.pack()
Result_12 = Label(
    Results_page,
    text="Number of games the player will contribute to the team's victory out of 143 games: ",
    bg="#00A051",
    fg="#0F1350",
)
Result_12.pack()
Back = Button(Results_page, text="Back", command=lambda: confirmation_page.tkraise())
Back.pack()
Next = Button(Results_page, text="Next", command=lambda: Results_1_page.tkraise())
Next.pack()

# Creating the results page against Yokohama DeNA Baystars
Results_page.config(bg="#00A051")

Title_result_DB = Label(
    Results_1_page,
    text="Overall result against Yokohama DeNA Basyatrs",
    bg="#004583",
    fg="white",
)
Title_result_DB.pack()
Result_1_DB = Label(
    Results_1_page, text="Predicted batting average: ", bg="#004583", fg="#ECB819"
)
Result_1_DB.pack()
Result_2_DB = Label(
    Results_1_page, text="Predicted number of homeruns: ", bg="#004583", fg="#ECB819"
)
Result_2_DB.pack()
Result_3_DB = Label(Results_1_page, text="Predicted RBI: ", bg="#004583", fg="#ECB819")
Result_3_DB.pack()
Result_4_DB = Label(
    Results_1_page, text="Predicted number of hits: ", bg="#004583", fg="#ECB819"
)
Result_4_DB.pack()
Result_5_DB = Label(
    Results_1_page,
    text="Predicted team's winning percentage:",
    bg="#004583",
    fg="#ECB819",
)
Result_5_DB.pack()
Result_6_DB = Label(
    Results_1_page,
    text="Predicted percentage of 4-0 per game:",
    bg="#004583",
    fg="#ECB819",
)
Result_6_DB.pack()
Result_7_DB = Label(
    Results_1_page,
    text="Predicted percentage of 4-1 per game:",
    bg="#004583",
    fg="#ECB819",
)
Result_7_DB.pack()
Result_8_DB = Label(
    Results_1_page,
    text="Predicted percentage of 4-2 per game:",
    bg="#004583",
    fg="#ECB819",
)
Result_8_DB.pack()
Result_9_DB = Label(
    Results_1_page,
    text="Predicted percentage of 4-3 per game:",
    bg="#004583",
    fg="#ECB819",
)
Result_9_DB.pack()
Result_10_DB = Label(
    Results_1_page,
    text="Predicted percentage of 4-4 per game: ",
    bg="#004583",
    fg="#ECB819",
)
Result_10_DB.pack()
Result_11_DB = Label(
    Results_1_page,
    text="Number of games the player will contribute to the team out of 22 games: ",
    bg="#004583",
    fg="#ECB819",
)
Result_11_DB.pack()
Result_12_DB = Label(
    Results_1_page,
    text="Number of games the player will contribute to the team's victory out of 22 games: ",
    bg="#004583",
    fg="#ECB819",
)
Result_12_DB.pack()
Back_1 = Button(Results_1_page, text="Back", command=lambda: Results_page.tkraise())
Back_1.pack()
Next_1 = Button(Results_1_page, text="Next", command=lambda: Results_2_page.tkraise())
Next_1.pack()

# Creating the results page against Chunichi Dragons
Results_1_page.config(bg="#004583")

Title_result_D = Label(
    Results_2_page,
    text="Overall result against Chunichi dragons",
    bg="#003377",
    fg="white",
)
Title_result_D.pack()
Result_1_D = Label(
    Results_2_page, text="Predicted batting average: ", bg="#003377", fg="red"
)
Result_1_D.pack()
Result_2_D = Label(
    Results_2_page, text="Predicted number of homeruns: ", bg="#003377", fg="red"
)
Result_2_D.pack()
Result_3_D = Label(Results_2_page, text="Predicted RBI: ", bg="#003377", fg="red")
Result_3_D.pack()
Result_4_D = Label(
    Results_2_page, text="Predicted number of hits: ", bg="#003377", fg="red"
)
Result_4_D.pack()
Result_5_D = Label(
    Results_2_page, text="Predicted team's winning percentage:", bg="#003377", fg="red"
)
Result_5_D.pack()
Result_6_D = Label(
    Results_2_page, text="Predicted percentage of 4-0 per game:", bg="#003377", fg="red"
)
Result_6_D.pack()
Result_7_D = Label(
    Results_2_page, text="Predicted percentage of 4-1 per game:", bg="#003377", fg="red"
)
Result_7_D.pack()
Result_8_D = Label(
    Results_2_page, text="Predicted percentage of 4-2 per game:", bg="#003377", fg="red"
)
Result_8_D.pack()
Result_9_D = Label(
    Results_2_page, text="Predicted percentage of 4-3 per game:", bg="#003377", fg="red"
)
Result_9_D.pack()
Result_10_D = Label(
    Results_2_page, text="Predicted percentage of 4-4 per game:", bg="#003377", fg="red"
)
Result_10_D.pack()
Result_11_D = Label(
    Results_2_page,
    text="Number of games the player will contribute to the team out of 22 games: ",
    bg="#003377",
    fg="red",
)
Result_11_D.pack()
Result_12_D = Label(
    Results_2_page,
    text="Number of games the player will contribute to the team's victory out of 22 games: ",
    bg="#003377",
    fg="red",
)
Result_12_D.pack()
Back_2 = Button(Results_2_page, text="Back", command=lambda: Results_1_page.tkraise())
Back_2.pack()
Next_2 = Button(Results_2_page, text="Next", command=lambda: Results_3_page.tkraise())
Next_2.pack()

# Creating the results page against Hanshin Tigers
Results_2_page.config(bg="#003377")

Title_result_T = Label(
    Results_3_page,
    text="Overall result against Hanshin Tigers",
    bg="#FCE300",
    fg="white",
)
Title_result_T.pack()
Result_1_T = Label(
    Results_3_page, text="Predicted batting average: ", bg="#FCE300", fg="#E7360C"
)
Result_1_T.pack()
Result_2_T = Label(
    Results_3_page, text="Predicted number of homeruns: ", bg="#FCE300", fg="#E7360C"
)
Result_2_T.pack()
Result_3_T = Label(Results_3_page, text="Predicted RBI: ", bg="#FCE300", fg="#E7360C")
Result_3_T.pack()
Result_4_T = Label(
    Results_3_page, text="Predicted number of hits: ", bg="#FCE300", fg="#E7360C"
)
Result_4_T.pack()
Result_5_T = Label(
    Results_3_page,
    text="Predicted team's winning percentage:",
    bg="#FCE300",
    fg="#E7360C",
)
Result_5_T.pack()
Result_6_T = Label(
    Results_3_page,
    text="Predicted percentage of 4-0 per game:",
    bg="#FCE300",
    fg="#E7360C",
)
Result_6_T.pack()
Result_7_T = Label(
    Results_3_page,
    text="Predicted percentage of 4-1 per game:",
    bg="#FCE300",
    fg="#E7360C",
)
Result_7_T.pack()
Result_8_T = Label(
    Results_3_page,
    text="Predicted percentage of 4-2 per game:",
    bg="#FCE300",
    fg="#E7360C",
)
Result_8_T.pack()
Result_9_T = Label(
    Results_3_page,
    text="Predicted percentage of 4-3 per game:",
    bg="#FCE300",
    fg="#E7360C",
)
Result_9_T.pack()
Result_10_T = Label(
    Results_3_page,
    text="Predicted percentage of 4-4 per game:",
    bg="#FCE300",
    fg="#E7360C",
)
Result_10_T.pack()
Result_11_T = Label(
    Results_3_page,
    text="Number of games the player will contribute to the team out of 22 games: ",
    bg="#FCE300",
    fg="#E7360C",
)
Result_11_T.pack()
Result_12_T = Label(
    Results_3_page,
    text="Number of games the player will contribute to the team's victory out of 22 games: ",
    bg="#FCE300",
    fg="#E7360C",
)
Result_12_T.pack()
Back_3 = Button(Results_3_page, text="Back", command=lambda: Results_2_page.tkraise())
Back_3.pack()
Next_3 = Button(Results_3_page, text="Next", command=lambda: Results_4_page.tkraise())
Next_3.pack()

# Creating the results page against Hiroshima Toyo Carp
Results_3_page.config(bg="#FCE300")

Title_result_C = Label(
    Results_4_page,
    text="Overall result against Hiroshima Toyo Carp",
    bg="#E70012",
    fg="white",
)
Title_result_C.pack()
Result_1_C = Label(
    Results_4_page, text="Predicted batting average: ", bg="#E70012", fg="#053365"
)
Result_1_C.pack()
Result_2_C = Label(
    Results_4_page, text="Predicted number of homeruns: ", bg="#E70012", fg="#053365"
)
Result_2_C.pack()
Result_3_C = Label(Results_4_page, text="Predicted RBI: ", bg="#E70012", fg="#053365")
Result_3_C.pack()
Result_4_C = Label(
    Results_4_page, text="Predicted number of hits: ", bg="#E70012", fg="#053365"
)
Result_4_C.pack()
Result_5_C = Label(
    Results_4_page,
    text="Predicted team's winning percentage:",
    bg="#E70012",
    fg="#053365",
)
Result_5_C.pack()
Result_6_C = Label(
    Results_4_page,
    text="Predicted percentage of 4-0 per game:",
    bg="#E70012",
    fg="#053365",
)
Result_6_C.pack()
Result_7_C = Label(
    Results_4_page,
    text="Predicted percentage of 4-1 per game:",
    bg="#E70012",
    fg="#053365",
)
Result_7_C.pack()
Result_8_C = Label(
    Results_4_page,
    text="Predicted percentage of 4-2 per game:",
    bg="#E70012",
    fg="#053365",
)
Result_8_C.pack()
Result_9_C = Label(
    Results_4_page,
    text="Predicted percentage of 4-3 per game:",
    bg="#E70012",
    fg="#053365",
)
Result_9_C.pack()
Result_10_C = Label(
    Results_4_page,
    text="Predicted percentage of 4-4 per game:",
    bg="#E70012",
    fg="#053365",
)
Result_10_C.pack()
Result_11_C = Label(
    Results_4_page,
    text="Number of games the player will contribute to the team out of 22 games: ",
    bg="#E70012",
    fg="#053365",
)
Result_11_C.pack()
Result_12_C = Label(
    Results_4_page,
    text="Number of games the player will contribute to the team's victory out of 22 games: ",
    bg="#E70012",
    fg="#053365",
)
Result_12_C.pack()
Back_4 = Button(Results_4_page, text="Back", command=lambda: Results_3_page.tkraise())
Back_4.pack()
Next_4 = Button(Results_4_page, text="Next", command=lambda: Results_5_page.tkraise())
Next_4.pack()

# Creating the results page against Yomiuri Giants
Results_4_page.config(bg="#E70012")

Title_result_G = Label(
    Results_5_page,
    text="Overall result against Yomiuri Giants",
    bg="#F49C00",
    fg="white",
)
Title_result_G.pack()
Result_1_G = Label(
    Results_5_page, text="Predicted batting average: ", bg="#F49C00", fg="#221815"
)
Result_1_G.pack()
Result_2_G = Label(
    Results_5_page, text="Predicted number of homeruns: ", bg="#F49C00", fg="#221815"
)
Result_2_G.pack()
Result_3_G = Label(Results_5_page, text="Predicted RBI: ", bg="#F49C00", fg="#221815")
Result_3_G.pack()
Result_4_G = Label(
    Results_5_page, text="Predicted number of hits: ", bg="#F49C00", fg="#221815"
)
Result_4_G.pack()
Result_5_G = Label(
    Results_5_page,
    text="Predicted team's winning percentage:",
    bg="#F49C00",
    fg="#221815",
)
Result_5_G.pack()
Result_6_G = Label(
    Results_5_page,
    text="Predicted percentage of 4-0 per game:",
    bg="#F49C00",
    fg="#221815",
)
Result_6_G.pack()
Result_7_G = Label(
    Results_5_page,
    text="Predicted percentage of 4-1 per game:",
    bg="#F49C00",
    fg="#221815",
)
Result_7_G.pack()
Result_8_G = Label(
    Results_5_page,
    text="Predicted percentage of 4-2 per game:",
    bg="#F49C00",
    fg="#221815",
)
Result_8_G.pack()
Result_9_G = Label(
    Results_5_page,
    text="Predicted percentage of 4-3 per game:",
    bg="#F49C00",
    fg="#221815",
)
Result_9_G.pack()
Result_10_G = Label(
    Results_5_page,
    text="Predicted percentage of 4-4 per game:",
    bg="#F49C00",
    fg="#221815",
)
Result_10_G.pack()
Result_11_G = Label(
    Results_5_page,
    text="Number of games the player will contribute to the team out of 22 games: ",
    bg="#F49C00",
    fg="#221815",
)
Result_11_G.pack()
Result_12_G = Label(
    Results_5_page,
    text="Number of games the player will contribute to the team's victory out of 22 games: ",
    bg="#F49C00",
    fg="#221815",
)
Result_12_G.pack()
Back_5 = Button(Results_5_page, text="Back", command=lambda: Results_4_page.tkraise())
Back_5.pack()
Next_5 = Button(Results_5_page, text="Next", command=lambda: Results_6_page.tkraise())
Next_5.pack()

# Creating the results page for displaying the pitcher and fielder of other teams
Results_5_page.config(bg="#F49C00")

Title = Label(
    Results_6_page,
    text="Overall results compared with opponent pitcher and fielders",
    bg="#00A051",
    fg="white",
)
Title.pack()
DeNA_ERA = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
DeNA_ERA.pack()
DeNA_field = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
DeNA_field.pack()
DeNA_information = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
DeNA_information.pack()
Chunichi_ERA = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Chunichi_ERA.pack()
Chunichi_field = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Chunichi_field.pack()
Chunichi_information = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Chunichi_information.pack()
Hanshin_ERA = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Hanshin_ERA.pack()
Hanshin_field = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Hanshin_field.pack()
Hanshin_information = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Hanshin_information.pack()
Hiroshima_ERA = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Hiroshima_ERA.pack()
Hiroshima_field = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Hiroshima_field.pack()
Hiroshima_information = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Hiroshima_information.pack()
Yomiuri_ERA = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Yomiuri_ERA.pack()
Yomiuri_field = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Yomiuri_field.pack()
Yomiuri_information = Label(Results_6_page, text="", bg="#00A051", fg="#221815")
Yomiuri_information.pack()
Back_6 = Button(Results_6_page, text="Back", command=lambda: Results_5_page.tkraise())
Back_6.pack()
Reset = Button(
    Results_6_page, text="Choose new player", command=lambda: start_page.tkraise()
)
Reset.pack()

Results_6_page.config(bg="#00A051")


# Calculation for the overall result
def calculation(player, year):
    number_to_player = {
        "player 1": 0,
        "player 2": 1,
        "player 3": 2,
        "player 4": 3,
        "player 5": 4,
        "player 6": 5,
        "player 7": 6,
        "player 8": 7,
    }
    index = number_to_player[player]
    conn_1 = sqlite3.connect("2024_stats.db")
    c_1 = conn_1.cursor()
    conn_2 = sqlite3.connect("2023_stats.db")
    c_2 = conn_2.cursor()
    conn_3 = sqlite3.connect("2022_stats.db")
    c_3 = conn_3.cursor()
    conn_4 = sqlite3.connect("2021_stats.db")
    c_4 = conn_4.cursor()
    conn_5 = sqlite3.connect("2020_stats.db")
    c_5 = conn_5.cursor()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()

    c_1.execute("SELECT * from stats_a")
    c_2.execute("SELECT * from stats_b")
    c_3.execute("SELECT * from stats_c")
    c_4.execute("SELECT * from stats_d")
    c_5.execute("SELECT * from stats_e")
    c_14.execute("SELECT * from stats_win_lose")

    data_2024 = c_1.fetchall()
    data_2023 = c_2.fetchall()
    data_2022 = c_3.fetchall()
    data_2021 = c_4.fetchall()
    data_2020 = c_5.fetchall()

    class Player_Total:
        def __init__(
            self,
            bat_2024,
            hit_2024,
            HR_2024,
            RBI_2024,
            injury_2024,
            bat_2023,
            hit_2023,
            HR_2023,
            RBI_2023,
            injury_2023,
            bat_2022,
            hit_2022,
            HR_2022,
            RBI_2022,
            bat_2021,
            hit_2021,
            HR_2021,
            RBI_2021,
            bat_2020,
            hit_2020,
            HR_2020,
            RBI_2020,
        ):
            self.bat_2024 = bat_2024
            self.hit_2024 = hit_2024
            self.HR_2024 = HR_2024
            self.RBI_2024 = RBI_2024
            self.injury_2024 = injury_2024
            self.bat_2023 = bat_2023
            self.hit_2023 = hit_2023
            self.HR_2023 = HR_2023
            self.RBI_2023 = RBI_2023
            self.injury_2023 = injury_2023
            self.bat_2022 = bat_2022
            self.hit_2022 = hit_2022
            self.HR_2022 = HR_2022
            self.RBI_2022 = RBI_2022
            self.bat_2021 = bat_2021
            self.hit_2021 = hit_2021
            self.HR_2021 = HR_2021
            self.RBI_2021 = RBI_2021
            self.bat_2020 = bat_2020
            self.hit_2020 = hit_2020
            self.HR_2020 = HR_2020
            self.RBI_2020 = RBI_2020

        def organize_stats(player):
            return [
                player.bat_2024,
                player.hit_2024,
                player.HR_2024,
                player.RBI_2024,
                player.injury_2024,
                player.bat_2023,
                player.hit_2023,
                player.HR_2023,
                player.RBI_2023,
                player.injury_2023,
                player.bat_2022,
                player.hit_2022,
                player.HR_2022,
                player.RBI_2022,
                player.bat_2021,
                player.hit_2021,
                player.HR_2021,
                player.RBI_2021,
                player.bat_2020,
                player.hit_2020,
                player.HR_2020,
                player.RBI_2020,
            ]

    data_1_Murakami = Player_Total(
        data_2024[0][1],
        data_2024[0][2],
        data_2024[0][4],
        data_2024[0][5],
        data_2024[0][6],
        data_2023[0][1],
        data_2023[0][2],
        data_2023[0][4],
        data_2023[0][5],
        data_2023[0][6],
        data_2022[0][1],
        data_2022[0][2],
        data_2022[0][4],
        data_2022[0][5],
        data_2021[0][1],
        data_2021[0][2],
        data_2021[0][4],
        data_2021[0][5],
        data_2020[0][1],
        data_2020[0][2],
        data_2020[0][4],
        data_2020[0][5],
    )
    player_1_Murakami = data_1_Murakami.organize_stats()

    data_2_Yamada = Player_Total(
        data_2024[1][1],
        data_2024[1][2],
        data_2024[1][4],
        data_2024[1][5],
        data_2024[1][6],
        data_2023[1][1],
        data_2023[1][2],
        data_2023[1][4],
        data_2023[1][5],
        data_2023[1][6],
        data_2022[1][1],
        data_2022[1][2],
        data_2022[1][4],
        data_2022[1][5],
        data_2021[1][1],
        data_2021[1][2],
        data_2021[1][4],
        data_2021[1][5],
        data_2020[1][1],
        data_2020[1][2],
        data_2020[1][4],
        data_2020[1][5],
    )
    player_2_Yamada = data_2_Yamada.organize_stats()

    data_3_Santana = Player_Total(
        data_2024[2][1],
        data_2024[2][2],
        data_2024[2][4],
        data_2024[2][5],
        data_2024[2][6],
        data_2023[2][1],
        data_2023[2][2],
        data_2023[2][4],
        data_2023[2][5],
        data_2023[2][6],
        data_2022[2][1],
        data_2022[2][2],
        data_2022[2][4],
        data_2022[2][5],
        data_2021[2][1],
        data_2021[2][2],
        data_2021[2][4],
        data_2021[2][5],
        None,
        None,
        None,
        None,
    )
    player_3_Santana = data_3_Santana.organize_stats()

    data_4_Osuna = Player_Total(
        data_2024[3][1],
        data_2024[3][2],
        data_2024[3][4],
        data_2024[3][5],
        data_2024[3][6],
        data_2023[3][1],
        data_2023[3][2],
        data_2023[3][4],
        data_2023[3][5],
        data_2023[3][6],
        data_2022[3][1],
        data_2022[3][2],
        data_2022[3][4],
        data_2022[3][5],
        data_2021[3][1],
        data_2021[3][2],
        data_2021[3][4],
        data_2021[3][5],
        None,
        None,
        None,
        None,
    )
    player_4_Osuna = data_4_Osuna.organize_stats()

    data_5_Aoki = Player_Total(
        data_2024[4][1],
        data_2024[4][2],
        data_2024[4][4],
        data_2024[4][5],
        data_2024[4][6],
        data_2023[4][1],
        data_2023[4][2],
        data_2023[4][4],
        data_2023[4][5],
        data_2023[4][6],
        data_2022[4][1],
        data_2022[4][2],
        data_2022[4][4],
        data_2022[4][5],
        data_2021[4][1],
        data_2021[4][2],
        data_2021[4][4],
        data_2021[4][5],
        data_2020[2][1],
        data_2020[2][2],
        data_2020[2][4],
        data_2020[2][5],
    )
    player_5_Aoki = data_5_Aoki.organize_stats()

    data_6_Shiomi = Player_Total(
        data_2024[5][1],
        data_2024[5][2],
        data_2024[5][4],
        data_2024[5][5],
        data_2024[5][6],
        data_2023[5][1],
        data_2023[5][2],
        data_2023[5][4],
        data_2023[5][5],
        data_2023[5][6],
        data_2022[5][1],
        data_2022[5][2],
        data_2022[5][4],
        data_2022[5][5],
        data_2021[5][1],
        data_2021[5][2],
        data_2021[5][4],
        data_2021[5][5],
        data_2020[3][1],
        data_2020[3][2],
        data_2020[3][4],
        data_2020[3][5],
    )
    player_6_Shiomi = data_6_Shiomi.organize_stats()

    data_7_Nakamura = Player_Total(
        data_2024[6][1],
        data_2024[6][2],
        data_2024[6][4],
        data_2024[6][5],
        data_2024[6][6],
        data_2023[6][1],
        data_2023[6][2],
        data_2023[6][4],
        data_2023[6][5],
        data_2023[6][6],
        data_2022[6][1],
        data_2022[6][2],
        data_2022[6][4],
        data_2022[6][5],
        data_2021[6][1],
        data_2021[6][2],
        data_2021[6][4],
        data_2021[6][5],
        data_2020[4][1],
        data_2020[4][2],
        data_2020[4][4],
        data_2020[4][5],
    )
    player_7_Nakamura = data_7_Nakamura.organize_stats()

    data_8_Nagaoka = Player_Total(
        data_2024[7][1],
        data_2024[7][2],
        data_2024[7][4],
        data_2024[7][5],
        data_2024[7][6],
        data_2023[7][1],
        data_2023[7][2],
        data_2023[7][4],
        data_2023[7][5],
        data_2023[7][6],
        data_2022[7][1],
        data_2022[7][2],
        data_2022[7][4],
        data_2022[7][5],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )
    player_8_Nagaoka = data_8_Nagaoka.organize_stats()

    if year == 3:
        data_win = c_14.fetchall()
        total_percentage = (data_win[0][1] + data_win[6][1] + data_win[12][1]) / (
            data_win[0][1]
            + data_win[6][1]
            + data_win[12][1]
            + data_win[0][2]
            + data_win[6][2]
            + data_win[12][2]
        )

        if index == 0:
            batting = (
                player_1_Murakami[1] + player_1_Murakami[6] + player_1_Murakami[11]
            ) / (player_1_Murakami[0] + player_1_Murakami[5] + player_1_Murakami[10])
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_1_Murakami[3] + player_1_Murakami[8] + player_1_Murakami[13]
            ) / (player_1_Murakami[1] + player_1_Murakami[6] + player_1_Murakami[11])
            Homerun_to_hit_ratio = (
                player_1_Murakami[2] + player_1_Murakami[7] + player_1_Murakami[12]
            ) / (player_1_Murakami[1] + player_1_Murakami[6] + player_1_Murakami[11])

            predicted_total_games_played = 143 - (
                (player_1_Murakami[9] + player_1_Murakami[4]) / 2
            )

        elif index == 1:
            batting = (
                player_2_Yamada[1] + player_2_Yamada[6] + player_2_Yamada[11]
            ) / (player_2_Yamada[0] + player_2_Yamada[5] + player_2_Yamada[10])
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_2_Yamada[3] + player_2_Yamada[8] + player_2_Yamada[13]
            ) / (player_2_Yamada[1] + player_2_Yamada[6] + player_2_Yamada[11])
            Homerun_to_hit_ratio = (
                player_2_Yamada[2] + player_2_Yamada[7] + player_2_Yamada[12]
            ) / (player_2_Yamada[1] + player_2_Yamada[6] + player_2_Yamada[11])

            predicted_total_games_played = 143 - (
                (player_2_Yamada[9] + player_2_Yamada[4]) / 2
            )

        elif index == 2:
            batting = (
                player_3_Santana[1] + player_3_Santana[6] + player_3_Santana[11]
            ) / (player_3_Santana[0] + player_3_Santana[5] + player_3_Santana[10])
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_3_Santana[3] + player_3_Santana[8] + player_3_Santana[13]
            ) / (player_3_Santana[1] + player_3_Santana[6] + player_3_Santana[11])
            Homerun_to_hit_ratio = (
                player_3_Santana[2] + player_3_Santana[7] + player_3_Santana[12]
            ) / (player_3_Santana[1] + player_3_Santana[6] + player_3_Santana[11])

            predicted_total_games_played = 143 - (
                (player_3_Santana[9] + player_3_Santana[4]) / 2
            )

        elif index == 3:
            batting = (player_4_Osuna[1] + player_4_Osuna[6] + player_4_Osuna[11]) / (
                player_4_Osuna[0] + player_4_Osuna[5] + player_4_Osuna[10]
            )
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_4_Osuna[3] + player_4_Osuna[8] + player_4_Osuna[13]
            ) / (player_4_Osuna[1] + player_4_Osuna[6] + player_4_Osuna[11])
            Homerun_to_hit_ratio = (
                player_4_Osuna[2] + player_4_Osuna[7] + player_4_Osuna[12]
            ) / (player_4_Osuna[1] + player_4_Osuna[6] + player_4_Osuna[11])

            predicted_total_games_played = 143 - (
                (player_4_Osuna[4] + player_4_Osuna[9]) / 2
            )

        elif index == 4:
            batting = (player_5_Aoki[1] + player_5_Aoki[6] + player_5_Aoki[11]) / (
                player_5_Aoki[0] + player_5_Aoki[5] + player_5_Aoki[10]
            )
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_5_Aoki[3] + player_5_Aoki[8] + player_5_Aoki[13]
            ) / (player_5_Aoki[1] + player_5_Aoki[6] + player_5_Aoki[11])
            Homerun_to_hit_ratio = (
                player_5_Aoki[2] + player_5_Aoki[7] + player_5_Aoki[12]
            ) / (player_5_Aoki[1] + player_5_Aoki[6] + player_5_Aoki[11])

            predicted_total_games_played = 143 - (
                (player_5_Aoki[4] + player_5_Aoki[9]) / 2
            )
        elif index == 5:
            batting = (
                player_6_Shiomi[1] + player_6_Shiomi[6] + player_6_Shiomi[11]
            ) / (player_6_Shiomi[0] + player_6_Shiomi[5] + player_6_Shiomi[10])
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_6_Shiomi[3] + player_6_Shiomi[8] + player_6_Shiomi[13]
            ) / (player_6_Shiomi[1] + player_6_Shiomi[6] + player_6_Shiomi[11])
            Homerun_to_hit_ratio = (
                player_6_Shiomi[2] + player_6_Shiomi[7] + player_6_Shiomi[12]
            ) / (player_6_Shiomi[1] + player_6_Shiomi[6] + player_6_Shiomi[11])

            predicted_total_games_played = 143 - (
                (player_6_Shiomi[4] + player_6_Shiomi[9]) / 2
            )

        elif index == 6:
            batting = (
                player_7_Nakamura[1] + player_7_Nakamura[6] + player_7_Nakamura[11]
            ) / (player_7_Nakamura[0] + player_7_Nakamura[5] + player_7_Nakamura[10])
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_7_Nakamura[3] + player_7_Nakamura[8] + player_7_Nakamura[13]
            ) / (player_7_Nakamura[1] + player_7_Nakamura[6] + player_7_Nakamura[11])
            Homerun_to_hit_ratio = (
                player_7_Nakamura[2] + player_7_Nakamura[7] + player_7_Nakamura[12]
            ) / (player_7_Nakamura[1] + player_7_Nakamura[6] + player_7_Nakamura[11])

            predicted_total_games_played = 143 - (
                (player_7_Nakamura[4] + player_7_Nakamura[9]) / 2
            )

        elif index == 7:
            batting = (
                player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11]
            ) / (player_8_Nagaoka[0] + player_8_Nagaoka[5] + player_8_Nagaoka[10])
            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_8_Nagaoka[3] + player_8_Nagaoka[8] + player_8_Nagaoka[13]
            ) / (player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11])
            Homerun_to_hit_ratio = (
                player_8_Nagaoka[2] + player_8_Nagaoka[7] + player_8_Nagaoka[12]
            ) / (player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11])

            predicted_total_games_played = 143 - (
                (player_8_Nagaoka[4] + player_8_Nagaoka[9]) / 2
            )

    elif year == 4:
        data_win = c_14.fetchall()
        total_percentage = (
            data_win[0][1] + data_win[6][1] + data_win[12][1] + data_win[18][1]
        ) / (
            data_win[0][1]
            + data_win[6][1]
            + data_win[12][1]
            + data_win[18][1]
            + data_win[0][2]
            + data_win[6][2]
            + data_win[12][2]
            + data_win[18][2]
        )

        if index == 0:
            batting = (
                player_1_Murakami[1]
                + player_1_Murakami[6]
                + player_1_Murakami[11]
                + player_1_Murakami[15]
            ) / (
                player_1_Murakami[0]
                + player_1_Murakami[5]
                + player_1_Murakami[10]
                + player_1_Murakami[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_1_Murakami[3]
                + player_1_Murakami[8]
                + player_1_Murakami[13]
                + player_1_Murakami[17]
            ) / (
                player_1_Murakami[1]
                + player_1_Murakami[6]
                + player_1_Murakami[11]
                + player_1_Murakami[15]
            )
            Homerun_to_hit_ratio = (
                player_1_Murakami[2]
                + player_1_Murakami[7]
                + player_1_Murakami[12]
                + player_1_Murakami[16]
            ) / (
                player_1_Murakami[1]
                + player_1_Murakami[6]
                + player_1_Murakami[11]
                + player_1_Murakami[15]
            )

            predicted_total_games_played = 143 - (
                (player_1_Murakami[4] + player_1_Murakami[9]) / 2
            )

        elif index == 1:
            batting = (
                player_2_Yamada[1]
                + player_2_Yamada[6]
                + player_2_Yamada[11]
                + player_2_Yamada[15]
            ) / (
                player_2_Yamada[0]
                + player_2_Yamada[5]
                + player_2_Yamada[10]
                + player_2_Yamada[14]
            )
            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_2_Yamada[3]
                + player_2_Yamada[8]
                + player_2_Yamada[13]
                + player_2_Yamada[17]
            ) / (
                player_2_Yamada[1]
                + player_2_Yamada[6]
                + player_2_Yamada[11]
                + player_2_Yamada[15]
            )
            Homerun_to_hit_ratio = (
                player_2_Yamada[2]
                + player_2_Yamada[7]
                + player_2_Yamada[12]
                + player_2_Yamada[16]
            ) / (
                player_2_Yamada[1]
                + player_2_Yamada[6]
                + player_2_Yamada[11]
                + player_2_Yamada[15]
            )

            predicted_total_games_played = 143 - (
                (player_2_Yamada[4] + player_2_Yamada[9]) / 2
            )

        elif index == 2:
            batting = (
                player_3_Santana[1]
                + player_3_Santana[6]
                + player_3_Santana[11]
                + player_3_Santana[15]
            ) / (
                player_3_Santana[0]
                + player_3_Santana[5]
                + player_3_Santana[10]
                + player_3_Santana[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_3_Santana[3]
                + player_3_Santana[8]
                + player_3_Santana[13]
                + player_3_Santana[17]
            ) / (
                player_3_Santana[1]
                + player_3_Santana[6]
                + player_3_Santana[11]
                + player_3_Santana[15]
            )
            Homerun_to_hit_ratio = (
                player_3_Santana[2]
                + player_3_Santana[7]
                + player_3_Santana[12]
                + player_3_Santana[16]
            ) / (
                player_3_Santana[1]
                + player_3_Santana[6]
                + player_3_Santana[11]
                + player_3_Santana[15]
            )

            predicted_total_games_played = 143 - (
                (player_3_Santana[4] + player_3_Santana[9]) / 2
            )

        elif index == 3:
            batting = (
                player_4_Osuna[1]
                + player_4_Osuna[6]
                + player_4_Osuna[11]
                + player_4_Osuna[15]
            ) / (
                player_4_Osuna[0]
                + player_4_Osuna[5]
                + player_4_Osuna[10]
                + player_4_Osuna[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_4_Osuna[3]
                + player_4_Osuna[8]
                + player_4_Osuna[13]
                + player_4_Osuna[17]
            ) / (
                player_4_Osuna[1]
                + player_4_Osuna[6]
                + player_4_Osuna[11]
                + player_4_Osuna[15]
            )
            Homerun_to_hit_ratio = (
                player_4_Osuna[2]
                + player_4_Osuna[7]
                + player_4_Osuna[12]
                + player_4_Osuna[16]
            ) / (
                player_4_Osuna[1]
                + player_4_Osuna[6]
                + player_4_Osuna[11]
                + player_4_Osuna[15]
            )

            predicted_total_games_played = 143 - (
                (player_4_Osuna[4] + player_4_Osuna[9]) / 2
            )

        elif index == 4:
            batting = (
                player_5_Aoki[1]
                + player_5_Aoki[6]
                + player_5_Aoki[11]
                + player_5_Aoki[15]
            ) / (
                player_5_Aoki[0]
                + player_5_Aoki[5]
                + player_5_Aoki[10]
                + player_5_Aoki[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_5_Aoki[3]
                + player_5_Aoki[8]
                + player_5_Aoki[13]
                + player_5_Aoki[17]
            ) / (
                player_5_Aoki[1]
                + player_5_Aoki[6]
                + player_5_Aoki[11]
                + player_5_Aoki[15]
            )
            Homerun_to_hit_ratio = (
                player_5_Aoki[2]
                + player_5_Aoki[7]
                + player_5_Aoki[12]
                + player_5_Aoki[16]
            ) / (
                player_5_Aoki[1]
                + player_5_Aoki[6]
                + player_5_Aoki[11]
                + player_5_Aoki[15]
            )

            predicted_total_games_played = 143 - (
                (player_5_Aoki[4] + player_5_Aoki[9]) / 2
            )

        elif index == 5:
            batting = (
                player_6_Shiomi[1]
                + player_6_Shiomi[6]
                + player_6_Shiomi[11]
                + player_6_Shiomi[15]
            ) / (
                player_6_Shiomi[0]
                + player_6_Shiomi[5]
                + player_6_Shiomi[10]
                + player_6_Shiomi[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_6_Shiomi[3]
                + player_6_Shiomi[8]
                + player_6_Shiomi[13]
                + player_6_Shiomi[17]
            ) / (
                player_6_Shiomi[1]
                + player_6_Shiomi[6]
                + player_6_Shiomi[11]
                + player_6_Shiomi[15]
            )
            Homerun_to_hit_ratio = (
                player_6_Shiomi[2]
                + player_6_Shiomi[7]
                + player_6_Shiomi[12]
                + player_6_Shiomi[16]
            ) / (
                player_6_Shiomi[1]
                + player_6_Shiomi[6]
                + player_6_Shiomi[11]
                + player_6_Shiomi[15]
            )

            predicted_total_games_played = 143 - (
                (player_6_Shiomi[4] + player_6_Shiomi[9]) / 2
            )

        elif index == 6:
            batting = (
                player_7_Nakamura[1]
                + player_7_Nakamura[6]
                + player_7_Nakamura[11]
                + player_7_Nakamura[15]
            ) / (
                player_7_Nakamura[0]
                + player_7_Nakamura[5]
                + player_7_Nakamura[10]
                + player_7_Nakamura[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_7_Nakamura[3]
                + player_7_Nakamura[8]
                + player_7_Nakamura[13]
                + player_7_Nakamura[17]
            ) / (
                player_7_Nakamura[1]
                + player_7_Nakamura[6]
                + player_7_Nakamura[11]
                + player_7_Nakamura[15]
            )
            Homerun_to_hit_ratio = (
                player_7_Nakamura[2]
                + player_7_Nakamura[7]
                + player_7_Nakamura[12]
                + player_7_Nakamura[16]
            ) / (
                player_7_Nakamura[1]
                + player_7_Nakamura[6]
                + player_7_Nakamura[11]
                + player_7_Nakamura[15]
            )

            predicted_total_games_played = 143 - (
                (player_7_Nakamura[4] + player_7_Nakamura[9]) / 2
            )

        elif index == 7:
            batting = (
                player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11]
            ) / (player_8_Nagaoka[0] + player_8_Nagaoka[5] + player_8_Nagaoka[10])

            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_8_Nagaoka[3] + player_8_Nagaoka[8] + player_8_Nagaoka[13]
            ) / (player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11])

            Homerun_to_hit_ratio = (
                player_8_Nagaoka[2] + player_8_Nagaoka[7] + player_8_Nagaoka[12]
            ) / (player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11])

            predicted_total_games_played = 143 - (
                (player_8_Nagaoka[4] + player_8_Nagaoka[9]) / 2
            )

    else:
        data_win = c_14.fetchall()
        total_percentage = (
            data_win[0][1]
            + data_win[6][1]
            + data_win[12][1]
            + data_win[18][1]
            + data_win[24][1]
        ) / (
            data_win[0][1]
            + data_win[6][1]
            + data_win[12][1]
            + data_win[18][1]
            + data_win[24][1]
            + data_win[0][2]
            + data_win[6][2]
            + data_win[12][2]
            + data_win[18][2]
            + data_win[24][2]
        )

        if index == 0:
            batting = (
                player_1_Murakami[1]
                + player_1_Murakami[6]
                + player_1_Murakami[11]
                + player_1_Murakami[15]
                + player_1_Murakami[19]
            ) / (
                player_1_Murakami[0]
                + player_1_Murakami[5]
                + player_1_Murakami[10]
                + player_1_Murakami[14]
                + player_1_Murakami[18]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_1_Murakami[3]
                + player_1_Murakami[8]
                + player_1_Murakami[13]
                + player_1_Murakami[17]
                + player_1_Murakami[21]
            ) / (
                player_1_Murakami[1]
                + player_1_Murakami[6]
                + player_1_Murakami[11]
                + player_1_Murakami[15]
                + player_1_Murakami[19]
            )
            Homerun_to_hit_ratio = (
                player_1_Murakami[2]
                + player_1_Murakami[7]
                + player_1_Murakami[12]
                + player_1_Murakami[16]
                + player_1_Murakami[20]
            ) / (
                player_1_Murakami[1]
                + player_1_Murakami[6]
                + player_1_Murakami[11]
                + player_1_Murakami[15]
                + player_1_Murakami[19]
            )

            predicted_total_games_played = 143 - (
                (player_1_Murakami[4] + player_1_Murakami[9]) / 2
            )

        elif index == 1:

            batting = (
                player_2_Yamada[1]
                + player_2_Yamada[6]
                + player_2_Yamada[11]
                + player_2_Yamada[15]
                + player_2_Yamada[19]
            ) / (
                player_2_Yamada[0]
                + player_2_Yamada[5]
                + player_2_Yamada[10]
                + player_2_Yamada[14]
                + player_2_Yamada[18]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_2_Yamada[3]
                + player_2_Yamada[8]
                + player_2_Yamada[13]
                + player_2_Yamada[17]
                + player_2_Yamada[21]
            ) / (
                player_2_Yamada[1]
                + player_2_Yamada[6]
                + player_2_Yamada[11]
                + player_2_Yamada[15]
                + player_2_Yamada[19]
            )
            Homerun_to_hit_ratio = (
                player_2_Yamada[2]
                + player_2_Yamada[7]
                + player_2_Yamada[12]
                + player_2_Yamada[16]
                + player_2_Yamada[20]
            ) / (
                player_2_Yamada[1]
                + player_2_Yamada[6]
                + player_2_Yamada[11]
                + player_2_Yamada[15]
                + player_2_Yamada[19]
            )

            predicted_total_games_played = 143 - (
                (player_2_Yamada[4] + player_2_Yamada[9]) / 2
            )

        elif index == 2:
            batting = (
                player_3_Santana[1]
                + player_3_Santana[6]
                + player_3_Santana[11]
                + player_3_Santana[15]
            ) / (
                player_3_Santana[0]
                + player_3_Santana[5]
                + player_3_Santana[10]
                + player_3_Santana[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_3_Santana[3]
                + player_3_Santana[8]
                + player_3_Santana[13]
                + player_3_Santana[17]
            ) / (
                player_3_Santana[1]
                + player_3_Santana[6]
                + player_3_Santana[11]
                + player_3_Santana[15]
            )
            Homerun_to_hit_ratio = (
                player_3_Santana[2]
                + player_3_Santana[7]
                + player_3_Santana[12]
                + player_3_Santana[16]
            ) / (
                player_3_Santana[1]
                + player_3_Santana[6]
                + player_3_Santana[11]
                + player_3_Santana[15]
            )
            predicted_total_games_played = 143 - (
                (player_3_Santana[4] + player_3_Santana[9]) / 2
            )

        elif index == 3:

            batting = (
                player_4_Osuna[1]
                + player_4_Osuna[6]
                + player_4_Osuna[11]
                + player_4_Osuna[15]
            ) / (
                player_4_Osuna[0]
                + player_4_Osuna[5]
                + player_4_Osuna[10]
                + player_4_Osuna[14]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_4_Osuna[3]
                + player_4_Osuna[8]
                + player_4_Osuna[13]
                + player_4_Osuna[17]
            ) / (
                player_4_Osuna[1]
                + player_4_Osuna[6]
                + player_4_Osuna[11]
                + player_4_Osuna[15]
            )
            Homerun_to_hit_ratio = (
                player_4_Osuna[2]
                + player_4_Osuna[7]
                + player_4_Osuna[12]
                + player_4_Osuna[16]
            ) / (
                player_4_Osuna[1]
                + player_4_Osuna[6]
                + player_4_Osuna[11]
                + player_4_Osuna[15]
            )
            predicted_total_games_played = 143 - (
                (player_4_Osuna[4] + player_4_Osuna[9]) / 2
            )

        elif index == 4:

            batting = (
                player_5_Aoki[1]
                + player_5_Aoki[6]
                + player_5_Aoki[11]
                + player_5_Aoki[15]
                + player_5_Aoki[19]
                / (
                    player_5_Aoki[0]
                    + player_5_Aoki[5]
                    + player_5_Aoki[10]
                    + player_5_Aoki[14]
                    + player_5_Aoki[18]
                )
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_5_Aoki[3]
                + player_5_Aoki[8]
                + player_5_Aoki[13]
                + player_5_Aoki[17]
                + player_5_Aoki[21]
            ) / (
                player_5_Aoki[1]
                + player_5_Aoki[6]
                + player_5_Aoki[11]
                + player_5_Aoki[15]
                + player_5_Aoki[19]
            )
            Homerun_to_hit_ratio = (
                player_5_Aoki[2]
                + player_5_Aoki[7]
                + player_5_Aoki[12]
                + player_5_Aoki[16]
                + player_5_Aoki[20]
            ) / (
                player_5_Aoki[1]
                + player_5_Aoki[6]
                + player_5_Aoki[11]
                + player_5_Aoki[15]
                + player_5_Aoki[19]
            )

            predicted_total_games_played = 143 - (
                (player_5_Aoki[4] + player_5_Aoki[9]) / 2
            )

        elif index == 5:

            batting = (
                player_6_Shiomi[1]
                + player_6_Shiomi[6]
                + player_6_Shiomi[11]
                + player_6_Shiomi[15]
                + player_6_Shiomi[19]
            ) / (
                player_6_Shiomi[0]
                + player_6_Shiomi[5]
                + player_6_Shiomi[10]
                + player_6_Shiomi[14]
                + player_6_Shiomi[18]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

            RBI_to_hit_ratio = (
                player_6_Shiomi[3]
                + player_6_Shiomi[8]
                + player_6_Shiomi[13]
                + player_6_Shiomi[17]
                + player_6_Shiomi[21]
            ) / (
                player_6_Shiomi[1]
                + player_6_Shiomi[6]
                + player_6_Shiomi[11]
                + player_6_Shiomi[15]
                + player_6_Shiomi[19]
            )
            Homerun_to_hit_ratio = (
                player_6_Shiomi[2]
                + player_6_Shiomi[7]
                + player_6_Shiomi[12]
                + player_6_Shiomi[16]
                + player_6_Shiomi[20]
            ) / (
                player_6_Shiomi[1]
                + player_6_Shiomi[6]
                + player_6_Shiomi[11]
                + player_6_Shiomi[15]
                + player_6_Shiomi[19]
            )

            predicted_total_games_played = 143 - (
                (player_6_Shiomi[4] + player_6_Shiomi[9]) / 2
            )

        elif index == 6:

            batting = (
                player_7_Nakamura[1]
                + player_7_Nakamura[6]
                + player_7_Nakamura[11]
                + player_7_Nakamura[15]
                + player_7_Nakamura[19]
            ) / (
                player_7_Nakamura[0]
                + player_7_Nakamura[5]
                + player_7_Nakamura[10]
                + player_7_Nakamura[14]
                + player_7_Nakamura[18]
            )

            prob_4_4 = batting**4
            prob_4_3 = (batting**3) * (1 - batting) * 4
            prob_4_2 = (batting**2) * ((1 - batting) ** 2) * 6
            prob_4_1 = (batting) * ((1 - batting) ** 3) * 4
            RBI_to_hit_ratio = (
                player_7_Nakamura[3]
                + player_7_Nakamura[8]
                + player_7_Nakamura[13]
                + player_7_Nakamura[17]
                + player_7_Nakamura[21]
            ) / (
                player_7_Nakamura[1]
                + player_7_Nakamura[6]
                + player_7_Nakamura[11]
                + player_7_Nakamura[15]
                + player_7_Nakamura[19]
            )
            Homerun_to_hit_ratio = (
                player_7_Nakamura[2]
                + player_7_Nakamura[7]
                + player_7_Nakamura[12]
                + player_7_Nakamura[16]
                + player_7_Nakamura[20]
            ) / (
                player_7_Nakamura[1]
                + player_7_Nakamura[6]
                + player_7_Nakamura[11]
                + player_7_Nakamura[15]
                + player_7_Nakamura[19]
            )

            predicted_total_games_played = 143 - (
                (player_7_Nakamura[4] + player_7_Nakamura[9]) / 2
            )

        elif index == 7:
            batting = (
                player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11]
            ) / (player_8_Nagaoka[0] + player_8_Nagaoka[5] + player_8_Nagaoka[10])

            prob_4_4, prob_4_3, prob_4_2, prob_4_1 = (
                (batting**4),
                (batting**3) * (1 - batting) * 4,
                (batting**2) * ((1 - batting) ** 2) * 6,
                (batting) * ((1 - batting) ** 3) * 4,
            )

            RBI_to_hit_ratio = (
                player_8_Nagaoka[3] + player_8_Nagaoka[8] + player_8_Nagaoka[13]
            ) / (player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11])

            Homerun_to_hit_ratio = (
                player_8_Nagaoka[2] + player_8_Nagaoka[7] + player_8_Nagaoka[12]
            ) / (player_8_Nagaoka[1] + player_8_Nagaoka[6] + player_8_Nagaoka[11])

            predicted_total_games_played = 143 - (
                (player_8_Nagaoka[4] + player_8_Nagaoka[9]) / 2
            )

    probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
    total_predicted_hit = 0
    counter = 1

    for prob in probabilities:
        total_predicted_hit += predicted_total_games_played * prob * counter
        counter += 1

    total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio
    total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio

    f = RBI_to_hit_ratio

    Total_number_of_games_contribution = 0
    counter = 1

    for prob_2 in probabilities:
        Total_number_of_games_contribution += (
            predicted_total_games_played * prob_2 * (1 - (1 - f) ** counter)
        )
        counter += 1

    result = [
        round(batting, 3),
        int(total_predicted_homerun),
        int(total_predicted_RBI),
        int(total_predicted_hit),
        round(total_percentage, 3),
        round((1 - (prob_4_4 + prob_4_3 + prob_4_2 + prob_4_1)), 3),
        round(prob_4_1, 3),
        round(prob_4_2, 3),
        round(prob_4_3, 3),
        round(prob_4_4, 3),
        int(Total_number_of_games_contribution),
        int(Total_number_of_games_contribution * total_percentage),
    ]

    return result

    conn_1.commit()
    conn_1.close()
    conn_2.commit()
    conn_2.close()
    conn_3.commit()
    conn_3.close()
    conn_4.commit()
    conn_4.close()
    conn_5.commit()
    conn_5.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Murakami of against different teams


def Murakami(year):
    conn_6 = sqlite3.connect("Murakami_stats_by_team.db")
    c_6 = conn_6.cursor()
    c_6.execute("SELECT * from stats_one")
    data = c_6.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Murakami_calculations(
        batting_DB,
        batting_D,
        batting_T,
        batting_C,
        batting_G,
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
        win_percentage_DB,
        win_percentage_D,
        win_percentage_T,
        win_percentage_C,
        win_percentage_G,
    ):
        win = [
            win_percentage_DB,
            win_percentage_D,
            win_percentage_T,
            win_percentage_C,
            win_percentage_G,
        ]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [
            RBI_to_hit_ratio_DB,
            RBI_to_hit_ratio_D,
            RBI_to_hit_ratio_T,
            RBI_to_hit_ratio_C,
            RBI_to_hit_ratio_G,
        ]
        Homerun_to_hit_ratio = [
            Homerun_to_hit_ratio_DB,
            Homerun_to_hit_ratio_D,
            Homerun_to_hit_ratio_T,
            Homerun_to_hit_ratio_C,
            Homerun_to_hit_ratio_G,
        ]
        Predicted_homerun_by_team = []
        Predicted_RBI_by_team = []
        Predicted_hit_by_team = []
        Predicted_4_1_by_team = []
        Predicted_4_2_by_team = []
        Predicted_4_3_by_team = []
        Predicted_4_4_by_team = []
        Total_number_of_games_contribution_by_team = []
        Total_number_of_games_contribution_victory_by_team = []

        for i in range(5):
            prob_4_4 = batting[i] ** 4
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22

            probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
            total_predicted_hit = 0
            counter = 1

            for prob in probabilities:
                total_predicted_hit += predicted_total_games_played * prob * counter
                counter += 1

            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = 0
            counter = 1
            for prob_2 in probabilities:
                Total_number_of_games_contribution += (
                    prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
                )
                counter += 1

            Predicted_homerun_by_team.append(int(total_predicted_homerun))
            Predicted_RBI_by_team.append(int(total_predicted_RBI))
            Predicted_hit_by_team.append(int(total_predicted_hit))
            Predicted_4_1_by_team.append(round(prob_4_1, 3))
            Predicted_4_2_by_team.append(round(prob_4_2, 3))
            Predicted_4_3_by_team.append(round(prob_4_3, 3))
            Predicted_4_4_by_team.append(round(prob_4_4, 3))

            Total_number_of_games_contribution_by_team.append(
                int(Total_number_of_games_contribution)
            )

            Total_number_of_games_contribution_victory_by_team.append(
                int(Total_number_of_games_contribution * win[i])
            )
        return [
            Predicted_homerun_by_team,
            Predicted_RBI_by_team,
            Predicted_hit_by_team,
            Predicted_4_1_by_team,
            Predicted_4_2_by_team,
            Predicted_4_3_by_team,
            Predicted_4_4_by_team,
            Total_number_of_games_contribution_by_team,
            Total_number_of_games_contribution_victory_by_team,
        ]

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = (
        data[15][1],
        data[15][2],
        data[15][4],
        data[15][5],
    )
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = (
        data[20][1],
        data[20][2],
        data[20][4],
        data[20][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[11][4],
        data[11][5],
    )
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = (
        data[16][1],
        data[16][2],
        data[16][4],
        data[16][5],
    )
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = (
        data[21][1],
        data[21][2],
        data[21][4],
        data[21][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = (
        data[17][1],
        data[17][2],
        data[17][4],
        data[17][5],
    )
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = (
        data[22][1],
        data[22][2],
        data[22][4],
        data[22][5],
    )

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = (
        data[18][1],
        data[18][2],
        data[18][4],
        data[18][5],
    )
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = (
        data[23][1],
        data[23][2],
        data[23][4],
        data[23][5],
    )

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = (
        data[19][1],
        data[19][2],
        data[19][4],
        data[19][5],
    )
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = (
        data[24][1],
        data[24][2],
        data[24][4],
        data[24][5],
    )

    batting_DB_5 = (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB
    ) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB
    )
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    RBI_to_hit_ratio_DB_5 = (
        RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB
    )
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB_5 = (
        homerun_2024_DB
        + homerun_2023_DB
        + homerun_2022_DB
        + homerun_2021_DB
        + homerun_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D
    )
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D
    )
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    RBI_to_hit_ratio_D_5 = (
        RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D
    )
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D_5 = (
        homerun_2024_D
        + homerun_2023_D
        + homerun_2022_D
        + homerun_2021_D
        + homerun_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (
        homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T
    )
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T
    )
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    RBI_to_hit_ratio_T_5 = (
        RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T
    )
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T_5 = (
        homerun_2024_T
        + homerun_2023_T
        + homerun_2022_T
        + homerun_2021_T
        + homerun_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (
        homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C
    )
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C
    )
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    RBI_to_hit_ratio_C_5 = (
        RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C
    )
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C_5 = (
        homerun_2024_C
        + homerun_2023_C
        + homerun_2022_C
        + homerun_2021_C
        + homerun_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (
        homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G
    )
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G
    )
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )
    RBI_to_hit_ratio_G_5 = (
        RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G
    )
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G_5 = (
        homerun_2024_G
        + homerun_2023_G
        + homerun_2022_G
        + homerun_2021_G
        + homerun_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (
        homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_4_DB = (
        data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
    )
    win_percentage_5_DB = (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
        + data_win[25][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_4_D = (
        data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
    )
    win_percentage_5_D = (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
        + data_win[26][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_4_T = (
        data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
    )
    win_percentage_5_T = (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
        + data_win[27][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_4_C = (
        data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
    )
    win_percentage_5_C = (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
        + data_win[28][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )
    win_percentage_4_G = (
        data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
    )
    win_percentage_5_G = (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
        + data_win[29][2]
    )

    if year == 5:
        x = Murakami_calculations(
            batting_DB_5,
            batting_D_5,
            batting_T_5,
            batting_C_5,
            batting_G_5,
            RBI_to_hit_ratio_DB_5,
            RBI_to_hit_ratio_D_5,
            RBI_to_hit_ratio_T_5,
            RBI_to_hit_ratio_C_5,
            RBI_to_hit_ratio_G_5,
            Homerun_to_hit_ratio_DB_5,
            Homerun_to_hit_ratio_D_5,
            Homerun_to_hit_ratio_T_5,
            Homerun_to_hit_ratio_C_5,
            Homerun_to_hit_ratio_G_5,
            win_percentage_5_DB,
            win_percentage_5_D,
            win_percentage_5_T,
            win_percentage_5_C,
            win_percentage_5_G,
        )
        result_DB = [
            round(batting_DB_5, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_5_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_5, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_5_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_5, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_5_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_5, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_5_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_5, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_5_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    elif year == 4:
        x = Murakami_calculations(
            batting_DB_4,
            batting_D_4,
            batting_T_4,
            batting_C_4,
            batting_G_4,
            RBI_to_hit_ratio_DB_4,
            RBI_to_hit_ratio_D_4,
            RBI_to_hit_ratio_T_4,
            RBI_to_hit_ratio_C_4,
            RBI_to_hit_ratio_G_4,
            Homerun_to_hit_ratio_DB_4,
            Homerun_to_hit_ratio_D_4,
            Homerun_to_hit_ratio_T_4,
            Homerun_to_hit_ratio_C_4,
            Homerun_to_hit_ratio_G_4,
            win_percentage_4_DB,
            win_percentage_4_D,
            win_percentage_4_T,
            win_percentage_4_C,
            win_percentage_4_G,
        )
        result_DB = [
            round(batting_DB_4, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_4_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_4, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_4_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_4, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_4_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_4, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_4_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_4, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_4_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 3:
        x = Murakami_calculations(
            batting_DB_3,
            batting_D_3,
            batting_T_3,
            batting_C_3,
            batting_G_3,
            RBI_to_hit_ratio_DB_3,
            RBI_to_hit_ratio_D_3,
            RBI_to_hit_ratio_T_3,
            RBI_to_hit_ratio_C_3,
            RBI_to_hit_ratio_G_3,
            Homerun_to_hit_ratio_DB_3,
            Homerun_to_hit_ratio_D_3,
            Homerun_to_hit_ratio_T_3,
            Homerun_to_hit_ratio_C_3,
            Homerun_to_hit_ratio_G_3,
            win_percentage_3_DB,
            win_percentage_3_D,
            win_percentage_3_T,
            win_percentage_3_C,
            win_percentage_3_G,
        )
        result_DB = [
            round(batting_DB_3, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_3_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_3, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_3_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_3, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_3_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_3, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_3_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_3, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_3_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    conn_6.commit()
    conn_6.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Yamada of against different teams


def Yamada(year):
    conn_7 = sqlite3.connect("Yamada_stats_by_team.db")
    c_7 = conn_7.cursor()
    c_7.execute("SELECT * from stats_two")
    data = c_7.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Yamada_calculations(
        batting_DB,
        batting_D,
        batting_T,
        batting_C,
        batting_G,
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
        win_percentage_DB,
        win_percentage_D,
        win_percentage_T,
        win_percentage_C,
        win_percentage_G,
    ):
        win = [
            win_percentage_DB,
            win_percentage_D,
            win_percentage_T,
            win_percentage_C,
            win_percentage_G,
        ]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [
            RBI_to_hit_ratio_DB,
            RBI_to_hit_ratio_D,
            RBI_to_hit_ratio_T,
            RBI_to_hit_ratio_C,
            RBI_to_hit_ratio_G,
        ]
        Homerun_to_hit_ratio = [
            Homerun_to_hit_ratio_DB,
            Homerun_to_hit_ratio_D,
            Homerun_to_hit_ratio_T,
            Homerun_to_hit_ratio_C,
            Homerun_to_hit_ratio_G,
        ]
        Predicted_homerun_by_team = []
        Predicted_RBI_by_team = []
        Predicted_hit_by_team = []
        Predicted_4_1_by_team = []
        Predicted_4_2_by_team = []
        Predicted_4_3_by_team = []
        Predicted_4_4_by_team = []
        Total_number_of_games_contribution_by_team = []
        Total_number_of_games_contribution_victory_by_team = []

        for i in range(5):
            prob_4_4 = batting[i] ** 4
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
            total_predicted_hit = 0
            counter = 1

            for prob in probabilities:
                total_predicted_hit += predicted_total_games_played * prob * counter
                counter += 1

            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = 0
            counter = 1
            for prob_2 in probabilities:
                Total_number_of_games_contribution += (
                    prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
                )
                counter += 1
            Predicted_homerun_by_team.append(int(total_predicted_homerun))
            Predicted_RBI_by_team.append(int(total_predicted_RBI))
            Predicted_hit_by_team.append(int(total_predicted_hit))
            Predicted_4_1_by_team.append(round(prob_4_1, 3))
            Predicted_4_2_by_team.append(round(prob_4_2, 3))
            Predicted_4_3_by_team.append(round(prob_4_3, 3))
            Predicted_4_4_by_team.append(round(prob_4_4, 3))

            Total_number_of_games_contribution_by_team.append(
                int(Total_number_of_games_contribution)
            )

            Total_number_of_games_contribution_victory_by_team.append(
                int(Total_number_of_games_contribution * win[i])
            )
        return [
            Predicted_homerun_by_team,
            Predicted_RBI_by_team,
            Predicted_hit_by_team,
            Predicted_4_1_by_team,
            Predicted_4_2_by_team,
            Predicted_4_3_by_team,
            Predicted_4_4_by_team,
            Total_number_of_games_contribution_by_team,
            Total_number_of_games_contribution_victory_by_team,
        ]

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = (
        data[15][1],
        data[15][2],
        data[15][4],
        data[15][5],
    )
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = (
        data[20][1],
        data[20][2],
        data[20][4],
        data[20][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[11][4],
        data[11][5],
    )
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = (
        data[16][1],
        data[16][2],
        data[16][4],
        data[16][5],
    )
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = (
        data[21][1],
        data[21][2],
        data[21][4],
        data[21][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = (
        data[17][1],
        data[17][2],
        data[17][4],
        data[17][5],
    )
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = (
        data[22][1],
        data[22][2],
        data[22][4],
        data[22][5],
    )
    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = (
        data[18][1],
        data[18][2],
        data[18][4],
        data[18][5],
    )
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = (
        data[23][1],
        data[23][2],
        data[23][4],
        data[23][5],
    )

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = (
        data[19][1],
        data[19][2],
        data[19][4],
        data[19][5],
    )
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = (
        data[24][1],
        data[24][2],
        data[24][4],
        data[24][5],
    )

    batting_DB_5 = (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB
    ) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB
    )
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    RBI_to_hit_ratio_DB_5 = (
        RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB
    )
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB_5 = (
        homerun_2024_DB
        + homerun_2023_DB
        + homerun_2022_DB
        + homerun_2021_DB
        + homerun_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D
    )
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D
    )
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    RBI_to_hit_ratio_D_5 = (
        RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D
    )
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D_5 = (
        homerun_2024_D
        + homerun_2023_D
        + homerun_2022_D
        + homerun_2021_D
        + homerun_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (
        homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T
    )
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T
    )
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    RBI_to_hit_ratio_T_5 = (
        RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T
    )
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T_5 = (
        homerun_2024_T
        + homerun_2023_T
        + homerun_2022_T
        + homerun_2021_T
        + homerun_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (
        homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C
    )
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C
    )
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    RBI_to_hit_ratio_C_5 = (
        RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C
    )
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C_5 = (
        homerun_2024_C
        + homerun_2023_C
        + homerun_2022_C
        + homerun_2021_C
        + homerun_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (
        homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G
    )
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G
    )
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )
    RBI_to_hit_ratio_G_5 = (
        RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G
    )
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G_5 = (
        homerun_2024_G
        + homerun_2023_G
        + homerun_2022_G
        + homerun_2021_G
        + homerun_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (
        homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_4_DB = (
        data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
    )
    win_percentage_5_DB = (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
        + data_win[25][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_4_D = (
        data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
    )
    win_percentage_5_D = (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
        + data_win[26][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_4_T = (
        data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
    )
    win_percentage_5_T = (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
        + data_win[27][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_4_C = (
        data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
    )
    win_percentage_5_C = (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
        + data_win[28][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )
    win_percentage_4_G = (
        data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
    )
    win_percentage_5_G = (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
        + data_win[29][2]
    )

    if year == 5:
        x = Yamada_calculations(
            batting_DB_5,
            batting_D_5,
            batting_T_5,
            batting_C_5,
            batting_G_5,
            RBI_to_hit_ratio_DB_5,
            RBI_to_hit_ratio_D_5,
            RBI_to_hit_ratio_T_5,
            RBI_to_hit_ratio_C_5,
            RBI_to_hit_ratio_G_5,
            Homerun_to_hit_ratio_DB_5,
            Homerun_to_hit_ratio_D_5,
            Homerun_to_hit_ratio_T_5,
            Homerun_to_hit_ratio_C_5,
            Homerun_to_hit_ratio_G_5,
            win_percentage_5_DB,
            win_percentage_5_D,
            win_percentage_5_T,
            win_percentage_5_C,
            win_percentage_5_G,
        )
        result_DB = [
            round(batting_DB_5, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_5_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_5, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_5_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_5, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_5_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_5, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_5_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_5, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_5_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 4:
        x = Yamada_calculations(
            batting_DB_4,
            batting_D_4,
            batting_T_4,
            batting_C_4,
            batting_G_4,
            RBI_to_hit_ratio_DB_4,
            RBI_to_hit_ratio_D_4,
            RBI_to_hit_ratio_T_4,
            RBI_to_hit_ratio_C_4,
            RBI_to_hit_ratio_G_4,
            Homerun_to_hit_ratio_DB_4,
            Homerun_to_hit_ratio_D_4,
            Homerun_to_hit_ratio_T_4,
            Homerun_to_hit_ratio_C_4,
            Homerun_to_hit_ratio_G_4,
            win_percentage_4_DB,
            win_percentage_4_D,
            win_percentage_4_T,
            win_percentage_4_C,
            win_percentage_4_G,
        )
        result_DB = [
            round(batting_DB_4, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_4_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_4, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_4_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_4, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_4_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_4, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_4_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_4, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_4_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 3:
        x = Yamada_calculations(
            batting_DB_3,
            batting_D_3,
            batting_T_3,
            batting_C_3,
            batting_G_3,
            RBI_to_hit_ratio_DB_3,
            RBI_to_hit_ratio_D_3,
            RBI_to_hit_ratio_T_3,
            RBI_to_hit_ratio_C_3,
            RBI_to_hit_ratio_G_3,
            Homerun_to_hit_ratio_DB_3,
            Homerun_to_hit_ratio_D_3,
            Homerun_to_hit_ratio_T_3,
            Homerun_to_hit_ratio_C_3,
            Homerun_to_hit_ratio_G_3,
            win_percentage_3_DB,
            win_percentage_3_D,
            win_percentage_3_T,
            win_percentage_3_C,
            win_percentage_3_G,
        )
        result_DB = [
            round(batting_DB_3, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_3_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_3, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_3_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_3, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_3_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_3, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_3_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_3, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_3_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    conn_7.commit()
    conn_7.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Santana of against different teams


def Santana(year):
    conn_8 = sqlite3.connect("Santana_stats_by_team.db")
    c_8 = conn_8.cursor()
    c_8.execute("SELECT * from stats_three")
    data = c_8.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Santana_calculations(
        batting_DB,
        batting_D,
        batting_T,
        batting_C,
        batting_G,
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
        win_percentage_DB,
        win_percentage_D,
        win_percentage_T,
        win_percentage_C,
        win_percentage_G,
    ):
        win = [
            win_percentage_DB,
            win_percentage_D,
            win_percentage_T,
            win_percentage_C,
            win_percentage_G,
        ]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [
            RBI_to_hit_ratio_DB,
            RBI_to_hit_ratio_D,
            RBI_to_hit_ratio_T,
            RBI_to_hit_ratio_C,
            RBI_to_hit_ratio_G,
        ]
        Homerun_to_hit_ratio = [
            Homerun_to_hit_ratio_DB,
            Homerun_to_hit_ratio_D,
            Homerun_to_hit_ratio_T,
            Homerun_to_hit_ratio_C,
            Homerun_to_hit_ratio_G,
        ]
        Predicted_homerun_by_team = []
        Predicted_RBI_by_team = []
        Predicted_hit_by_team = []
        Predicted_4_1_by_team = []
        Predicted_4_2_by_team = []
        Predicted_4_3_by_team = []
        Predicted_4_4_by_team = []
        Total_number_of_games_contribution_by_team = []
        Total_number_of_games_contribution_victory_by_team = []

        for i in range(5):
            prob_4_4 = batting[i] ** 4
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
            total_predicted_hit = 0
            counter = 1

            for prob in probabilities:
                total_predicted_hit += predicted_total_games_played * prob * counter
                counter += 1

            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = 0
            counter = 1
            for prob_2 in probabilities:
                Total_number_of_games_contribution += (
                    prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
                )
                counter += 1
            Predicted_homerun_by_team.append(int(total_predicted_homerun))
            Predicted_RBI_by_team.append(int(total_predicted_RBI))
            Predicted_hit_by_team.append(int(total_predicted_hit))
            Predicted_4_1_by_team.append(round(prob_4_1, 3))
            Predicted_4_2_by_team.append(round(prob_4_2, 3))
            Predicted_4_3_by_team.append(round(prob_4_3, 3))
            Predicted_4_4_by_team.append(round(prob_4_4, 3))

            Total_number_of_games_contribution_by_team.append(
                int(Total_number_of_games_contribution)
            )

            Total_number_of_games_contribution_victory_by_team.append(
                int(Total_number_of_games_contribution * win[i])
            )
        return [
            Predicted_homerun_by_team,
            Predicted_RBI_by_team,
            Predicted_hit_by_team,
            Predicted_4_1_by_team,
            Predicted_4_2_by_team,
            Predicted_4_3_by_team,
            Predicted_4_4_by_team,
            Total_number_of_games_contribution_by_team,
            Total_number_of_games_contribution_victory_by_team,
        ]

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = (
        data[15][1],
        data[15][2],
        data[15][4],
        data[15][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[11][4],
        data[11][5],
    )
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = (
        data[16][1],
        data[16][2],
        data[16][4],
        data[16][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = (
        data[17][1],
        data[17][2],
        data[17][4],
        data[17][5],
    )

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = (
        data[18][1],
        data[18][2],
        data[18][4],
        data[18][5],
    )
    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = (
        data[19][1],
        data[19][2],
        data[19][4],
        data[19][5],
    )

    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB
    )
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB
    )
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB_4 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D
    )
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D
    )
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D_4 = (
        homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )

    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T
    )
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T
    )
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T_4 = (
        homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C
    )
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C
    )
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C_4 = (
        homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )

    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G
    )
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G
    )
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G_4 = (
        homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_4_DB = (
        data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_4_D = (
        data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_4_T = (
        data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_4_C = (
        data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )
    win_percentage_4_G = (
        data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
    )

    if year == 4 or year == 5:
        x = Santana_calculations(
            batting_DB_4,
            batting_D_4,
            batting_T_4,
            batting_C_4,
            batting_G_4,
            RBI_to_hit_ratio_DB_4,
            RBI_to_hit_ratio_D_4,
            RBI_to_hit_ratio_T_4,
            RBI_to_hit_ratio_C_4,
            RBI_to_hit_ratio_G_4,
            Homerun_to_hit_ratio_DB_4,
            Homerun_to_hit_ratio_D_4,
            Homerun_to_hit_ratio_T_4,
            Homerun_to_hit_ratio_C_4,
            Homerun_to_hit_ratio_G_4,
            win_percentage_4_DB,
            win_percentage_4_D,
            win_percentage_4_T,
            win_percentage_4_C,
            win_percentage_4_G,
        )
        result_DB = [
            round(batting_DB_4, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_4_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_4, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_4_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_4, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_4_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_4, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_4_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_4, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_4_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 3:
        x = Santana_calculations(
            batting_DB_3,
            batting_D_3,
            batting_T_3,
            batting_C_3,
            batting_G_3,
            RBI_to_hit_ratio_DB_3,
            RBI_to_hit_ratio_D_3,
            RBI_to_hit_ratio_T_3,
            RBI_to_hit_ratio_C_3,
            RBI_to_hit_ratio_G_3,
            Homerun_to_hit_ratio_DB_3,
            Homerun_to_hit_ratio_D_3,
            Homerun_to_hit_ratio_T_3,
            Homerun_to_hit_ratio_C_3,
            Homerun_to_hit_ratio_G_3,
            win_percentage_3_DB,
            win_percentage_3_D,
            win_percentage_3_T,
            win_percentage_3_C,
            win_percentage_3_G,
        )
        result_DB = [
            round(batting_DB_3, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_3_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_3, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_3_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_3, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_3_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_3, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_3_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_3, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_3_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    conn_8.commit()
    conn_8.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Osuna of against different teams


def Osuna(year):
    conn_9 = sqlite3.connect("Osuna_stats_by_team.db")
    c_9 = conn_9.cursor()
    c_9.execute("SELECT * from stats_four")
    data = c_9.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Osuna_calculations(
        batting_DB,
        batting_D,
        batting_T,
        batting_C,
        batting_G,
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
        win_percentage_DB,
        win_percentage_D,
        win_percentage_T,
        win_percentage_C,
        win_percentage_G,
    ):
        win = [
            win_percentage_DB,
            win_percentage_D,
            win_percentage_T,
            win_percentage_C,
            win_percentage_G,
        ]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [
            RBI_to_hit_ratio_DB,
            RBI_to_hit_ratio_D,
            RBI_to_hit_ratio_T,
            RBI_to_hit_ratio_C,
            RBI_to_hit_ratio_G,
        ]
        Homerun_to_hit_ratio = [
            Homerun_to_hit_ratio_DB,
            Homerun_to_hit_ratio_D,
            Homerun_to_hit_ratio_T,
            Homerun_to_hit_ratio_C,
            Homerun_to_hit_ratio_G,
        ]
        Predicted_homerun_by_team = []
        Predicted_RBI_by_team = []
        Predicted_hit_by_team = []
        Predicted_4_1_by_team = []
        Predicted_4_2_by_team = []
        Predicted_4_3_by_team = []
        Predicted_4_4_by_team = []
        Total_number_of_games_contribution_by_team = []
        Total_number_of_games_contribution_victory_by_team = []

        for i in range(5):
            prob_4_4 = batting[i] ** 4
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
            total_predicted_hit = 0
            counter = 1

            for prob in probabilities:
                total_predicted_hit += predicted_total_games_played * prob * counter
                counter += 1

            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = 0
            counter = 1
            for prob_2 in probabilities:
                Total_number_of_games_contribution += (
                    prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
                )
                counter += 1

            Predicted_homerun_by_team.append(int(total_predicted_homerun))
            Predicted_RBI_by_team.append(int(total_predicted_RBI))
            Predicted_hit_by_team.append(int(total_predicted_hit))
            Predicted_4_1_by_team.append(round(prob_4_1, 3))
            Predicted_4_2_by_team.append(round(prob_4_2, 3))
            Predicted_4_3_by_team.append(round(prob_4_3, 3))
            Predicted_4_4_by_team.append(round(prob_4_4, 3))

            Total_number_of_games_contribution_by_team.append(
                int(Total_number_of_games_contribution)
            )

            Total_number_of_games_contribution_victory_by_team.append(
                int(Total_number_of_games_contribution * win[i])
            )
        return [
            Predicted_homerun_by_team,
            Predicted_RBI_by_team,
            Predicted_hit_by_team,
            Predicted_4_1_by_team,
            Predicted_4_2_by_team,
            Predicted_4_3_by_team,
            Predicted_4_4_by_team,
            Total_number_of_games_contribution_by_team,
            Total_number_of_games_contribution_victory_by_team,
        ]

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = (
        data[15][1],
        data[15][2],
        data[15][4],
        data[15][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[11][4],
        data[11][5],
    )
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = (
        data[16][1],
        data[16][2],
        data[16][4],
        data[16][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = (
        data[17][1],
        data[17][2],
        data[17][4],
        data[17][5],
    )

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = (
        data[18][1],
        data[18][2],
        data[18][4],
        data[18][5],
    )
    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = (
        data[19][1],
        data[19][2],
        data[19][4],
        data[19][5],
    )

    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB
    )
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB
    )
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB_4 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D
    )
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D
    )
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D_4 = (
        homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )

    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T
    )
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T
    )
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T_4 = (
        homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C
    )
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C
    )
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C_4 = (
        homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )

    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G
    )
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G
    )
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G_4 = (
        homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_4_DB = (
        data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_4_D = (
        data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_4_T = (
        data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_4_C = (
        data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )
    win_percentage_4_G = (
        data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
    )

    if year == 4 or year == 5:
        x = Osuna_calculations(
            batting_DB_4,
            batting_D_4,
            batting_T_4,
            batting_C_4,
            batting_G_4,
            RBI_to_hit_ratio_DB_4,
            RBI_to_hit_ratio_D_4,
            RBI_to_hit_ratio_T_4,
            RBI_to_hit_ratio_C_4,
            RBI_to_hit_ratio_G_4,
            Homerun_to_hit_ratio_DB_4,
            Homerun_to_hit_ratio_D_4,
            Homerun_to_hit_ratio_T_4,
            Homerun_to_hit_ratio_C_4,
            Homerun_to_hit_ratio_G_4,
            win_percentage_4_DB,
            win_percentage_4_D,
            win_percentage_4_T,
            win_percentage_4_C,
            win_percentage_4_G,
        )
        result_DB = [
            round(batting_DB_4, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_4_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_4, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_4_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_4, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_4_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_4, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_4_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_4, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_4_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 3:
        x = Osuna_calculations(
            batting_DB_3,
            batting_D_3,
            batting_T_3,
            batting_C_3,
            batting_G_3,
            RBI_to_hit_ratio_DB_3,
            RBI_to_hit_ratio_D_3,
            RBI_to_hit_ratio_T_3,
            RBI_to_hit_ratio_C_3,
            RBI_to_hit_ratio_G_3,
            Homerun_to_hit_ratio_DB_3,
            Homerun_to_hit_ratio_D_3,
            Homerun_to_hit_ratio_T_3,
            Homerun_to_hit_ratio_C_3,
            Homerun_to_hit_ratio_G_3,
            win_percentage_3_DB,
            win_percentage_3_D,
            win_percentage_3_T,
            win_percentage_3_C,
            win_percentage_3_G,
        )
        result_DB = [
            round(batting_DB_3, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_3_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_3, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_3_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_3, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_3_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_3, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_3_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_3, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_3_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    conn_9.commit()
    conn_9.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Aoki of against different teams


def Aoki(year):
    conn_10 = sqlite3.connect("Aoki_stats_by_team.db")
    c_10 = conn_10.cursor()
    c_10.execute("SELECT * from stats_five")
    data = c_10.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Aoki_calculations(
        batting_DB,
        batting_D,
        batting_T,
        batting_C,
        batting_G,
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
        win_percentage_DB,
        win_percentage_D,
        win_percentage_T,
        win_percentage_C,
        win_percentage_G,
    ):
        win = [
            win_percentage_DB,
            win_percentage_D,
            win_percentage_T,
            win_percentage_C,
            win_percentage_G,
        ]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [
            RBI_to_hit_ratio_DB,
            RBI_to_hit_ratio_D,
            RBI_to_hit_ratio_T,
            RBI_to_hit_ratio_C,
            RBI_to_hit_ratio_G,
        ]
        Homerun_to_hit_ratio = [
            Homerun_to_hit_ratio_DB,
            Homerun_to_hit_ratio_D,
            Homerun_to_hit_ratio_T,
            Homerun_to_hit_ratio_C,
            Homerun_to_hit_ratio_G,
        ]
        Predicted_homerun_by_team = []
        Predicted_RBI_by_team = []
        Predicted_hit_by_team = []
        Predicted_4_1_by_team = []
        Predicted_4_2_by_team = []
        Predicted_4_3_by_team = []
        Predicted_4_4_by_team = []
        Total_number_of_games_contribution_by_team = []
        Total_number_of_games_contribution_victory_by_team = []

        for i in range(5):
            prob_4_4 = batting[i] ** 4
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
            total_predicted_hit = 0
            counter = 1

            for prob in probabilities:
                total_predicted_hit += predicted_total_games_played * prob * counter
                counter += 1

            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = 0
            counter = 1
            for prob_2 in probabilities:
                Total_number_of_games_contribution += (
                    prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
                )
                counter += 1

            Predicted_homerun_by_team.append(int(total_predicted_homerun))
            Predicted_RBI_by_team.append(int(total_predicted_RBI))
            Predicted_hit_by_team.append(int(total_predicted_hit))
            Predicted_4_1_by_team.append(round(prob_4_1, 3))
            Predicted_4_2_by_team.append(round(prob_4_2, 3))
            Predicted_4_3_by_team.append(round(prob_4_3, 3))
            Predicted_4_4_by_team.append(round(prob_4_4, 3))

            Total_number_of_games_contribution_by_team.append(
                int(Total_number_of_games_contribution)
            )

            Total_number_of_games_contribution_victory_by_team.append(
                int(Total_number_of_games_contribution * win[i])
            )
        return [
            Predicted_homerun_by_team,
            Predicted_RBI_by_team,
            Predicted_hit_by_team,
            Predicted_4_1_by_team,
            Predicted_4_2_by_team,
            Predicted_4_3_by_team,
            Predicted_4_4_by_team,
            Total_number_of_games_contribution_by_team,
            Total_number_of_games_contribution_victory_by_team,
        ]

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = (
        data[15][1],
        data[15][2],
        data[15][4],
        data[15][5],
    )
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = (
        data[20][1],
        data[20][2],
        data[20][4],
        data[20][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[11][4],
        data[11][5],
    )
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = (
        data[16][1],
        data[16][2],
        data[16][4],
        data[16][5],
    )
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = (
        data[21][1],
        data[21][2],
        data[21][4],
        data[21][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = (
        data[17][1],
        data[17][2],
        data[17][4],
        data[17][5],
    )
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = (
        data[22][1],
        data[22][2],
        data[22][4],
        data[22][5],
    )

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = (
        data[18][1],
        data[18][2],
        data[18][4],
        data[18][5],
    )
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = (
        data[23][1],
        data[23][2],
        data[23][4],
        data[23][5],
    )

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = (
        data[19][1],
        data[19][2],
        data[19][4],
        data[19][5],
    )
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = (
        data[24][1],
        data[24][2],
        data[24][4],
        data[24][5],
    )

    batting_DB_5 = (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB
    ) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB
    )
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    RBI_to_hit_ratio_DB_5 = (
        RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB
    )
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB_5 = (
        homerun_2024_DB
        + homerun_2023_DB
        + homerun_2022_DB
        + homerun_2021_DB
        + homerun_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D
    )
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D
    )
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    RBI_to_hit_ratio_D_5 = (
        RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D
    )
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D_5 = (
        homerun_2024_D
        + homerun_2023_D
        + homerun_2022_D
        + homerun_2021_D
        + homerun_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (
        homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T
    )
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T
    )
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    RBI_to_hit_ratio_T_5 = (
        RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T
    )
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T_5 = (
        homerun_2024_T
        + homerun_2023_T
        + homerun_2022_T
        + homerun_2021_T
        + homerun_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (
        homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C
    )
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C
    )
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    RBI_to_hit_ratio_C_5 = (
        RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C
    )
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C_5 = (
        homerun_2024_C
        + homerun_2023_C
        + homerun_2022_C
        + homerun_2021_C
        + homerun_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (
        homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G
    )
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G
    )
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )
    RBI_to_hit_ratio_G_5 = (
        RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G
    )
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G_5 = (
        homerun_2024_G
        + homerun_2023_G
        + homerun_2022_G
        + homerun_2021_G
        + homerun_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (
        homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_4_DB = (
        data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
    )
    win_percentage_5_DB = (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
        + data_win[25][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_4_D = (
        data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
    )
    win_percentage_5_D = (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
        + data_win[26][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_4_T = (
        data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
    )
    win_percentage_5_T = (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
        + data_win[27][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_4_C = (
        data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
    )
    win_percentage_5_C = (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
        + data_win[28][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )
    win_percentage_4_G = (
        data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
    )
    win_percentage_5_G = (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
        + data_win[29][2]
    )

    if year == 5:
        x = Aoki_calculations(
            batting_DB_5,
            batting_D_5,
            batting_T_5,
            batting_C_5,
            batting_G_5,
            RBI_to_hit_ratio_DB_5,
            RBI_to_hit_ratio_D_5,
            RBI_to_hit_ratio_T_5,
            RBI_to_hit_ratio_C_5,
            RBI_to_hit_ratio_G_5,
            Homerun_to_hit_ratio_DB_5,
            Homerun_to_hit_ratio_D_5,
            Homerun_to_hit_ratio_T_5,
            Homerun_to_hit_ratio_C_5,
            Homerun_to_hit_ratio_G_5,
            win_percentage_5_DB,
            win_percentage_5_D,
            win_percentage_5_T,
            win_percentage_5_C,
            win_percentage_5_G,
        )
        result_DB = [
            round(batting_DB_5, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_5_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_5, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_5_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_5, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_5_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_5, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_5_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_5, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_5_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 4:
        x = Aoki_calculations(
            batting_DB_4,
            batting_D_4,
            batting_T_4,
            batting_C_4,
            batting_G_4,
            RBI_to_hit_ratio_DB_4,
            RBI_to_hit_ratio_D_4,
            RBI_to_hit_ratio_T_4,
            RBI_to_hit_ratio_C_4,
            RBI_to_hit_ratio_G_4,
            Homerun_to_hit_ratio_DB_4,
            Homerun_to_hit_ratio_D_4,
            Homerun_to_hit_ratio_T_4,
            Homerun_to_hit_ratio_C_4,
            Homerun_to_hit_ratio_G_4,
            win_percentage_4_DB,
            win_percentage_4_D,
            win_percentage_4_T,
            win_percentage_4_C,
            win_percentage_4_G,
        )
        result_DB = [
            round(batting_DB_4, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_4_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_4, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_4_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_4, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_4_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_4, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_4_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_4, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_4_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 3:
        x = Aoki_calculations(
            batting_DB_3,
            batting_D_3,
            batting_T_3,
            batting_C_3,
            batting_G_3,
            RBI_to_hit_ratio_DB_3,
            RBI_to_hit_ratio_D_3,
            RBI_to_hit_ratio_T_3,
            RBI_to_hit_ratio_C_3,
            RBI_to_hit_ratio_G_3,
            Homerun_to_hit_ratio_DB_3,
            Homerun_to_hit_ratio_D_3,
            Homerun_to_hit_ratio_T_3,
            Homerun_to_hit_ratio_C_3,
            Homerun_to_hit_ratio_G_3,
            win_percentage_3_DB,
            win_percentage_3_D,
            win_percentage_3_T,
            win_percentage_3_C,
            win_percentage_3_G,
        )
        result_DB = [
            round(batting_DB_3, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_3_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_3, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_3_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_3, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_3_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_3, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_3_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_3, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_3_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    conn_10.commit()
    conn_10.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Shiomi of against different teams


def Shiomi(year):
    conn_11 = sqlite3.connect("Shiomi_stats_by_team.db")
    c_11 = conn_11.cursor()
    c_11.execute("SELECT * from stats_six")
    data = c_11.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Shiomi_calculations(
        batting_DB,
        batting_D,
        batting_T,
        batting_C,
        batting_G,
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
        win_percentage_DB,
        win_percentage_D,
        win_percentage_T,
        win_percentage_C,
        win_percentage_G,
    ):
        win = [
            win_percentage_DB,
            win_percentage_D,
            win_percentage_T,
            win_percentage_C,
            win_percentage_G,
        ]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [
            RBI_to_hit_ratio_DB,
            RBI_to_hit_ratio_D,
            RBI_to_hit_ratio_T,
            RBI_to_hit_ratio_C,
            RBI_to_hit_ratio_G,
        ]
        Homerun_to_hit_ratio = [
            Homerun_to_hit_ratio_DB,
            Homerun_to_hit_ratio_D,
            Homerun_to_hit_ratio_T,
            Homerun_to_hit_ratio_C,
            Homerun_to_hit_ratio_G,
        ]
        Predicted_homerun_by_team = []
        Predicted_RBI_by_team = []
        Predicted_hit_by_team = []
        Predicted_4_1_by_team = []
        Predicted_4_2_by_team = []
        Predicted_4_3_by_team = []
        Predicted_4_4_by_team = []
        Total_number_of_games_contribution_by_team = []
        Total_number_of_games_contribution_victory_by_team = []

        for i in range(5):
            prob_4_4 = batting[i] ** 4
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
            total_predicted_hit = 0
            counter = 1

            for prob in probabilities:
                total_predicted_hit += predicted_total_games_played * prob * counter
                counter += 1

            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = 0
            counter = 1
            for prob_2 in probabilities:
                Total_number_of_games_contribution += (
                    prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
                )
                counter += 1

            Predicted_homerun_by_team.append(int(total_predicted_homerun))
            Predicted_RBI_by_team.append(int(total_predicted_RBI))
            Predicted_hit_by_team.append(int(total_predicted_hit))
            Predicted_4_1_by_team.append(round(prob_4_1, 3))
            Predicted_4_2_by_team.append(round(prob_4_2, 3))
            Predicted_4_3_by_team.append(round(prob_4_3, 3))
            Predicted_4_4_by_team.append(round(prob_4_4, 3))
            Total_number_of_games_contribution_by_team.append(
                int(Total_number_of_games_contribution)
            )

            Total_number_of_games_contribution_victory_by_team.append(
                int(Total_number_of_games_contribution * win[i])
            )
        return [
            Predicted_homerun_by_team,
            Predicted_RBI_by_team,
            Predicted_hit_by_team,
            Predicted_4_1_by_team,
            Predicted_4_2_by_team,
            Predicted_4_3_by_team,
            Predicted_4_4_by_team,
            Total_number_of_games_contribution_by_team,
            Total_number_of_games_contribution_victory_by_team,
        ]

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = (
        data[15][1],
        data[15][2],
        data[15][4],
        data[15][5],
    )
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = (
        data[20][1],
        data[20][2],
        data[20][4],
        data[20][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[11][4],
        data[11][5],
    )
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = (
        data[16][1],
        data[16][2],
        data[16][4],
        data[16][5],
    )
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = (
        data[21][1],
        data[21][2],
        data[21][4],
        data[21][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = (
        data[17][1],
        data[17][2],
        data[17][4],
        data[17][5],
    )
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = (
        data[22][1],
        data[22][2],
        data[22][4],
        data[22][5],
    )

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = (
        data[18][1],
        data[18][2],
        data[18][4],
        data[18][5],
    )
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = (
        data[23][1],
        data[23][2],
        data[23][4],
        data[23][5],
    )

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = (
        data[19][1],
        data[19][2],
        data[19][4],
        data[19][5],
    )
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = (
        data[24][1],
        data[24][2],
        data[24][4],
        data[24][5],
    )

    batting_DB_5 = (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB
    ) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB
    )
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    RBI_to_hit_ratio_DB_5 = (
        RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB
    )
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB_5 = (
        homerun_2024_DB
        + homerun_2023_DB
        + homerun_2022_DB
        + homerun_2021_DB
        + homerun_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D
    )
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D
    )
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    RBI_to_hit_ratio_D_5 = (
        RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D
    )
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D_5 = (
        homerun_2024_D
        + homerun_2023_D
        + homerun_2022_D
        + homerun_2021_D
        + homerun_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (
        homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T
    )
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T
    )
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    RBI_to_hit_ratio_T_5 = (
        RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T
    )
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T_5 = (
        homerun_2024_T
        + homerun_2023_T
        + homerun_2022_T
        + homerun_2021_T
        + homerun_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (
        homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C
    )
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C
    )
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    RBI_to_hit_ratio_C_5 = (
        RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C
    )
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C_5 = (
        homerun_2024_C
        + homerun_2023_C
        + homerun_2022_C
        + homerun_2021_C
        + homerun_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (
        homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G
    )
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G
    )
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )
    RBI_to_hit_ratio_G_5 = (
        RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G
    )
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G_5 = (
        homerun_2024_G
        + homerun_2023_G
        + homerun_2022_G
        + homerun_2021_G
        + homerun_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (
        homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_4_DB = (
        data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
    )
    win_percentage_5_DB = (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
        + data_win[25][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_4_D = (
        data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
    )
    win_percentage_5_D = (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
        + data_win[26][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_4_T = (
        data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
    )
    win_percentage_5_T = (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
        + data_win[27][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_4_C = (
        data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
    )
    win_percentage_5_C = (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
        + data_win[28][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )
    win_percentage_4_G = (
        data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
    )
    win_percentage_5_G = (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
        + data_win[29][2]
    )

    if year == 5:
        x = Shiomi_calculations(
            batting_DB_5,
            batting_D_5,
            batting_T_5,
            batting_C_5,
            batting_G_5,
            RBI_to_hit_ratio_DB_5,
            RBI_to_hit_ratio_D_5,
            RBI_to_hit_ratio_T_5,
            RBI_to_hit_ratio_C_5,
            RBI_to_hit_ratio_G_5,
            Homerun_to_hit_ratio_DB_5,
            Homerun_to_hit_ratio_D_5,
            Homerun_to_hit_ratio_T_5,
            Homerun_to_hit_ratio_C_5,
            Homerun_to_hit_ratio_G_5,
            win_percentage_5_DB,
            win_percentage_5_D,
            win_percentage_5_T,
            win_percentage_5_C,
            win_percentage_5_G,
        )
        result_DB = [
            round(batting_DB_5, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_5_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_5, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_5_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_5, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_5_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_5, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_5_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_5, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_5_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 4:
        x = Shiomi_calculations(
            batting_DB_4,
            batting_D_4,
            batting_T_4,
            batting_C_4,
            batting_G_4,
            RBI_to_hit_ratio_DB_4,
            RBI_to_hit_ratio_D_4,
            RBI_to_hit_ratio_T_4,
            RBI_to_hit_ratio_C_4,
            RBI_to_hit_ratio_G_4,
            Homerun_to_hit_ratio_DB_4,
            Homerun_to_hit_ratio_D_4,
            Homerun_to_hit_ratio_T_4,
            Homerun_to_hit_ratio_C_4,
            Homerun_to_hit_ratio_G_4,
            win_percentage_4_DB,
            win_percentage_4_D,
            win_percentage_4_T,
            win_percentage_4_C,
            win_percentage_4_G,
        )
        result_DB = [
            round(batting_DB_4, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_4_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_4, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_4_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_4, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_4_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_4, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_4_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_4, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_4_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 3:
        x = Shiomi_calculations(
            batting_DB_3,
            batting_D_3,
            batting_T_3,
            batting_C_3,
            batting_G_3,
            RBI_to_hit_ratio_DB_3,
            RBI_to_hit_ratio_D_3,
            RBI_to_hit_ratio_T_3,
            RBI_to_hit_ratio_C_3,
            RBI_to_hit_ratio_G_3,
            Homerun_to_hit_ratio_DB_3,
            Homerun_to_hit_ratio_D_3,
            Homerun_to_hit_ratio_T_3,
            Homerun_to_hit_ratio_C_3,
            Homerun_to_hit_ratio_G_3,
            win_percentage_3_DB,
            win_percentage_3_D,
            win_percentage_3_T,
            win_percentage_3_C,
            win_percentage_3_G,
        )
        result_DB = [
            round(batting_DB_3, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_3_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_3, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_3_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_3, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_3_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_3, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_3_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_3, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_3_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    conn_11.commit()
    conn_11.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Nakamura of against different teams


def Nakamura(year):
    conn_12 = sqlite3.connect("Nakamura_stats_by_team.db")
    c_12 = conn_12.cursor()
    c_12.execute("SELECT * from stats_seven")
    data = c_12.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Nakamura_calculations(
        batting_DB,
        batting_D,
        batting_T,
        batting_C,
        batting_G,
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
        win_percentage_DB,
        win_percentage_D,
        win_percentage_T,
        win_percentage_C,
        win_percentage_G,
    ):
        win = [
            win_percentage_DB,
            win_percentage_D,
            win_percentage_T,
            win_percentage_C,
            win_percentage_G,
        ]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [
            RBI_to_hit_ratio_DB,
            RBI_to_hit_ratio_D,
            RBI_to_hit_ratio_T,
            RBI_to_hit_ratio_C,
            RBI_to_hit_ratio_G,
        ]
        Homerun_to_hit_ratio = [
            Homerun_to_hit_ratio_DB,
            Homerun_to_hit_ratio_D,
            Homerun_to_hit_ratio_T,
            Homerun_to_hit_ratio_C,
            Homerun_to_hit_ratio_G,
        ]
        Predicted_homerun_by_team = []
        Predicted_RBI_by_team = []
        Predicted_hit_by_team = []
        Predicted_4_1_by_team = []
        Predicted_4_2_by_team = []
        Predicted_4_3_by_team = []
        Predicted_4_4_by_team = []
        Total_number_of_games_contribution_by_team = []
        Total_number_of_games_contribution_victory_by_team = []

        for i in range(5):
            prob_4_4 = batting[i] ** 4
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
            total_predicted_hit = 0
            counter = 1

            for prob in probabilities:
                total_predicted_hit += predicted_total_games_played * prob * counter
                counter += 1

            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = 0
            counter = 1
            for prob_2 in probabilities:
                Total_number_of_games_contribution += (
                    prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
                )
                counter += 1

            Predicted_homerun_by_team.append(int(total_predicted_homerun))
            Predicted_RBI_by_team.append(int(total_predicted_RBI))
            Predicted_hit_by_team.append(int(total_predicted_hit))
            Predicted_4_1_by_team.append(round(prob_4_1, 3))
            Predicted_4_2_by_team.append(round(prob_4_2, 3))
            Predicted_4_3_by_team.append(round(prob_4_3, 3))
            Predicted_4_4_by_team.append(round(prob_4_4, 3))
            Total_number_of_games_contribution_by_team.append(
                int(Total_number_of_games_contribution)
            )

            Total_number_of_games_contribution_victory_by_team.append(
                int(Total_number_of_games_contribution * win[i])
            )
        return [
            Predicted_homerun_by_team,
            Predicted_RBI_by_team,
            Predicted_hit_by_team,
            Predicted_4_1_by_team,
            Predicted_4_2_by_team,
            Predicted_4_3_by_team,
            Predicted_4_4_by_team,
            Total_number_of_games_contribution_by_team,
            Total_number_of_games_contribution_victory_by_team,
        ]

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = (
        data[15][1],
        data[15][2],
        data[15][4],
        data[15][5],
    )
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = (
        data[20][1],
        data[20][2],
        data[20][4],
        data[20][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[11][4],
        data[11][5],
    )
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = (
        data[16][1],
        data[16][2],
        data[16][4],
        data[16][5],
    )
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = (
        data[21][1],
        data[21][2],
        data[21][4],
        data[21][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = (
        data[17][1],
        data[17][2],
        data[17][4],
        data[17][5],
    )
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = (
        data[22][1],
        data[22][2],
        data[22][4],
        data[22][5],
    )

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = (
        data[18][1],
        data[18][2],
        data[18][4],
        data[18][5],
    )
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = (
        data[23][1],
        data[23][2],
        data[23][4],
        data[23][5],
    )

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = (
        data[19][1],
        data[19][2],
        data[19][4],
        data[19][5],
    )
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = (
        data[24][1],
        data[24][2],
        data[24][4],
        data[24][5],
    )

    batting_DB_5 = (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB
    ) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB
    )
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    RBI_to_hit_ratio_DB_5 = (
        RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB
    )
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB_5 = (
        homerun_2024_DB
        + homerun_2023_DB
        + homerun_2022_DB
        + homerun_2021_DB
        + homerun_2020_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (
        homerun_2024_DB + homerun_2023_DB + homerun_2022_DB
    ) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D
    )
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D
    )
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    RBI_to_hit_ratio_D_5 = (
        RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D
    )
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D_5 = (
        homerun_2024_D
        + homerun_2023_D
        + homerun_2022_D
        + homerun_2021_D
        + homerun_2020_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (
        homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D
    ) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T
    )
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T
    )
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    RBI_to_hit_ratio_T_5 = (
        RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T
    )
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T_5 = (
        homerun_2024_T
        + homerun_2023_T
        + homerun_2022_T
        + homerun_2021_T
        + homerun_2020_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (
        homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T
    ) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C
    )
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C
    )
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    RBI_to_hit_ratio_C_5 = (
        RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C
    )
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C_5 = (
        homerun_2024_C
        + homerun_2023_C
        + homerun_2022_C
        + homerun_2021_C
        + homerun_2020_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (
        homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C
    ) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G
    )
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G
    )
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )
    RBI_to_hit_ratio_G_5 = (
        RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G
    )
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G_5 = (
        homerun_2024_G
        + homerun_2023_G
        + homerun_2022_G
        + homerun_2021_G
        + homerun_2020_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (
        homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G
    ) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_4_DB = (
        data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
    )
    win_percentage_5_DB = (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
    ) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[19][1]
        + data_win[25][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
        + data_win[19][2]
        + data_win[25][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_4_D = (
        data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
    )
    win_percentage_5_D = (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
    ) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[20][1]
        + data_win[26][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
        + data_win[20][2]
        + data_win[26][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_4_T = (
        data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
    )
    win_percentage_5_T = (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
    ) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[21][1]
        + data_win[27][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
        + data_win[21][2]
        + data_win[27][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_4_C = (
        data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
    )
    win_percentage_5_C = (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
    ) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[22][1]
        + data_win[28][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
        + data_win[22][2]
        + data_win[28][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )
    win_percentage_4_G = (
        data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
    )
    win_percentage_5_G = (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
    ) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[23][1]
        + data_win[29][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
        + data_win[23][2]
        + data_win[29][2]
    )

    if year == 5:
        x = Nakamura_calculations(
            batting_DB_5,
            batting_D_5,
            batting_T_5,
            batting_C_5,
            batting_G_5,
            RBI_to_hit_ratio_DB_5,
            RBI_to_hit_ratio_D_5,
            RBI_to_hit_ratio_T_5,
            RBI_to_hit_ratio_C_5,
            RBI_to_hit_ratio_G_5,
            Homerun_to_hit_ratio_DB_5,
            Homerun_to_hit_ratio_D_5,
            Homerun_to_hit_ratio_T_5,
            Homerun_to_hit_ratio_C_5,
            Homerun_to_hit_ratio_G_5,
            win_percentage_5_DB,
            win_percentage_5_D,
            win_percentage_5_T,
            win_percentage_5_C,
            win_percentage_5_G,
        )
        result_DB = [
            round(batting_DB_5, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_5_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_5, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_5_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_5, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_5_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_5, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_5_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_5, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_5_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 4:
        x = Nakamura_calculations(
            batting_DB_4,
            batting_D_4,
            batting_T_4,
            batting_C_4,
            batting_G_4,
            RBI_to_hit_ratio_DB_4,
            RBI_to_hit_ratio_D_4,
            RBI_to_hit_ratio_T_4,
            RBI_to_hit_ratio_C_4,
            RBI_to_hit_ratio_G_4,
            Homerun_to_hit_ratio_DB_4,
            Homerun_to_hit_ratio_D_4,
            Homerun_to_hit_ratio_T_4,
            Homerun_to_hit_ratio_C_4,
            Homerun_to_hit_ratio_G_4,
            win_percentage_4_DB,
            win_percentage_4_D,
            win_percentage_4_T,
            win_percentage_4_C,
            win_percentage_4_G,
        )
        result_DB = [
            round(batting_DB_4, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_4_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_4, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_4_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_4, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_4_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_4, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_4_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_4, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_4_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]
    elif year == 3:
        x = Nakamura_calculations(
            batting_DB_3,
            batting_D_3,
            batting_T_3,
            batting_C_3,
            batting_G_3,
            RBI_to_hit_ratio_DB_3,
            RBI_to_hit_ratio_D_3,
            RBI_to_hit_ratio_T_3,
            RBI_to_hit_ratio_C_3,
            RBI_to_hit_ratio_G_3,
            Homerun_to_hit_ratio_DB_3,
            Homerun_to_hit_ratio_D_3,
            Homerun_to_hit_ratio_T_3,
            Homerun_to_hit_ratio_C_3,
            Homerun_to_hit_ratio_G_3,
            win_percentage_3_DB,
            win_percentage_3_D,
            win_percentage_3_T,
            win_percentage_3_C,
            win_percentage_3_G,
        )
        result_DB = [
            round(batting_DB_3, 3),
            int(x[0][0]),
            int(x[1][0]),
            int(x[2][0]),
            round(win_percentage_3_DB, 3),
            round(1 - (x[3][0] + x[4][0] + x[5][0] + x[6][0]), 3),
            round(x[3][0], 3),
            round(x[4][0], 3),
            round(x[5][0], 3),
            round(x[6][0], 3),
            int(x[7][0]),
            int(x[8][0]),
        ]
        result_D = [
            round(batting_D_3, 3),
            int(x[0][1]),
            int(x[1][1]),
            int(x[2][1]),
            round(win_percentage_3_D, 3),
            round(1 - (x[3][1] + x[4][1] + x[5][1] + x[6][1]), 3),
            round(x[3][1], 3),
            round(x[4][1], 3),
            round(x[5][1], 3),
            round(x[6][1], 3),
            int(x[7][1]),
            int(x[8][1]),
        ]
        result_T = [
            round(batting_T_3, 3),
            int(x[0][2]),
            int(x[1][2]),
            int(x[2][2]),
            round(win_percentage_3_T, 3),
            round(1 - (x[3][2] + x[4][2] + x[5][2] + x[6][2]), 3),
            round(x[3][2], 3),
            round(x[4][2], 3),
            round(x[5][2], 3),
            round(x[6][2], 3),
            int(x[7][2]),
            int(x[8][2]),
        ]
        result_C = [
            round(batting_C_3, 3),
            int(x[0][3]),
            int(x[1][3]),
            int(x[2][3]),
            round(win_percentage_3_C, 3),
            round(1 - (x[3][3] + x[4][3] + x[5][3] + x[6][3]), 3),
            round(x[3][3], 3),
            round(x[4][3], 3),
            round(x[5][3], 3),
            round(x[6][3], 3),
            int(x[7][3]),
            int(x[8][3]),
        ]
        result_G = [
            round(batting_G_3, 3),
            int(x[0][4]),
            int(x[1][4]),
            int(x[2][4]),
            round(win_percentage_3_G, 3),
            round(1 - (x[3][4] + x[4][4] + x[5][4] + x[6][4]), 3),
            round(x[3][4], 3),
            round(x[4][4], 3),
            round(x[5][4], 3),
            round(x[6][4], 3),
            int(x[7][4]),
            int(x[8][4]),
        ]
        return [result_DB, result_D, result_T, result_C, result_G]

    conn_6.commit()
    conn_6.close()
    conn_14.commit()
    conn_14.close()

    # Calculation for Nagaoka of against different teams


def Nagaoka():
    conn_13 = sqlite3.connect("Nagaoka_stats_by_team.db")
    c_13 = conn_13.cursor()
    c_13.execute("SELECT * from stats_eight")
    data = c_13.fetchall()
    conn_14 = sqlite3.connect("Win_lose_by_opponent.db")
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = (
        data[0][1],
        data[0][2],
        data[0][4],
        data[0][5],
    )
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = (
        data[5][1],
        data[5][2],
        data[5][4],
        data[5][5],
    )
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = (
        data[10][1],
        data[10][2],
        data[10][4],
        data[10][5],
    )

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = (
        data[1][1],
        data[1][2],
        data[1][4],
        data[1][5],
    )
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = (
        data[6][1],
        data[6][2],
        data[6][4],
        data[6][5],
    )
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = (
        data[11][1],
        data[11][2],
        data[10][4],
        data[11][5],
    )

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = (
        data[2][1],
        data[2][2],
        data[2][4],
        data[2][5],
    )
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = (
        data[7][1],
        data[7][2],
        data[7][4],
        data[7][5],
    )
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = (
        data[12][1],
        data[12][2],
        data[12][4],
        data[12][5],
    )

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = (
        data[3][1],
        data[3][2],
        data[3][4],
        data[3][5],
    )
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = (
        data[8][1],
        data[8][2],
        data[8][4],
        data[8][5],
    )
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = (
        data[13][1],
        data[13][2],
        data[13][4],
        data[13][5],
    )

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = (
        data[4][1],
        data[4][2],
        data[4][4],
        data[4][5],
    )
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = (
        data[9][1],
        data[9][2],
        data[9][4],
        data[9][5],
    )
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = (
        data[14][1],
        data[14][2],
        data[14][4],
        data[14][5],
    )

    batting_DB = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (
        bat_2024_DB + bat_2023_DB + bat_2022_DB
    )
    batting_D = (hit_2024_D + hit_2023_D + hit_2022_D) / (
        bat_2024_D + bat_2023_D + bat_2022_D
    )
    batting_T = (hit_2024_T + hit_2023_T + hit_2022_T) / (
        bat_2024_T + bat_2023_T + bat_2022_T
    )
    batting_C = (hit_2024_C + hit_2023_C + hit_2022_C) / (
        bat_2024_C + bat_2023_C + bat_2022_C
    )
    batting_G = (hit_2024_G + hit_2023_G + hit_2022_G) / (
        bat_2024_G + bat_2023_G + bat_2022_G
    )

    RBI_to_hit_ratio_DB = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    Homerun_to_hit_ratio_DB = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (
        hit_2024_DB + hit_2023_DB + hit_2022_DB
    )
    RBI_to_hit_ratio_D = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    Homerun_to_hit_ratio_D = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (
        hit_2024_D + hit_2023_D + hit_2022_D
    )
    RBI_to_hit_ratio_T = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    Homerun_to_hit_ratio_T = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (
        hit_2024_T + hit_2023_T + hit_2022_T
    )
    RBI_to_hit_ratio_C = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    Homerun_to_hit_ratio_C = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (
        hit_2024_C + hit_2023_C + hit_2022_C
    )
    RBI_to_hit_ratio_G = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )
    Homerun_to_hit_ratio_G = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (
        hit_2024_G + hit_2023_G + hit_2022_G
    )

    batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
    RBI_to_hit_ratio = [
        RBI_to_hit_ratio_DB,
        RBI_to_hit_ratio_D,
        RBI_to_hit_ratio_T,
        RBI_to_hit_ratio_C,
        RBI_to_hit_ratio_G,
    ]
    Homerun_to_hit_ratio = [
        Homerun_to_hit_ratio_DB,
        Homerun_to_hit_ratio_D,
        Homerun_to_hit_ratio_T,
        Homerun_to_hit_ratio_C,
        Homerun_to_hit_ratio_G,
    ]

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
        data_win[1][1]
        + data_win[7][1]
        + data_win[13][1]
        + data_win[1][2]
        + data_win[7][2]
        + data_win[13][2]
    )
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
        data_win[2][1]
        + data_win[8][1]
        + data_win[14][1]
        + data_win[2][2]
        + data_win[8][2]
        + data_win[14][2]
    )
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
        data_win[3][1]
        + data_win[9][1]
        + data_win[15][1]
        + data_win[3][2]
        + data_win[9][2]
        + data_win[15][2]
    )
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
        data_win[4][1]
        + data_win[10][1]
        + data_win[16][1]
        + data_win[4][2]
        + data_win[10][2]
        + data_win[16][2]
    )
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
        data_win[5][1]
        + data_win[11][1]
        + data_win[17][1]
        + data_win[5][2]
        + data_win[11][2]
        + data_win[17][2]
    )

    win = [
        win_percentage_3_DB,
        win_percentage_3_D,
        win_percentage_3_T,
        win_percentage_3_C,
        win_percentage_3_G,
    ]

    Predicted_homerun_by_team = []
    Predicted_RBI_by_team = []
    Predicted_hit_by_team = []
    Predicted_4_1_by_team = []
    Predicted_4_2_by_team = []
    Predicted_4_3_by_team = []
    Predicted_4_4_by_team = []
    Total_number_of_games_contribution_by_team = []
    Total_number_of_games_contribution_victory_by_team = []

    for i in range(5):
        prob_4_4 = batting[i] ** 4
        prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
        prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
        prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4
        predicted_total_games_played = 22
        probabilities = [prob_4_1, prob_4_2, prob_4_3, prob_4_4]
        total_predicted_hit = 0
        counter = 1

        for prob in probabilities:
            total_predicted_hit += predicted_total_games_played * prob * counter
            counter += 1

        total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
        total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

        f = RBI_to_hit_ratio[i]

        Total_number_of_games_contribution = 0
        counter = 1
        for prob_2 in probabilities:
            Total_number_of_games_contribution += (
                prob_2 * (1 - (1 - f) ** counter) * predicted_total_games_played
            )
            counter += 1

        Predicted_homerun_by_team.append(int(total_predicted_homerun))
        Predicted_RBI_by_team.append(int(total_predicted_RBI))
        Predicted_hit_by_team.append(int(total_predicted_hit))
        Predicted_4_1_by_team.append(round(prob_4_1, 3))
        Predicted_4_2_by_team.append(round(prob_4_2, 3))
        Predicted_4_3_by_team.append(round(prob_4_3, 3))
        Predicted_4_4_by_team.append(round(prob_4_4, 3))

        Total_number_of_games_contribution_by_team.append(
            int(Total_number_of_games_contribution)
        )

        Total_number_of_games_contribution_victory_by_team.append(
            int(Total_number_of_games_contribution * win[i])
        )

    result_DB = [
        round(batting_DB, 3),
        int(Predicted_homerun_by_team[0]),
        int(Predicted_RBI_by_team[0]),
        int(Predicted_hit_by_team[0]),
        round(win_percentage_3_DB, 3),
        round(
            1
            - (
                Predicted_4_4_by_team[0]
                + Predicted_4_3_by_team[0]
                + Predicted_4_2_by_team[0]
                + Predicted_4_1_by_team[0]
            ),
            3,
        ),
        round(Predicted_4_1_by_team[0], 3),
        round(Predicted_4_2_by_team[0], 3),
        round(Predicted_4_3_by_team[0], 3),
        round(Predicted_4_4_by_team[0], 3),
        int(Total_number_of_games_contribution_by_team[0]),
        int(Total_number_of_games_contribution_victory_by_team[0]),
    ]
    result_D = [
        round(batting_D, 3),
        int(Predicted_homerun_by_team[1]),
        int(Predicted_RBI_by_team[1]),
        int(Predicted_hit_by_team[1]),
        round(win_percentage_3_D, 3),
        round(
            1
            - (
                Predicted_4_4_by_team[1]
                + Predicted_4_3_by_team[1]
                + Predicted_4_2_by_team[1]
                + Predicted_4_1_by_team[1]
            ),
            3,
        ),
        round(Predicted_4_1_by_team[1], 3),
        round(Predicted_4_2_by_team[1], 3),
        round(Predicted_4_3_by_team[1], 3),
        round(Predicted_4_4_by_team[1], 3),
        int(Total_number_of_games_contribution_by_team[1]),
        int(Total_number_of_games_contribution_victory_by_team[1]),
    ]
    result_T = [
        round(batting_T, 3),
        int(Predicted_homerun_by_team[2]),
        int(Predicted_RBI_by_team[2]),
        int(Predicted_hit_by_team[2]),
        round(win_percentage_3_T, 3),
        round(
            1
            - (
                Predicted_4_4_by_team[2]
                + Predicted_4_3_by_team[2]
                + Predicted_4_2_by_team[2]
                + Predicted_4_1_by_team[2]
            ),
            3,
        ),
        round(Predicted_4_1_by_team[2], 3),
        round(Predicted_4_2_by_team[2], 3),
        round(Predicted_4_3_by_team[2], 3),
        round(Predicted_4_4_by_team[2], 3),
        int(Total_number_of_games_contribution_by_team[2]),
        int(Total_number_of_games_contribution_victory_by_team[2]),
    ]
    result_C = [
        round(batting_C, 3),
        int(Predicted_homerun_by_team[3]),
        int(Predicted_RBI_by_team[3]),
        int(Predicted_hit_by_team[3]),
        round(win_percentage_3_C, 3),
        round(
            1
            - (
                Predicted_4_4_by_team[3]
                + Predicted_4_3_by_team[3]
                + Predicted_4_2_by_team[3]
                + Predicted_4_1_by_team[3]
            ),
            3,
        ),
        round(Predicted_4_1_by_team[3], 3),
        round(Predicted_4_2_by_team[3], 3),
        round(Predicted_4_3_by_team[3], 3),
        round(Predicted_4_4_by_team[3], 3),
        int(Total_number_of_games_contribution_by_team[3]),
        int(Total_number_of_games_contribution_victory_by_team[3]),
    ]
    result_G = [
        round(batting_G, 3),
        int(Predicted_homerun_by_team[4]),
        int(Predicted_RBI_by_team[4]),
        int(Predicted_hit_by_team[4]),
        round(win_percentage_3_G, 3),
        round(
            1
            - (
                Predicted_4_4_by_team[4]
                + Predicted_4_3_by_team[4]
                + Predicted_4_2_by_team[4]
                + Predicted_4_1_by_team[4]
            ),
            3,
        ),
        round(Predicted_4_1_by_team[4], 3),
        round(Predicted_4_2_by_team[4], 3),
        round(Predicted_4_3_by_team[4], 3),
        round(Predicted_4_4_by_team[4], 3),
        int(Total_number_of_games_contribution_by_team[4]),
        int(Total_number_of_games_contribution_victory_by_team[4]),
    ]
    return [result_DB, result_D, result_T, result_C, result_G]

    conn_13.commit()
    conn_13.close()
    conn_14.commit()
    conn_14.close()

    # Creating the instruction page
    step = Label(
        instruction_page,
        text="Step by step instruction for the system",
        bg="#E6002D",
        fg="white",
    )


    step.pack()
    step_one = Label(
        instruction_page,
        text="1. Click the start button on the start page.",
        bg="#E6002D",
        fg="white",
    )
    step_one.pack()
    step_two = Label(
        instruction_page,
        text="2. Choose the player that you want the prediction of.",
        bg="#E6002D",
        fg="white",
    )
    step_two.pack()
    step_three = Label(
        instruction_page,
        text="3. Choose the number of years of data the system want to use.",
        bg="#E6002D",
        fg="white",
    )
    step_three.pack()
    step_four = Label(
        instruction_page,
        text="4. Go to the confirmation page and check if the input is correct.",
        bg="#E6002D",
        fg="white",
    )
    step_four.pack()
    step_five = Label(
        instruction_page,
        text="5. Click the input button to display data on the next page.",
        bg="#E6002D",
        fg="white",
    )
    step_five.pack()
    back_btn = Button(instruction_page, text="Back", command=lambda: start_page.tkraise())
    back_btn.pack()

    instruction_page.config(bg="#E6002D")


root.mainloop()
