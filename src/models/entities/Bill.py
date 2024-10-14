from utils.Dateformat import DateFormat

class Bill():
    
    def __init__(self,id, chs_data_dat=None,
                 account_fiscal_id=None, 
                ruta_xml_comprobante_recibido=None,
                 ruta_pdf_generado=None) -> None:
        self.id = id
        self.chs_data_dat =chs_data_dat
        self.account_fiscal_id= account_fiscal_id
        self.ruta_xml_comprobante_recibido = ruta_xml_comprobante_recibido
        self.ruta_pdf_generado = ruta_pdf_generado
    
    def to_JSON(self):
        return{
            'id': self.id,
            'chs_data_dat':  self.chs_data_dat,
            'account_fiscal_id':self.account_fiscal_id,
            'ruta_xml_comprobante_recibido':self.ruta_xml_comprobante_recibido,
            'ruta_pdf_generado': self.ruta_pdf_generado
        }
        
        
        
        
      