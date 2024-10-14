from database.db import get_connection
from .entities.Bill import Bill

class BillModel():
    
    @classmethod
    def get_bill(self):
        try:
            connection=get_connection()
            bills=[]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id,concession_code,chs_data_dat,account_fiscal_id,ruta_xml_enviado,ruta_xml_recibido,ruta_xml_comprobante_recibido,ruta_pdf_generado FROM public.csv_data LIMIT 10;")
                resultset=cursor.fetchall()
                #print("result",resultset)
                for row in resultset:
                    bill=Bill(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    bills.append(bill.to_JSON())
            connection.close
            return bills
                    
        except Exception as ex:
            raise Exception(ex)