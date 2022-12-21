## A simple record generator.

Just made this so I can generate CSV and JSON files quickly to use in testing/matches. There are multiple arguments you can pass to generate different file tyles and make partner match files with varying percentages.

#### Example:
```
python3 cluster_gen.py -file_type csv -id_types email c2 -ppid_count 64 -count 50000 -partners 2
```
This will create 
- 1 parent file with 50k records, all containing EMAILS & C2s where C2 is 64 characters (a hashed emails length)
- 2 files with varying %s to be used in different match operation tests. Both with a different percentage match rate vs the parent file.   
 
   
## Arguments
### -file_type (required)
Relatively self explanatory, choose which file type you want to generate.
``` 
  -file_type {csv,json}
                        Sets the output type, either csv or json.
```
### -id_types (required)
Select the ID types to generate, can be email, cid, idfa, gaid, default is email only.
``` 
  -id_types [{email,idfa,gaid,c0,c1,c2,c3,c4,c5,c6,c7,c8,c9} ...]
                        Select the ID types to generate, can be email, cid, idfa, gaid.
```
### -count (required)
How many records you want to generate.
```
  -count COUNT          Sets the number of IDs.
```
### -partners
Creates match file(s) (the amount depending on the parameter) based on the original file for use in matches.
```
  -partners PARTNERS    How many partner match files to create, default is 0
```
### -ppid_count 
Set the character count for CIDs generated, default is 32. 
This enables you to generate PPIDs for testing GAM360 and others.
```
  -ppid_count PPID_COUNT
                        Choose the PPID 'character length
```
### -add_traits
Use this commmand to generate random age, gender and colour for each record, default is off.
```
  -add_traits           Add traits or not to the output file. Default is true
```
### -gzip
Optional argument to gzip the file.
```
  -gzip         Gzip this file to test file upload.
```