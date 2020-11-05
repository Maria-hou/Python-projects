

# parent class
class User:
    name = 'Jane Doe'
    state = 'Pennsylvania'

    def welcome(self):
        msg = "\nWelcome to the 2020 presidential election in {}, {}.\
 Thank you for using your vote!".format(self.state,self.name)
        return msg

# child class with polymorphism
class Republican(User):
    name = 'Barry Wrie'
    party = 'Republican'
    candidate = 'Donald Trump'
    vote_format = 'in person'

    def welcome(self):
        msg = "\nWelcome to the {} voting center. On the behalf of {}\
 and the {} party, we thank you!".format(self.vote_format, self.candidate,\
                                         self.party)
        return msg

# child class with polymorphism
class Democratic(User):
    name = 'Amy Fine'
    party = 'Democratic'
    candidate = 'Joe Biden'
    vote_format = 'mail-in'
    
    def welcome(self):
        msg = "\nWelcome to the {} voting center. On the behalf of {}\
 and the {} party, we thank you!".format(self.vote_format, self.candidate,\
                                         self.party)
        return msg

if __name__ == "__main__":
    amy = Democratic()
    print(amy.welcome())

    barry = Republican()
    print(barry.welcome())
