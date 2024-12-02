import ezodf
import polars as pl

def extract_named_ranges_from_ods(file_path):
    # Open the ODS file
    doc = ezodf.opendoc(file_path)

    # Retrieve the named ranges from the document
    named_ranges = doc.named_ranges

    # Create a dictionary to store DataFrames
    named_range_dataframes = {}

    for named_range_name, named_range in named_ranges.items():
        # Get the sheet and the range details
        sheet = named_range.table
        start_cell = named_range.start
        end_cell = named_range.end

        # Access the sheet
        sheet_data = doc.sheets[sheet]

        # Extract cells within the specified range
        data = []

        for row_idx in range(start_cell[0], end_cell[0] + 1):
            row_data = []
            for col_idx in range(start_cell[1], end_cell[1] + 1):
                cell = sheet_data[row_idx, col_idx]
                row_data.append(cell.value)
            data.append(row_data)

        # Convert the data to a Polars DataFrame
        df = pl.DataFrame(data[1:], columns=data[0])

        # Store the DataFrame in the dictionary with the named range name
        named_range_dataframes[named_range_name] = df

    return named_range_dataframes

# Example usage
if __name__ == "__main__":
    file_path = 'your_file.ods'
    named_ranges_dfs = extract_named_ranges_from_ods(file_path)

    for name, df in named_ranges_dfs.items():
        print(f"Named Range: {name}")
        print(df)
