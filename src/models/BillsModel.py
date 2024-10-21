from database.db import get_connection
from .entities.Bill import Bill


class BillModel:
    @classmethod
    def get_bill_by_id(self, identificacion=None):
        try:
            connection = get_connection()
            bills = []

            with connection.cursor() as cursor:
                query = """SELECT id,chs_data_dat,account_fiscal_id,
                               ruta_xml_comprobante_recibido,ruta_pdf_generado,
                               account_razon FROM public.csv_data  
                               WHERE  account_fiscal_id = %s LIMIT 10;"""
                cursor.execute(query, identificacion)

                resultset = cursor.fetchall()
                for row in resultset:
                    bill = Bill(row[0], row[1], row[2], row[3], row[4], row[5])
                    bills.append(bill.to_JSON())
            connection.close
            return bills

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_bill_by_id_date(
        self, identificacion=None, fecha_inicio=None, fecha_fin=None
    ):
        try:
            connection = get_connection()
            bills = []

            with connection.cursor() as cursor:
                query = """
                    SELECT id, chs_data_dat, account_fiscal_id, ruta_xml_comprobante_recibido, ruta_pdf_generado,account_razon
                    FROM public.csv_data
                    WHERE (%s IS NULL OR account_fiscal_id = %s)
                    AND (%s IS NULL OR chs_data_dat >= %s)
                    AND (%s IS NULL OR chs_data_dat <= %s)
                    LIMIT 10;
                """

                cursor.execute(
                    query,
                    (
                        identificacion,
                        identificacion,
                        fecha_inicio,
                        fecha_inicio,
                        fecha_fin,
                        fecha_fin,
                    ),
                )

                resulset = cursor.fetchall()
                for row in resulset:
                    bill = Bill(row[0], row[1], row[2], row[3], row[4], row[5])
                    bills.append(bill.to_JSON())
            connection.close
            return bills

        except Exception as ex:
            print(ex)
            raise Exception(ex)
