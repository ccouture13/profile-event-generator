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

cidt = ["c0", "c1","c2","c3","c4","c5","c6","c7","c8","c9"]
idt = ["email", "idfa", "gaid"] + cidt

parser.add_argument("-id_types", required=True, choices= idt, help="Select the ID types to generate, can be email, cid, idfa, gaid.", type=str, nargs='*')
parser.add_argument("-file_type", required=True, choices= ["csv", "json"], help="Sets the output type, either csv or json.", type=str)
parser.add_argument("-count", required=True, help="Sets the number of IDs.", type=int)
parser.add_argument("-partners", default= 0, help="How many partner match files to create, default is 0", type=int)
parser.add_argument("-ppid_count", default= 36, help="Choose the PPID 'character length", type=int)
parser.add_argument("-add_traits", help="Add traits or not to the output file. ", action=argparse.BooleanOptionalAction)

args = parser.parse_args()

# Set variables
id_clusters = []

add_traits = args.add_traits
id_types = args.id_types
outputType = args.file_type
numID = range(args.count)
numberPartners = range(args.partners)
ppid_count = 32 if args.ppid_count is None else args.ppid_count

colours = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
car_manufacturers = ["Ford", "Toyota", "Honda", "GM", "Tesla", "VW", "Mercedes", "BMW", "Audi", "Fiat"]
genders = ["male", "female"]

# Make the identity clusters/records.
def createCSVCluster():
  for i in numID:
    email_bytes = random.getrandbits(128).to_bytes(16, byteorder="big")
    csv_email = {"id_e": hashlib.sha3_256(email_bytes).hexdigest(),}
    csv_idfa = {"id_a": str(uuid.uuid4()).upper().replace('-', ''),}
    csv_gaid = {"id_g": str(uuid.uuid4()).upper(),}
    csv_id_c = ''.join(random.choices('0123456789abcdef', k=ppid_count))

    identity_clusters = {}
    for i in id_types:
      if i not in cidt:
        identity_clusters |= locals()[f"csv_{i}"]
      if i in cidt:
        identity_clusters[f"id_{i}"] = csv_id_c

    if add_traits == True:
      identity_clusters.update({
        "trait_colour": random.choice(colours),
        "trait_car": random.choice(car_manufacturers),
        "trait_age": str(random.randint(18, 45)),
        "trait_gender": random.choice(genders)
      })

    id_clusters.append(identity_clusters)

def createJSONCluster():
  for i in numID:
    email_bytes = random.getrandbits(128).to_bytes(16, byteorder="big")
    email = "e:"+hashlib.sha3_256(email_bytes).hexdigest()

    id_c = ''.join(random.choices('0123456789abcdef', k=ppid_count))
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

    if id_types[0] not in cidt: {
      j_identity_clusters.update({
        "id" : locals()[id_types[0]],
      },)
    }
    else: {
      j_identity_clusters.update({
        "id" : id_types[0]+":"+id_c,
      },)
    }
    for k in id_types[1:]: 
      if k not in cidt:
        j_identity_clusters["neighbours"].append(
          {
            "id" : locals()[k],
          },
        )
      if k in cidt:
          j_identity_clusters["neighbours"].append(
          {
            "id" : k+":"+ id_c,
          },
        )
    traits = [{"key": "colour", "value": colour}, {"key": "car", "value": car}, {"key": "age", "value": age}, {"key": "gender", "value": gender}]
    if add_traits:
        j_identity_clusters["traits"].append(traits)

    id_clusters.append(j_identity_clusters)

# If filetype is CSV, output a CSV & the random matches.
if outputType == "csv":
  createCSVCluster()
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

        num_rows = sum(1 for _ in csv_reader)

        randMatchPerc = random.randint(23, 43)/100
        num_rows_to_take = int(num_rows * randMatchPerc)

        random_rows = random.sample(range(num_rows), num_rows_to_take)

        input_file.seek(0)
        csv_reader = csv.reader(input_file)

        with open(f"{int(randMatchPerc * 100)}% match rate.csv", 'w') as output_file:
          fieldnames = id_clusters[0].keys()
          csv_writer = csv.writer(output_file)
          csv_writer.writerow(fieldnames)
          for i, row in enumerate(csv_reader):
            if i in random_rows:
              csv_writer.writerow(row)
        output_file.close


# If filetype is JSON, output a JSON & the random matches.
if outputType == "json":
  createJSONCluster()
  with open("clusters.json", "w") as jsonfile:
    for item in id_clusters:
        jsonfile.write(json.dumps(item))
        jsonfile.write('\n')

  if numberPartners != 0:
    linestowrite = []
    for i in numberPartners:
      with open("clusters.json", "r") as jsonInput:
        linestowrite.extend(json.loads(lines) for lines in jsonInput)
        num_rows = len(linestowrite)

        randMatchPerc = random.randint(23, 43)/100
        num_rows_to_take = int(num_rows * randMatchPerc)

        random_rows = random.sample(range(num_rows), num_rows_to_take)

        with open(f"{int(randMatchPerc * 100)}% match rate.json", 'w') as output_file2:
          for i, row in enumerate(linestowrite):
            if i in random_rows:
              output_file2.write(json.dumps(row))
              output_file2.write('\n')
        output_file2.close