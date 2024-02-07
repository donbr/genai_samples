# filename: output_numbers.py

class UserProxy:
    def stop(self):
        print("Stopping script...")
        exit(0)

for i in range(1, 101):
    print(i)

user_proxy = UserProxy()