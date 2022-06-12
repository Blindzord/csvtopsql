class insert_in_db:
    def load_excel(self):
        import csv
        self.archivo = open (r"C:\Users\usr\Documents\portabilidadtest.csv")
        self.filas = csv.reader( self.archivo, delimiter= ",")
        self.lista = list(self.filas)
        #del(self.lista[0])
        self.tuplaa = tuple (self.lista)
        #for rw in self.tuplaa:
            #print(rw)

    def truncate_table(self):
        import psycopg2
        self.connection = psycopg2.connect("dbname=clientes_db user=user password=pasword")
        self.cursor = self.connection.cursor()
        self.query = "truncate table portabilidad"
        self.cursor.execute(self.query)
        self.connection.commit()
        self.cursor.close()
        self.connection.close() 

  
    def insert_numeros(self):
        import psycopg2
        self.connection = psycopg2.connect("dbname=clientes_db user=user password=pasword")
        self.cursor = self.connection.cursor()
        self.cursor.executemany ("insert into portabilidad (numero) values (%s)" ,self.tuplaa)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    #def select (self):
        #import psycopg2
        #self.connection = psycopg2.connect("dbname=clientes_db user=user password=pasword")
        #self.cursor = self.connection.cursor()
        #self.query = "SELECT numero FROM public.portabilidad"
        #self.cursor.execute(self.query)
        #self.all_items = self.cursor.fetchall()
        #self.cursor.close()
        #self.connection.close()
        #print(self.all_items)
        
ins_db = insert_in_db()
ins_db.load_excel()
ins_db.truncate_table()
ins_db.insert_numeros()
#ins_db.select()