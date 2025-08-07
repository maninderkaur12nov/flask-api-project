from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from sqlalchemy import create_engine, text
from marshmallow import Schema, fields, ValidationError
import urllib
app = Flask(__name__)
api = Api(app)
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-SUJ2P8G\\MSSQLSERVER1;"
    "DATABASE=test1;"
    "Trusted_Connection=yes;"
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# --- API Route to Get All Records ---
@app.route('/currentcondition', methods=['GET'])
def get_all_conditions():
    try:
        with engine.connect() as conn:
            query = text("SELECT * FROM CurrentCondition")
            result = conn.execute(query)
            rows = result.fetchall()
            columns = result.keys()  # get column names

            # Convert each row to dictionary
            data = [dict(zip(columns, row)) for row in rows]
            return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # --- Run the app ---
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)