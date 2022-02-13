def greeter(name, message = 'Live Long and Prosper'):
    print('Welcome', name, '-', message)

greeter('Eloise')
greeter('Eloise', 'Hope you like Python')

def greeter(message = 'Live Long and Prosper', name):
    print('Welcome', name, '-', message)
    