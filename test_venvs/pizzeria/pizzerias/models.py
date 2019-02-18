from django.db import models

class Pizza(models.Model):
    """A pizza a user orders"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Topping(models.Model):
    """Toppings on a user's pizza order"""
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'toppings'
        
    def __str__(self):
        """Return a string representation of the moodel"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."
