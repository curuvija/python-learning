from classes import User

def main():
    admin = User('Milos', 'Curuvija', 'curuvija@live.com', 'lozinka1')
    print(admin.__dict__)

if __name__ == '__main__':
    main()