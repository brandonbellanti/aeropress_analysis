# import libraries
import datetime, subprocess

# get current date and time
today = datetime.datetime.today()

# create recprd template
brew_record_template = f"""date: {today.strftime(r'%Y-%m-%d')}
time: {today.strftime(r'%H:%M %p')}
drink_type: 
method: 
filter: 
coffee_type: 
roast: 
grind_size: 
coffee_weight: 
brew_water_weight: 
brew_water_temp: 
pour_duration: 
stir_start_time: 
stir_duration: 
push_start_time: 
push_duration: 
overall_duration: 
added_water_weight: 
added_water_temp: 
extraction: 
body: 
rating: 
notes: """

# create new filepath in the project directory
project_dir = '/Users/BrandonBel/Documents/Coding/projects/aeropress_analysis'
brew_record_filepath = project_dir + f"""/brew_records/ap-br-{today.strftime(r'%Y%m%d-%H%M')}.yml"""

# create new file and write template for brew record
with open(brew_record_filepath,'w') as brew_file:
	brew_file.write(brew_record_template)

# open brew record file for editing
subprocess.run(f"""open {brew_record_filepath}""", shell=True)
