import string

# ── Read file
file_name = "blackcoffee.txt"

with open(file_name, "r") as file:
    raw_contents = file.read()

lowercased_text = raw_contents.lower()

# remove every punctuation character from the text
unicode_punctuation = "—–''""…"
all_punctuation = string.punctuation + unicode_punctuation

cleaned_text = lowercased_text
for punctuation_char in all_punctuation:
    cleaned_text = cleaned_text.replace(punctuation_char, "")

# split the cleaned text into a list of individual words
word_list = cleaned_text.split()

# count words
# use a dictionary
word_counts = {}
for word in word_list:
    word_counts[word] = word_counts.get(word, 0) + 1

# results
total_word_count = len(word_list)
unique_word_count = len(word_counts)

# sort the dictionary by count
sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
top_ten_words = sorted_word_counts[:10]

# build output to save it to results.txt
output_lines = []
output_lines.append("Word Frequency Counter")
output_lines.append(f"File: {file_name}")
output_lines.append("-" * 40)
output_lines.append(f"{'Total words':<15}: {total_word_count}")
output_lines.append(f"{'Unique words':<15}: {unique_word_count}")
output_lines.append("-" * 40)
output_lines.append("Top 10 Most Common Words")
output_lines.append("-" * 40)

for word, count in top_ten_words:
    output_lines.append(f"{word:<15}: {count}")

report = "\n".join(output_lines)
print(report)

# Save the same report to results.txt
with open("results.txt", "w") as results_file:
    results_file.write(report + "\n")
