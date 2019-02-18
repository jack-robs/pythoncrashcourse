from django.db import models

class Meal(models.Model):
    """A Meal user creates"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
        
class foodChoices(models.Model):
    """Food choices in each meal"""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'meal contents'
        
    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text)>50:
            return self.text[:50] + '...'
        else:
            return self.text
        
'''
working commands:

t = Topic.object.get(id=1)
t.entry_set.all()

'''
