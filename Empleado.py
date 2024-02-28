from fecha import fecha

class empleado: 
    nombre= ""
    apellido= ""   
    '''--------------------------------------------------------
    # Aqui va el codigo del empleado
    -----------------------------------------------------------'''
            
    genero = ""
    salario = 0
    '''--------------------------------------------------------
    #Aqui va el codigo del empleado
    -----------------------------------------------------------'''
    '''----------------------------------------------------
    # Aqui va el codigo del metodo 
    -------------------------------------------------------'''
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        '''---------------------------------------------------
        # Aqui va el codigo del nuevo empleado
        -------------------------------------------------------''' 
        return None
        
    def ConsultarSalario(self):
        '''----------------------------------------------------
        # Aqui va el codigo del metodo
     ----------------------------------------------------------'''
        return self.salario
    
    def ConsultarNombre(self):
        '''----------------------------------------------------
        # Aqui va el codigo del metodo
        -------------------------------------------------------'''
        return self.nombre
    
    def ConsultarApellido(self):
        '''----------------------------------------------------
        # Aqui va el codigo del metodo
        -------------------------------------------------------'''
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        '''----------------------------------------------------
        # Aqui va el codigo del metodo
        -------------------------------------------------------'''
        return self.nombre +" "+ self.apellido
    
    def AumentoSalarial(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario + self.salario
        self.salario = nSalario 

        return "El nuevo salario es de: "+self.salario 
    def Duplicarsalario(self):
        '''--------------------------------------------------------
        #Aqui va el codigo
        -----------------------------------------------------------'''
        #Forma 1
        #self.salario=self.salario*2
        self.salario *= 2
    def CalcularSalarioAnual(self):
        '''--------------------------------------------------------
        #Aqui va el codigo
        #Forma 1
        -----------------------------------------------------------'''
        return self.salario*12
        '''--------------------------------------------------------
        #Forma 2
        -----------------------------------------------------------'''
        salarioAnual = self.salario*12
        return salarioAnual


    


