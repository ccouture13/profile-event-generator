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

3. Generated CSV files will be saved in the `Outputs` directory, under `Profile Files` and `Event Files`.

Files are saved with the `COUNT` in K and the`TIMESTAMP` at which they were generated, this is so you can keep previous files for testing matches & deduplication from source to source.