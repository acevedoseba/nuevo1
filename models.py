from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#--------Usuario----------
class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)

    def serialize(self):
        return{
            "id": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#--------Producto----------

class Producto(db.Model):
    __tablename__ = 'Producto'
    id_producto = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(250), nullable= False)
    nombre = db.Column(db.String(250), nullable= False)
    valor_venta = db.Column(db.String(250), nullable= False)
    stock = db.Column(db.String(250), nullable= False)
    descripcion = db.Column(db.String(250), nullable= False)
    imagen = db.Column(db.String(250), nullable= True)
    estado = db.Column(db.String(250), nullable= False)
    

    def serialize(self):
        return{
            "id_producto": self.id_producto,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "valor_venta": self.valor_venta,
            "stock": self.stock,
            "descripcion": self.direccion,
            "imagen": self.imagen,
            "estado": self.estado
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


#--------Descuento_Producto----------

class Descuento_Producto(db.Model):
    __tablename__ = 'Descuento_Producto'
    producto_id = db.Column(db.Integer, primary_key=True)
    descuento_id = db.Column(db.String(250), nullable= False)
    fecha_inicio = db.Column(db.String(250), nullable= True)
    fecha_termino = db.Column(db.String(250), nullable= True)
    
    

    def serialize(self):
        return{
            "producto_id": self.producto_id,
            "descuento_id": self.descuento_id,
            "fecha_inicio": self.fecha_inicio,
            "fecha_termino": self.fecha_termino    
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------Descuento----------

class Descuento(db.Model):
    __tablename__ = 'Descuento'
    id_descuento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable= False)
    fecha = db.Column(db.String(250), nullable= False)
    porcentaje = db.Column(db.String(250), nullable= False)
    estado = db.Column(db.String(250), nullable= False)
    
    

    def serialize(self):
        return{
            "id_descuento": self.id_descuento,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "porcentaje": self.porcentaje,
            "estado": self.estado    
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------Detalle----------

#class Detalle(db.Model):
    __tablename__ = 'Detalle'
    id_detalle = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.String(250), nullable= False)
    valor = db.Column(db.String(250), nullable= False)
    descuento = db.Column(db.String(250), nullable= False)
    estado = db.Column(db.String(250), nullable= False)
    venta_id = db.Column(db.String(250), nullable= False)
    producto_id = db.Column(db.String(250), nullable= False)
    
    

    def serialize(self):
        return{
            "id_detalle": self.id_detalle,
            "cantidad": self.cantidad,
            "valor": self.valor,
            "descuento": self.descuento,
            "estado": self.estado,
            "venta_id": self.venta_id,
            "producto_id": self.producto_id
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------Descuento----------

#class Descuento(db.Model):
    __tablename__ = 'Descuento'
    id_descuento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable= False)
    fecha = db.Column(db.String(250), nullable= False)
    porcentaje = db.Column(db.String(250), nullable= False)
    estado = db.Column(db.String(250), nullable= False)
    
    

    def serialize(self):
        return{
            "id_descuento": self.id_descuento,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "porcentaje": self.porcentaje,
            "estado": self.estado    
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------Venta----------

class Venta(db.Model):
    __tablename__ = 'Venta'
    id_Venta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(250), nullable= False)
    descuento = db.Column(db.String(250), nullable= True)
    sub_total = db.Column(db.String(250), nullable= False)
    iva = db.Column(db.String(250), nullable= False)
    total = db.Column(db.String(250), nullable= False)
    estado = db.Column(db.String(250), nullable= False)
    cliente_id = db.Column(db.String(250), nullable= False)
    vendedor_id = db.Column(db.String(250), nullable= False)
    despacho_id = db.Column(db.String(250), nullable= False)
    
    

    def serialize(self):
        return{
            "id_Venta": self.id_Venta,
            "fecha": self.fecha,
            "descuento": self.descuento,
            "sub_total": self.sub_total,
            "iva": self.iva,
            "total": self.total,
            "estado": self.estado,
            "cliente_id": self.cliente_id,
            "vendedor_id": self.vendedor_id,
            "despacho_id": self.despacho_id
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------Despacho----------

class Despacho(db.Model):
    __tablename__ = 'Despacho'
    id_despacho = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(250), nullable= True)
    fecha_entrega = db.Column(db.String(250), nullable= True)
    hora_entrega = db.Column(db.String(250), nullable= True)
    rut_recibe = db.Column(db.String(250), nullable= True)
    nombre_recibe = db.Column(db.String(250), nullable= True)
    estado_despacho = db.Column(db.String(250), nullable= False)
    venta_id = db.Column(db.String(250), nullable= False)
    comuna_id = db.Column(db.String(250), nullable= False)
    

    def serialize(self):
        return{
            "id_despacho": self.id_despacho,
            "direccion": self.direccion,
            "fecha_entrega": self.fecha_entrega,
            "hora_entrega": self.hora_entrega,
            "rut_recibe": self.rut_recibe,
            "nombre_recibe": self.nombre_recibe,
            "estado_despacho": self.estado_despacho,
            "venta_id": self.venta_id,
            "comuna_id": self.comuna_id
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()        

#--------Cliente----------

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id_usuario = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(250), nullable= False)
    dv = db.Column(db.String(250), nullable= False)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    fono = db.Column(db.String(250), nullable= False)
    correo = db.Column(db.String(250), nullable= False)
    estado = db.Column(db.String(250), nullable= False)
    comuna_id = db.Column(db.String(250), nullable= False)
    

    def serialize(self):
        return{
            "id_usuario": self.id_usuario,
            "rut": self.rut,
            "dv": self.dv,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "correo": self.correo,
            "estado": self.estado,
            "comuna_id": self.comuna_id
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()        

#--------Vendedor----------

class Vendedor(db.Model):
    __tablename__ = 'Vendedor'
    id_vendedor = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(250), nullable= False)
    dv = db.Column(db.String(250), nullable= False)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    fono = db.Column(db.String(250), nullable= False)
    correo = db.Column(db.String(250), nullable= False)
    estado = db.Column(db.String(250), nullable= False)
    comuna_id = db.Column(db.String(250), nullable= False)
    

    def serialize(self):
        return{
            "id_vendedor": self.id_vendedor,
            "rut": self.rut,
            "dv": self.dv,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "correo": self.correo,
            "estado": self.estado,
            "comuna_id": self.comuna_id
            
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()      
        
#--------Comuna----------

class Comuna(db.Model):
    __tablename__ = 'Comuna'
    id_comuna = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable= False)
    region_id_region = db.Column(db.String(250), nullable= False)
    
    def serialize(self):
        return{
            "id_comuna": self.id_comuna,
            "nombre": self.nombre,
            "region_id_region": self.region_id_region    
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------region----------

class region(db.Model):
    __tablename__ = 'region'
    id_region = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable= False)

    def serialize(self):
        return{
            "id_region": self.id_region,
            "nombre": self.nombre  
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------Donacion----------

class Donacion(db.Model):
    __tablename__ = 'Donacion'
    id_donacion = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.String(250), nullable= False)
    fecha = db.Column(db.String(250), nullable= False)
    cliente_id = db.Column(db.String(250), nullable= False)
    
    

    def serialize(self):
        return{
            "id_donacion": self.id_donacion,
            "valor": self.valor,
            "fecha": self.fecha,
            "cliente_id": self.cliente_id    
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#--------Suscripcion----------

class Suscripcion(db.Model):
    __tablename__ = 'Suscripcion'
    id_suscripcion = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.String(250), nullable= False)
    fecha_termino = db.Column(db.String(250), nullable= True)
    cliente_id = db.Column(db.String(250), nullable= False)
    
    

    def serialize(self):
        return{
            "id_suscripcion": self.id_suscripcion,
            "fecha_inicio": self.fecha_inicio,
            "fecha_termino": self.fecha_termino,
            "cliente_id": self.cliente_id    
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()