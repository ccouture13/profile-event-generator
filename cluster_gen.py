import random
import hashlib
import csv
import uuid

import argparse

################################################

parser = argparse.ArgumentParser(description='A cluster/record generator.')
parser.add_argument("-c", "--number_ids", help="Sets the number of IDs default is 500", type=int)
parser.add_argument("-p", "--number_partners", help="How many partner match files to creat, default is 0", type=int)
parser.add_argument("-m", "--match_percentage", help="Set maximum match percentage, default is 20", type=int)
parser.add_argument("-cid_ppid", "--custom_id", help="Set which custom ID to use as PPID between 0 & 9, default is c0", type=int)


args = parser.parse_args()

if args.number_ids is None:
  numID = range(500)
else:
  numID = range(args.number_ids)

if args.match_percentage is None:
  matchPerc = 0.2
else:
  matchPerc = args.match_percentage

if args.number_partners is None:
  numberPartners = 0 
else:
  numberPartners = range(args.number_partners+1)

if args.custom_id is None:  
  PPID = ""
else:
  PPID = args.custom_id

##################################################

identity_clusterss = []

colours = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
car_manufacturers = ["Ford", "Toyota", "Honda", "GM", "Tesla", "VW", "Mercedes", "BMW", "Audi", "Fiat"]
genders = ["male", "female"]

for i in numID:
  email_bytes = random.getrandbits(128).to_bytes(16, byteorder="big")
  hashed_email = hashlib.sha3_256(email_bytes).hexdigest()
  
  id_c = ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))

  idfa = str(uuid.uuid4()).upper().replace('-', '')
  gaid = str(uuid.uuid4()).upper()
  
  colour = random.choice(colours)
  car = random.choice(car_manufacturers)
  age = str(random.randint(18, 45))
  gender = random.choice(genders)
  
  identity_clusters = {
      "id_e": hashed_email, 
      "id_c"+str(PPID): id_c, 
      "id_a": idfa,
      "id_g": gaid,
      "trait_colour": colour,
      "trait_car": car,
      "trait_age": age,
      "trait_gender": gender
  }

  identity_clusterss.append(identity_clusters)

with open('clusters.csv', 'w') as csvfile:
    fieldnames = identity_clusterss[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for cluster in identity_clusterss:
        writer.writerow(cluster)
    csvfile.close

if numberPartners != 0:
  for i in numberPartners:
    with open('clusters.csv', 'r') as input_file:
      input_file.seek(0)
      csv_reader = csv.reader(input_file)

      num_rows = sum(1 for row in csv_reader)

      randMatchPerc = random.randint(6, matchPerc)/100
      num_rows_to_take = int(num_rows * randMatchPerc)

      random_rows = random.sample(range(num_rows), num_rows_to_take)

      input_file.seek(0)
      csv_reader = csv.reader(input_file)

      with open(str(int(randMatchPerc*100)) + "% match rate." +".csv", 'w') as output_file:
        fieldnames = identity_clusterss[0].keys()
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(fieldnames)
        for i, row in enumerate(csv_reader):
          if i in random_rows:
            csv_writer.writerow(row)
      output_file.close