import csv
import json
from datetime import datetime

def generate_cli_commands_from_csv(file_path):
    event_types = {}

    # Read the CSV data from the file
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if event_type := row['event_type'].strip():
                if event_type not in event_types:
                    event_types[event_type] = set()

                for header in reader.fieldnames:
                    if header.startswith('prop_'):
                        event_types[event_type].add(header[5:])

    # Generate CLI commands for each event type
    commands = []
    for event_type, properties in event_types.items():
        schema = [{"name": prop, "type": {"kind": "string"}} for prop in properties]
        schema_json = json.dumps(schema)
        cli_command = f'bin/optable-cli --timeout=10s event-schema create {event_type} "{event_type}" "{event_type}" \'{schema_json}\''
        commands.append(cli_command)

    # Write the commands to a file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f'eventschema{timestamp}.txt'
    with open(output_file, 'w') as f:
        for command in commands:
            f.write(command + "\n")

    print(f"CLI commands written to {output_file}")

if __name__ == "__main__":
    file_path = '<insert_path>'
    generate_cli_commands_from_csv(file_path)
