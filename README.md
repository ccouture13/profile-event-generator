# A Simple Record Generator

This record generator creates CSV files of two types: `PROFILE` and `EVENT`, intended for testing purposes.

## How to Use

1. Adjust the settings in `config.json` according to your needs. This configuration controls the volume and characteristics of the generated data.

    ```json
    {
      "COUNT": 5000,
      "MAX_INVALID_PERCENTAGE": 0.05,
      "MAX_EMPTY_PERCENTAGE": 0.2
    }
    ```

2. **Generate Records**:
    - For **Profile** records, open a terminal, navigate to the project directory, and run:
        ```bash
        python3 profile_gen.py
        ```
    - For **Event** records, execute:
        ```bash
        python3 event_gen.py
        ```
    -Generated CSV files will be saved in the `Outputs` directory, under `Profile Files` and `Event Files`.

3. **Generate Event Schema**:
    - To generate an eventschema CLI command, open the event_schema.py and ad the relative path to your events file.
        ```python
        # Replace with your filepath
        file_path = 'Examples/5K_events_2024-02-02_1211.csv'
        ```
    - Then open a terminal, navigate to the project directory, and run:
        ```bash
        python3 schema_gen.py
        ```
    - This will then output a .txt file containing all CLI commands to create event schemas for each event_type.

Files are saved with the `COUNT` in K and the`TIMESTAMP` at which they were generated, this is so you can keep previous files for testing matches & deduplication from source to source.
