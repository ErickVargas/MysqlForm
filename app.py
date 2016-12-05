import web
# @
db = web.database(dbn='mysql', db='form', user='root', pw='1234')
#result = db.select('contactos')
#for row in result:
   # print row
#db.insert('contactos',nombre='aldo', telefono=12345, email='al@hot')

#db.update('contactos',where='id_contacto=3',email='ric@hot')

#db.delete('contactos',where='id_contacto=6')
num=2
#result=db.query("select * from contactos where id_contactos=1")
result=db.select('contactos',where= "id_contacto=%s"%(num))
for row in result:
    print row.nombre
