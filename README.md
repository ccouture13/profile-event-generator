## A simple(ish) record generator.

Just made this so I can generate CSV and JSON files quickly to use in testing/matches. There are multiple arguments you can pass to generate different file tyles and make partner match files with varying percentages.

#### Example:
```
python3 cluster_gen.py -file_type json -count 50000 -partners 2
```
This will create 
- 1 parent file with 50k records.
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
  -id_types [{email,idfa,gaid} ...]
                        Select the ID types to generate, can be email, cid, idfa, gaid.
```
### -count
For CSV it will generate rows with a header, for JSON it will generate individual lines.
```
  -count COUNT          Sets the number of IDs.
```
### -partners
Creates match file(s) (the amount depending on the parameter) based on the original file for use in matches.
```
  -partners PARTNERS    How many partner match files to create, default is 0
```
### -add_cid 
Creates an ID type which is a custom ID, default is C5.
```
  -add_cid {1,2,3,4,5,6,7,8,9}
                        Add CID and choose which CID, default = 5
```
## -add_traits
Use this commmand to generate random age, gender and colour for each record, default is off.
```
  -add_traits           Add traits or not to the output file. Default is true
```
