from User import User

adrien = User("Adrien Rosales", "adrien@python.com")
nibbles = User("Mr. Nibbles", "nibbles@python.com")
benny = User("Benny Bob", "benny@python.com")

print("* Adrien transactions*")
adrien.make_deposit(1000).make_withdrawal(200).make_deposit(3000).make_deposit(500).display_user_balance()
print("* END Adrien transactions*\n")

print("* Nibbles transactions*")                                  # not enough funds for withdrawal
nibbles.make_deposit(3500).make_withdrawal(500).make_withdrawal(1500).make_withdrawal(8000).display_user_balance()
print("* END Nibbles transactions*\n")

print("* Benny transactions*")
benny.make_deposit(7000).make_withdrawal(1000).make_withdrawal(1900).make_withdrawal(1300).display_user_balance()
print("* END Benny transactions*\n")

print("* Transfer Adrien to Benny*")
adrien.transfer_money(benny, 1000).display_user_balance()
benny.display_user_balance()
print("* END BONUS*")
