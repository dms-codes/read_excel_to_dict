# Excel to Dictionary Converter

This Python script allows you to convert data from an Excel file into a Python dictionary. You can use this script to load data from an Excel spreadsheet and create a dictionary where one column serves as keys, and another column serves as values.

## Prerequisites

Before running the script, ensure you have the `pandas` library installed. You can install it using `pip`:

```bash
pip install pandas
```

## Usage

1. Import the necessary library:

   ```python
   import pandas as pd
   ```

2. Load the Excel file using `pd.read_excel`. Replace `'test.xlsx'` with the path to your Excel file:

   ```python
   df = pd.read_excel('test.xlsx', header=None)
   ```

   - The `header=None` argument is used to indicate that there are no column headers in the Excel file.

3. Convert the data from the Excel file into a Python dictionary using `dict(zip())`:

   ```python
   res = dict(zip(df[0], df[1]))
   ```

   - In this example, the first column (`df[0]`) is used as keys, and the second column (`df[1]`) is used as values in the dictionary.

4. Print or use the resulting dictionary (`res`) as needed:

   ```python
   print(res)
   ```

## Example

In this example, the script loads data from the "test.xlsx" Excel file, where the first column contains keys and the second column contains values. It converts this data into a dictionary and prints the result.

## License

This script is provided under the [MIT License](LICENSE).
```

You can customize the script and README.md file to suit your specific Excel file and use case.
