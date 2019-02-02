class mobile(object):
     
    def __init__(self, iphone, samsung, nokia):
        """Constructor"""
        self.iphone = iphone
        self.samsung = samsung
        self.nokia = nokia
    
    def block(self):
        """
        Block the phone
        """
        return "Bloking"
    
    def start(self):
        """
        Unblock the phone
        """
        return "Use phone!"
if __name__ == "__main__":
    phone = mobile("iOS", 5, 4)
    print(phone.iphone)
    
    author = mobile("Jobs", 3, 6)
    print(author.iphone)
