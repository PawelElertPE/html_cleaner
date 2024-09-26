# text = "To_elqTrackID12345 and some more text."

# index = text.find('elqTrackID')
# print(index)


# def remove_after_elqTrackID(text):
#     cut_off_index = text.find('elqTrackID') + len('elqTrackID')
#     return text[:cut_off_index]

# # Example usage
# text = "This is a sample text with elqTrackID12345 and some more text."
# cleaned_text = remove_after_elqTrackID(text)
# print(cleaned_text)


# def remove_string(text, start_str, end_str):
#     while start_str in text and end_str in text:
#         start_index = text.find(start_str)
#         end_index = text.find(end_str, start_index) + len(end_str)
#         text = text[:start_index] + text[end_index:]
#     return text

# # Example usage
# text = "This is a sample text with elqTrackID12345elqTrack and another elqTrack=true to be removed."
# start_str = "elqTrackID"
# end_str = "elqTrack=true"

# cleaned_text = remove_string(text, start_str, end_str)
# print(cleaned_text)

start_str = "elqTrackID"
end_str = "elqTrack=true"
text = "This is a sample text with elqTrackID12345elqTrack and another elqTrack=true to be removed."

start_index = text.find(start_str)
end_index = text.find(end_str) + len(end_str)

text_before = text[:start_index]
text_after_end = text[end_index:]
print(f"The text before is: {text_before}")
print(f"The text after is: {text_after_end}")

clean_html = text_before + "%%REPLACE WITH UTM%%" + text_after_end
print(clean_html)
