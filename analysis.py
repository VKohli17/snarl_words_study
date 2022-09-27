import matplotlib.pyplot as plt
import csv
import os

def generate_graph(year_list, percentage_list):
    plt.plot(year_list, percentage_list, marker='o')
    plt.xlabel("Years")
    plt.ylabel("Percentage of snarl usage")
    plt.title("Evolution of the snarl usage of \"bhakt\"")
    plt.xticks(year_list)
    plt.savefig("output.png")


def process_file(file_name, data_dir):

    file = open(os.path.join(data_dir, file_name), "r")
    csv_reader_obj = csv.reader(file, delimiter=",")
    total_counter = 0
    snarl_counter = 0
    for row in csv_reader_obj:
        if len(row[-1]) == 1:
            total_counter += 1
        if row[-1] == 'S':
            snarl_counter += 1
    
    return (total_counter, snarl_counter, (snarl_counter/total_counter))

def process_all_files(data_dir, years):

    snarl_percentage = []
    for year in years:
        file_name = "data_{}.csv".format(year)
        total_counter, snarl_counter, fraction = process_file(file_name, data_dir)
        print("Year: {}, total: {}, snarl: {}, snarl proportion: {}".format(year, total_counter, snarl_counter, fraction))
        snarl_percentage.append(fraction*100)
    
    return snarl_percentage

## Driver begins here 

YEARS_AS_OF_NOW = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
DATA_DIR = "./annotated"

percentage_list = process_all_files(DATA_DIR, YEARS_AS_OF_NOW)

generate_graph(YEARS_AS_OF_NOW, percentage_list)

        

# process_file("data_2011.csv", "./annotated")




# x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# y = [0, 10, 300, 350, 400, 350, 380, 290, 400]

# plt.plot(x, y)
# plt.show()

