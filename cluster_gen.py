import random
import hashlib
import csv
import uuid
import json
import argparse
import sys
import os

# CLI arguments
parser = argparse.ArgumentParser(description='A cluster/record generator.')

parser.add_argument("-t", "--output_type", help="Sets the output type, either csv or json", type=str)
parser.add_argument("-c", "--number_ids", help="Sets the number of IDs default is 50", type=int)
parser.add_argument("-p", "--number_partners", help="How many partner match files to create, default is 0", type=int)
parser.add_argument("-m", "--match_percentage", help="Set maximum match percentage, default is 20", type=int)
parser.add_argument("-cid", "--custom_id", help="Set which custom ID to use as custumID between 0 & 9, default is c1", type=int)


args = parser.parse_args()

# Set variables/handle empty.
id_clusters = []

filetypes = ["csv","json"]
if args.output_type in filetypes:
  outputType = args.output_type
else:
  outputType = "csv"

if args.number_ids is None:
  numID = range(50)
else:
  numID = range(args.number_ids)

if args.match_percentage is None:
  matchPerc = 0.2
else:
  matchPerc = args.match_percentage

if args.number_partners is None:
  numberPartners = 0 
else:
  numberPartners = range(args.number_partners)

if args.custom_id is None:  
  custumID = "1"
else:
  custumID = args.custom_id

# Make the identity clusters/records.
def createCluster(filetyp):
  colours = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
  car_manufacturers = ["Ford", "Toyota", "Honda", "GM", "Tesla", "VW", "Mercedes", "BMW", "Audi", "Fiat"]
  genders = ["male", "female"]



  for i in numID:
    if outputType == "csv":
      email_bytes = random.getrandbits(128).to_bytes(16, byteorder="big")
      hashed_email = hashlib.sha3_256(email_bytes).hexdigest()

      id_c = ''.join(random.choices('0123456789abcdef', k=32))


      idfa = str(uuid.uuid4()).upper().replace('-', '')
      gaid = str(uuid.uuid4()).upper()
      colour = random.choice(colours)
      car = random.choice(car_manufacturers)
      age = str(random.randint(18, 45))
      gender = random.choice(genders)
      
      identity_clusters = {
        # "id_e": hashed_email, 
        "id_c"+str(custumID): id_c, 
        # "id_a": idfa,
        # "id_g": gaid,
        # "trait_colour": colour,
        # "trait_car": car,
        # "trait_age": age,
        # "trait_gender": gender
      }
      id_clusters.append(identity_clusters)

    if outputType == "json":
      email_bytes = random.getrandbits(128).to_bytes(16, byteorder="big")
      hashed_email = hashlib.sha3_256(email_bytes).hexdigest()

      id_c = ''.join(random.choices('0123456789abcdef', k=32))

      idfa = str(uuid.uuid4()).upper().replace('-', '')
      gaid = str(uuid.uuid4()).upper()
      colour = random.choice(colours)
      car = random.choice(car_manufacturers)
      age = str(random.randint(18, 45))
      gender = random.choice(genders)
      
      j_identity_clusters = {
        "id": "e:"+hashed_email,
        "neighbors": [
          {"id": "c:"+str(custumID)+id_c}, 
          {"id": "a:"+idfa},
          {"id": "g:"+idfa},
        ],
        "traits":[
          {
            "key": "colour",
            "value": colour,
          },
          {
            "key": "car",
            "value": car,
          },
          {
            "key": "age",
            "value": age,
          },
          {
            "key": "gender",
            "value": gender,
          }
        ]
      }
      id_clusters.append(j_identity_clusters)

# If filetype is CSV, output a CSV & the random matches.
if outputType == "csv":
  createCluster(args.output_type)
  with open("clusters.csv", 'w') as csvfile:
      fieldnames = id_clusters[0].keys()
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()

      for cluster in id_clusters:
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

        with open(str(int(randMatchPerc*100)) + "% match rate" +".csv", 'w') as output_file:
          fieldnames = id_clusters[0].keys()
          csv_writer = csv.writer(output_file)
          csv_writer.writerow(fieldnames)
          for i, row in enumerate(csv_reader):
            if i in random_rows:
              csv_writer.writerow(row)
        output_file.close
pass


# If filetype is JSON, output a JSON & the random matches.
if outputType == "json":
  createCluster(args.output_type)
  with open("clusters.json", "w") as jsonfile:
    for item in id_clusters:
        jsonfile.write(json.dumps(item))
        jsonfile.write('\n')

  if numberPartners != 0:
    linestowrite = []
    for i in numberPartners:
      with open("clusters.json", "r") as jsonInput:
        for lines in jsonInput:
          linestowrite.append(json.loads(lines))
          
        num_rows = len(linestowrite)

        randMatchPerc = random.randint(10, matchPerc)/100
        num_rows_to_take = int(num_rows * randMatchPerc)

        random_rows = random.sample(range(num_rows), num_rows_to_take)

        with open(str(int(randMatchPerc*100)) + "% match rate" +".json", 'w') as output_file2:
          for i, row in enumerate(linestowrite):
            if i in random_rows:
              output_file2.write(json.dumps(row))
              output_file2.write('\n')
        output_file2.close
pass