class NombreRomain:
    @staticmethod
    def convert(nombre):
        listConvertion=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
        i=1
        while i<=14:
            if(nombre==i):
                return listConvertion[i-1]
            i+=1