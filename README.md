## A simple (and possibly broken) cluster generator.

Just made this so I can generate CSV and JSON files quickly to use in testing/matches. There are multiple arguments you can pass to generate different file tyles and make partner match files with varying percentages.

## Arguments
### Output File Type (JSON or CSV)
Relatively self explanatory, choose which file type you want to generate.
``` 
  -t OUTPUT_TYPE, --output_type OUTPUT_TYPE
                        Sets the output type, either csv or json
```
### Number of IDs to generate for the master output file.
For CSV it will generate rows with a header, for JSON it will generate individual lines.
```
  -c NUMBER_IDS, --number_ids NUMBER_IDS
                        Sets the number of IDs default is 50
```
### Create match output files.
Creates match file(s) (the amount depending on the parameter) based on the original file for use in matches.
```
  -p NUMBER_PARTNERS, --number_partners NUMBER_PARTNERS
                        How many partner match files to create, default is 0
```
### Set the maximum match percentage. 
Lowest can be 10 and the generator will choose a random percent between 10 and your maximum. Default is 20%
```
  -m MATCH_PERCENTAGE, --match_percentage MATCH_PERCENTAGE
                        Set maximum match percentage, default is 20
```
### CID selector.
Select which CID to generate random 8 character PPIDs for, default is c1.
```
  -cid CUSTOM_ID, --custom_id CUSTOM_ID
                        Set which custom ID to use as custumID between 0 & 9, default is c1
```
