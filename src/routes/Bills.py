from flask import Blueprint, jsonify, request, send_file, abort
import os

# Models
from models.BillsModel import BillModel

main = Blueprint('bills_blueprint', __name__)


@main.route('/')
def get_bills_byid_date():
    try:
         # Imprimir todos los parámetros de consulta recibidos
        print("Request args:", request.args)
        
        # Capturar parámetros de la URL
        identificacion = request.args.get('identificacion')
        fecha_inicio = request.args.get('fecha_inicio')
        fecha_fin = request.args.get('fecha_fin')
        
        # Imprimir para depurar
        print(f"identificacion: {identificacion}")
        print(f"fecha_inicio: {fecha_inicio}")
        print(f"fecha_fin: {fecha_fin}")
        bills = BillModel.get_bill_by_id_date(identificacion= identificacion, fecha_inicio= fecha_inicio, fecha_fin=fecha_fin)
        return jsonify(bills)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
 
@main.route('/<id>')
def get_bills():
    try:
         # Imprimir todos los parámetros de consulta recibidos
        print("Request args:", request.args)
        
        # Capturar parámetros de la URL
        identificacion = request.args.get('identificacion')
        
        # Imprimir para depurar
        print(f"identificacion: {identificacion}")
      
        bills = BillModel.get_bill_by_id(identificacion= identificacion)
        return jsonify(bills)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
    
@main.route('/download', methods=['GET'])
def download_file():
    file_path = request.args.get('file')

    if file_path and os.path.exists(file_path):
        try:
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            return str(e), 500
    else:
        abort(404, description="File not found")
      
