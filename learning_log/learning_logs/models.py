from django.db import models

# Create your models here.
#add new model = migrate db again

#make a class Topic that inherits from parent class Model, imported from models
class Topic(models.Model):
    """A topic the user is learning about"""
    #set text attribute to CharField(params), imported from models
    #use this to store small amount of text
    text = models.CharField(max_length=200)
    #set date_added attribute to DateTimeField, DJ auto sets to current DTG
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

#class Entry that inherits from DJ base Model class
class Entry(models.Model):
    """Something specific learned about a topic"""
    #topic attribute is a FK instance (db term, connects entry to spec. topic
    #topic is assigned a key when created, calling that key calls that data
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #instance of TextField, no size limit
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    #nest class w/in Entry(). has extra info for mnging a model
    #set special attribute telling DJ to use 'entires' when it needs to 
    #refer to >1 entries
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a string representation of the model"""
        #tells DJ to return first 50 chars of text, then '...'
        if len(self.text)>50:
            return self.text[:50] + "..."
        else:
            return(str(self.text))
