class NombreRomain:
    @staticmethod
    def convert(nombre):
        listConvertion=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV']
        i=1
        while i<=24:
            if(nombre==i):
                return listConvertion[i-1]
            i+=1