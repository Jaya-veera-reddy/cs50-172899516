import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression pattern to match YouTube embed URLs
    pattern = r'<iframe [^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"[^>]*>'

    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)  # Extract the video ID
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
