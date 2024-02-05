# Manual Sort

This program helps you sort a list of items. It reads a list of items from a
text file and asks the user to compare each pair of items to determine the
order. The sorted list is then printed to the console.

## Usage

```bash
python manual_sort.py <input_file>.txt
```

## Using this to sort JIRA tickets

0. Export the list of JIRA tickets to a csv file.
    - Go to filters -> "View all issues"
    - Edit the query to filter the tickets you want to sort.
    - Click "Export Issues" -> "Export CSV (All fields)".
    - Save the file as `jira_tickets.csv`.
0. Move the "key" column and "title" column to a text file
    - Open the csv file in a spreadsheet program.
    - Copy the "key" and "title" columns to a new text file and save it as `jira_tickets.txt`.
0. Run the program
    - `python manual_sort.py jira_tickets.txt`
