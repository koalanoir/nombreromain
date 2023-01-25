class NombreRomain:
    @staticmethod
    def convert(nombre):
        listConvertion=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
        i=1
        while i<=12:
            if(nombre==i):
                return listConvertion[i-1]
            i+=1