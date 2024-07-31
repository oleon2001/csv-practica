class vehiculo():
     
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.arrancar=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        if self.estado_vehiculo():
            print("El vehículo está en marcha")
        else:
            print("No se puede arrancar")

    def acelerar(self):
        if self.estado_vehiculo():
            print("Acelerando")
        else:
            print("No se puede acelerar")
    
    def estado(self):
        print("Marca:", self.marca, "\nModelo", self.modelo, "\nEnMarcha:", self.arrancar, 
             "\nAcelerando", self.acelera) 
        

    def estado_vehiculo(self, gasolina='ok', aceite='ok', puertas='cerradas'):
        if gasolina == 'ok' and aceite == 'ok' and puertas == 'cerradas':
            return True
        else:
            return False

mi_vehiculo = vehiculo('HONDA','CIVIC')
mi_vehiculo.estado_vehiculo(gasolina='ok', aceite='ok', puertas='cerradas')
mi_vehiculo.estado()
mi_vehiculo.arrancar()
mi_vehiculo.acelerar()