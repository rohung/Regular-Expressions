class Person():

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Galt, John') 
        self.email = kwargs.get('email', 'john_galt@gmail.com')
        self.phone = kwargs.get('phone', '555-555-5555')
        self.job = kwargs.get('job', 'engineer, hiddenworld')
        self.twitter = kwargs.get('twitter', '@johngalt') 

        for key, value, in kwargs.items(): 
            setattr(self, key, value)

    def __str__(self): 
        return """
                Name: {}
                E-mail: {}
                Phone: {}
                Job and Company: {}
                Twitter: {}
                """.format(self.name, 
                           self.email, 
                           self.phone, 
                           self.job, 
                           self.twitter)