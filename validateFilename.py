from pathvalidate import is_valid_filename

# list of filenames to check
filenames = [
    "to:do_*.<md>",
    "web?si>te<-*tasks/.md",
    "b:a*<c>kl\"og.md",
    "weekly-tasks.md"
]

# Loop through the list of filenames and see which ones are valid
for filename in filenames:
    if is_valid_filename(filename):
        print(f"Yes, '{filename}' is a valid filename!")
    else:
        print(f"'{filename}' is an invalid filename.")