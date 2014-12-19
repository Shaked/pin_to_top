"""
Pin to top plugin for Pelican
================================

Adds .pin variable to article's context and pins the article to the top 
 even if it is older than the other articles
"""
from pelican import signals
  
def update_pinned_articles(generator): 
    new_order = [] 
    # count articles and keep the pinned ordered by date
    pinned = 0; 
    for article in generator.context['articles']:
        if hasattr(article,'pin'): 
            new_order.insert(pinned,article)
            pinned += 1 
        else: 
            new_order.append(article)
    generator.context['articles'] = new_order

def register():
    signals.article_generator_finalized.connect(update_pinned_articles)
