import csv

# get data from given tablename
def get_data(tablename):
  filename = 'data/yop-' + tablename + '.csv'
  with open(filename) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      columns = {}
      user_list = []
      for row in csv_reader:
          if line_count == 0:
            for column in row:
              columns[column] = ""
              line_count += 1
          else:
            user_data = {}
            index = 0
            for column in columns:
              user_data[column] = row[index]
              index += 1
            user_list.append(user_data)
  return user_list

def update_data(tablename,data_list):
  filename = 'data/yop-' + tablename + '.csv'
  headings = []
  with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      headings = row
      #data_list.append(headings)
      break
  with open(filename,'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(headings)
    for data in data_list:
      new_data = []
      for heading in headings:     
        new_data.append(data[heading])
      print(new_data)
      csv_writer.writerow(new_data)
  return data_list


    