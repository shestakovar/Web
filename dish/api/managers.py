from django.db import models


class DishManager(models.QuerySet):
    def most_favs(self):
        return self.annotate(count=models.Count('bookmarks')).order_by('-count')

    def most_comments(self):
        return self.annotate(count=models.Count('comment')).order_by('-count')

    def alph(self):
        return self.order_by('name')
    
    def has_ingredients(self, temp):
        return self.filter(ingredients__in=temp).distinct()
    
    def in_bookmarks(self, user):
        return self.filter(bookmarks=user)
