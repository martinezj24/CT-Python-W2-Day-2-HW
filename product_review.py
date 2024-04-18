#Task 1: Keyword Highlighter

print('''
            Product Review Analysis
''')

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

def review_highlight(reviews):
    key_words = ['good','excellent','bad','poor','average']
    for review in reviews:
        for kw in key_words:
            if kw in review:
                review = review.replace(kw, kw.upper())
            elif kw.title() in review:
                review = review.replace(kw.title(), kw.upper())

        print(review)

review_highlight(reviews)

#Task 2: Sentiment Tally (rewrites the review_highlight variable)


def review_highlight(reviews):
    positive_words = ["good", "excellent", "great", "awesome", 
    "fantastic", "superb", "amazing"] 
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", 
    "disappointing", "subpar"]

    for review in reviews:
        positive_count = 0
        negative_count = 0
        for word in review.lower().split():
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
        print("Review:", review)
        print("Positive words:", positive_count)
        print("Negative words:", negative_count)
        print()



review_highlight(reviews)






#Task 3: Review Summary

summaries = []

for review in reviews:
    if len(review) > 30:
        summary_review = review[:30]+ '...'
    else:
        summary_review = review
    summaries.append(summary_review)

print(summaries)

#Not sure what Im missing here to actually append the '...' in a space
#but I could at least get it to append in the reviews
