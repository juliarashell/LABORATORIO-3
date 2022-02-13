def greeter(name, 
            title = 'Dr', 
            prompt = 'Welcome', 
            message = 'Live Long and Prosper') :
    print(prompt, title, name, '-', message)

    greeter(message = 'We like Python', name = 'Lloyd')

    greeter('Lloyd', message = 'We like Python')

    greeter(name='John', 'We like Python')
    