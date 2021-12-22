import json
class Shipments:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def get_shipments(self, start_date, end_date):
        query = f"select s.shipment_id,s.weight_kg,s.distance_km,s.pickup_time,s.dropoff_time, sce.co2_emission \
                    from co2_emission_analytics.shipments s inner join co2_emission_analytics.shipment_co2_emissions sce \
                    on s.id =sce.shipment_id where s.dropoff_time between '"+start_date+"' and  '"+end_date+"'"
        self.cur.execute(query)
        columns = ("shipment_id","weight_(kg)","distance_(km)","pickup_time","drop_off_time","CO2_emission")
        results = []
        for row in self.cur.fetchall():
            results.append(dict(zip(columns,row)))
        self.cur.close()
        return results
