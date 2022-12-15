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

parser.add_argument("-id_types", default= "email", choices= ["email", "idfa", "gaid"], help="Select the ID types to generate, can be email, cid, idfa, gaid, default is email only.", type=str, nargs='*')
parser.add_argument("-file_type", default="csv", choices= ["csv", "json"], help="Sets the output type, either csv or json, default is CSV.", type=str)
parser.add_argument("-count", default= 50, help="Sets the number of IDs default is 50", type=int)
parser.add_argument("-partners", default= 0, help="How many partner match files to create, default is 0", type=int)
parser.add_argument("-add_cid", default=5, choices=[1,2,3,4,5,6,7,8,9], help="Add CID and choose which CID, default = 5", type=int)
parser.add_argument("-add_traits", help="Add traits or not to the output file. Default is true", action=argparse.BooleanOptionalAction)

args = parser.parse_args()

# Set variables
id_clusters = []

add_traits = args.add_traits
id_types = args.id_types
outputType = args.file_type
numID = range(args.count)
numberPartners = range(args.partners)
customID = args.add_cid

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
      
      identity_clusters = {}
      for i in id_types: 
        if "email" in id_types: {
          identity_clusters.update({"id_e": hashed_email,})
        }
        if "idfa" in id_types: {
          identity_clusters.update({"id_a": idfa,})
        }
        if "gaid" in id_types: {
          identity_clusters.update({"id_g": gaid,})
        }
        if args.add_cid: {
          identity_clusters.update({"id_c"+str(customID): id_c,})
        }
        if add_traits == True:
          identity_clusters.update({
            "trait_colour": colour,
            "trait_car": car,
            "trait_age": age,
            "trait_gender": gender
          })
      
      id_clusters.append(identity_clusters)

    if outputType == "json":
      email_bytes = random.getrandbits(128).to_bytes(16, byteorder="big")
      email = "e:"+hashlib.sha3_256(email_bytes).hexdigest()

      id_c = "c"+str(customID)+":"+''.join(random.choices('0123456789abcdef', k=32))
      idfa = "a:"+ str(uuid.uuid4()).upper().replace('-', '')
      gaid = "g:"+str(uuid.uuid4()).upper()
      colour = random.choice(colours)
      car = random.choice(car_manufacturers)
      age = str(random.randint(18, 45))
      gender = random.choice(genders)

      j_identity_clusters = {
        "id": "",
        "neighbours": [],
        "traits": [],
      }

      for j in id_types[0]: 
        j_identity_clusters.update({
          "id" : locals()[id_types[0]],
      })
      for k in id_types[1:]: 
        j_identity_clusters["neighbours"].append(
          {
            "id" : locals()[k],
          },
      )
      if args.add_cid: {
        j_identity_clusters["neighbours"].append(
          {
            "id" : id_c,
          },
        )
      } 
      if add_traits == True:
        j_identity_clusters["traits"].append(
          {
            "key": "colour",
            "value": colour,
          },)
        j_identity_clusters["traits"].append(
          {
            "key": "car",
            "value": car,
          },)
        j_identity_clusters["traits"].append(
          {
            "key": "age",
            "value": age,
          },)
        j_identity_clusters["traits"].append(
          {
            "key": "gender",
            "value": gender,
          })
      id_clusters.append(j_identity_clusters)

# If filetype is CSV, output a CSV & the random matches.
if outputType == "csv":
  createCluster(args.file_type)
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

        randMatchPerc = random.randint(23, 43)/100
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
  createCluster(args.file_type)
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

        randMatchPerc = random.randint(23, 43)/100
        num_rows_to_take = int(num_rows * randMatchPerc)

        random_rows = random.sample(range(num_rows), num_rows_to_take)

        with open(str(int(randMatchPerc*100)) + "% match rate" +".json", 'w') as output_file2:
          for i, row in enumerate(linestowrite):
            if i in random_rows:
              output_file2.write(json.dumps(row))
              output_file2.write('\n')
        output_file2.close
pass