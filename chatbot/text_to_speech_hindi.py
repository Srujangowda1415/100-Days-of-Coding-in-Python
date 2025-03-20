from gtts import gTTS
import os

# Hindi text stored in a Python list
hindi_text_list = [
    "सूरज क्षितिज के नीचे चला गया, आकाश सुनहरे रंग में नहाया हुआ था।",
    "हवा हल्की थी और पक्षी अपने घोंसलों में लौट रहे थे।",
    "चारों ओर एक अद्भुत शांति थी, जैसे प्रकृति विश्राम कर रही हो।"
]
hindi_poem = """
हो गया पूर्ण अज्ञात वास,
पाडंव लौटे वन से सहास,
पावक में कनक-सदृश तप कर,
वीरत्व लिए कुछ और प्रखर,
नस-नस में तेज-प्रवाह लिये,
कुछ और नया उत्साह लिये।

सच है, विपत्ति जब आती है,
कायर को ही दहलाती है,
शूरमा नहीं विचलित होते,
क्षण एक नहीं धीरज खोते,
विघ्नों को गले लगाते हैं,
काँटों में राह बनाते हैं।
"""

# Join list elements into a single text string
text = " ".join(hindi_text_list)  # Use "\n" for natural pauses

# Generate speech
# tts = gTTS(text, lang="hi")
tts = gTTS(hindi_poem, lang="hi")


# Save the audio file
output_file = "hindi_output.mp3"
tts.save(output_file)

# Play the audio (platform-dependent)
if os.name == "nt":  # Windows
    os.system(f"start {output_file}")
elif os.name == "posix":  # macOS/Linux
    os.system(f"afplay {output_file}")  # macOS
    # os.system(f"mpg321 {output_file}")  # Linux alternative

print(f"Audio saved as {output_file}")
