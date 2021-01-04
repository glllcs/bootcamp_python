import sys


class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def check_account(self):
        count = 0
        has_addr = 0
        if not hasattr(self, 'id'):
            print("Error: no attribute id")
            return False
        elif not hasattr(self, 'name'):
            print("Error: no attribute name")
            return False
        elif not hasattr(self, 'value'):
            print("Error: no attribute value")
            return False
        for attr in dir(self):
            if not attr.startswith('__') and attr != "ID_COUNT":
                count += 1
            if attr.startswith('b'):
                print("Error: an attribute starting with 'b'")
                return False
            elif attr.startswith('zip') or attr.startswith('addr'):
                has_addr = 1
        if has_addr != 1:
            print("Error: no attribute starting with 'addr' or 'zip'")
            return False
        # elif count % 2 == 0:
            # print("Error: an even number of attributes")
            # return False
        return True


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def __str__(self):
        txt = "-----\n"
        for acc in self.account:
            txt += str(acc.__dict__) + '\n'
        txt += "-----\n"
        return txt

    def add(self, account):
        self.account.append(account)

    def account_exists(self, name_id):
        if not isinstance(name_id, (int, str)):
            return None
        for acc in self.account:
            if acc.id == name_id or acc.name == name_id:
                return acc
        return None

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        if not isinstance(amount, (float, int)) or amount <= 0.0:
            print("Error: incorrect transfert amount.")
            return False
        acc1 = self.account_exists(origin)
        if acc1 is None:
            print("Error: origin account doesn't exist")
            return False
        elif not acc1.check_account():
            print("Error: origin account is corrupted")
            return False
        acc2 = self.account_exists(dest)
        if acc2 is None:
            print("Error: destination account doesn't exist")
            return False
        elif not acc2.check_account():
            print("Error: destination account is corrupted")
            return False
        elif acc1.value < amount:
            print("Error: origin account doesn't have this amount to transfer")
            return False
        elif acc1 == acc2:
            print("Error: origin and destination account are the same")
            return False
        acc1.transfer(-amount)
        acc2.transfer(amount)
        print(f"Successfully transfered ${amount} from {acc1.name} to",
              acc2.name)
        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        acc = self.account_exists(account)
        if acc is None:
            print(f"Cannot fix: '{account}' account doesn't exist")
            return False
        fixed = acc.check_account()
        if fixed is True:
            print(f"Cannot fix: '{account}' account isn't corrupted")
            return False
        while fixed is False:
            if not hasattr(acc, 'id'):
                acc.id = acc.ID_COUNT
                Account.ID_COUNT += 1
            if not hasattr(acc, 'name'):
                acc.name = input("What's the account's name from " + account +
                                 "? ")
            if not hasattr(acc, 'value'):
                acc.value = int(input("What's the account amount from " +
                                      account + "? "))
            count = 0
            has_zip = 0
            has_addr = 0
            for attr in dir(acc):
                if not attr.startswith('__') and attr != "ID_COUNT":
                    count += 1
                if attr.startswith('b'):
                    new_name = input("Enter new attribute name to replace "
                                     f"'{attr}'={acc.__dict__[attr]}: ")
                    acc.__dict__[new_name] = acc.__dict__.pop(attr)
                elif attr.startswith('zip') or attr.startswith('addr'):
                    has_addr = 1
            if has_addr != 1:
                acc.addr = input(f"Enter value to 'addr': ")
            fixed = acc.check_account()
        print("Error fixed!")
        return True
