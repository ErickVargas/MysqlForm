import web
# @
from web import form
render=web.template.render('templates')
urls = (
    '/', 'index',
    '/detalles/(.+)','detalles'
    
)
db = web.database(dbn='mysql', db='form', user='root', pw='1234')
myform = form.Form( 
    form.Textbox("Nombre"), 
    form.Textbox("telefono"),
    form.Textbox("email")
    ) 
class index:
    def GET(self):
        form = myform()
        result=db.select('contactos')
        return render.index(form,result)
        
    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.index(form)
        else:
            db.insert('contactos',nombre=form.d.Nombre, telefono=form.d.telefono, email=form.d.email)
            result=db.select('contactos')
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return render.index(form,result)
class detalles:
    def GET(self,id):
        #result=db.select('contactos' where='id_contacto=%s'%(id) )
        result=db.select('contactos',where= "id_contacto=%s"%(id))
        return render.detalles(result)
        #return "Listing info about user: {0}".format(id)

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()