import math
from PIL import Image

def readTxt():
    # Open source file to extract text
    with open('book.txt', 'r') as inp:
        data = inp.read()
    str = ""
    for i in data:
        str += i
    return str
# a) (a) Download the text of a book of your choice. For example, I downloaded The Count of Monte Cristo, by Alexandre
# Dumas. Load your file, and compute the number of times that each character xi appears.

def letterCount():
    str = readTxt()
    list1 = list(str)
    charCountDict = {}  # Dictionary containing the count of each character
    for item in list1:
        # if item.isalpha():
        if item in charCountDict:
            charCountDict[item] += 1
        else:
            charCountDict[item] = 1
    totalChars = sum(charCountDict.values())
    return charCountDict, totalChars

# (b) Estimate the probability p(xi) of each character.
# (f) Estimate the probability p(xi) of each pixel intensity.
def probability(countDict, total):
    newDict = {}
    for key in countDict:
        prob = countDict[key] / total
        newDict[key] = prob
    return newDict

# (c) Compute the entropy of a character as:
# (g) Compute the entropy of a pixel as in (4.1):
def entropy(dictionary, total):
    sum = 0.0
    probDict = probability(dictionary, total)
    for key in probDict:
        sum += probDict[key] * math.log(1 / probDict[key], 2)
    return sum


# (e) Download an image of your choice. For example, I downloaded the image in Figure 4.1 below. Load your image, and
# compute the number of times that each pixel intensity xi appears.
def pixel_intensity():
    img = Image.open('image.png').convert('LA')
    img.save('greyscale.png')
    img = Image.open('greyscale.png', 'r')
    row, column = img.size
    image = list(img.getdata())
    intensity = {}
    for i in image:
        if i[0] in intensity:
            intensity[i[0]] += 1
        else:
            intensity[i[0]] = 1
    return intensity, row * column


# (d) Your result from (c) tells you the information encoded in each character of the book. Now multiply this by the
# number of characters in the book, to obtain the overall entropy of the book.

# (h) Your result from (g) tells you the information encoded in each pixel of the image. Now multiply this by the number
# of pixels in the image, to obtain the overall entropy of the book.
if __name__ == '__main__':
    # Entropy of BOOK
    count_dict, total = letterCount()
    overallBookEntropy = entropy(count_dict, total) * total
    print("Entropy of the book =", overallBookEntropy)
    # Entropy of IMAGE
    intensity_dict, total2 = pixel_intensity()
    overallImgEntropy = entropy(intensity_dict, total) * total
    print("Image Entropy: ", overallImgEntropy)

    
"""Final Output: 
Entropy of the book = 86614.4434486718
Image Entropy:  1046522.3118012662
"""



# (i) Which cWhich contains more information, the book or the image?ontains more information, the book or the image?
"""In my case the image contains more information as it had higher Overall Entropy."""

# (j) Do you think this is a fair comparison? Why, or why not?
"""I results depend on the type of data. So, I think it is not a fair comparison as it is dependent on the number of
characters in the book and its distribution and number of pixels in the image and its intensity. Also it is hard to 
compare the size this way."""
