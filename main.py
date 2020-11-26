import eel, os

eel.init('web')

@eel.expose
def prefix(type):
    print(type)
    f = open('web/'+type+'.map')
    file = open('prefix.map', 'w')
    file.write(f.read())
    f.close()
    file.close()
    return '1'
@eel.expose
def username():
    user = os.environ.get('USERNAME')
    print (user)
    return user

eel.start('main.html',size=(700,400))
