#! python3
# mclip.py - A multi-clipboard program

text = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Woulds you consider making this a monthly donation?"""
}

import pyperclip
import sys
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}")